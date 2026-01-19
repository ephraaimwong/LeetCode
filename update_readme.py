import os
import re
import yaml

# ---- REPO CONFIGURATIONS ----

# parent = "readme.md"
# dirToScan = ["easy", "medium", "hard"]
# child = "child_folder/readme.md"

# childOpenTag = ""
# parentOpenTag = ""
# childCloseTag = ""
# parentCloseTag = ""

SECTIONS = {
    "Easy": {"start": "", "end": ""},
    "Medium": {"start": "", "end": ""},
    "Hard": {"start": "", "end": ""}
}

def read_frontmatter(file):
    """
    Read YAML front matter in child readme
    """
    if not os.path.exists(file):
        return None
    with open(file, "r", encoding="utf-8") as filename:
        content = filename.read()
    
    sections = content.split("---", 2)
    
    if len(sections)<3:
        return None
    
    yamlText = sections[1]
    
    try:
        meta = yaml.safe_load(yamlText)
        if not isinstance(meta, dict): 
            return None
        return meta
    except yaml.YAMLError as e:
        print(f"YAML Error in {file}:\n     {e}")
        return None
    
def generate_MD_rows(meta, folder):
    rows = []
    
    number = meta.get("number", "?")
    name = meta.get("name", "Unknown")
    url = meta.get("url", "?")
    
    problemLink = f"[{number} - {name}]({url})"
    
    solutions = meta.get("solutions", [])
    if not solutions:
        return []
    
    for i in solutions:
        language = i.get("language", "Unknown")
        filename = i.get("filename", "")
        algorithm = i.get("algorithm", "")
        
        summary = i.get("summary", "")
        if summary:
            summary = summary.strip().replace("\n","<br>")
        
        if filename:
            filepath = os.path.join(folder, filename).replace("\\", "/")
            filepath = f"[{filename}]({filepath})"
        else:
            filepath = "No File Found"
        
        MD_Row = f"|{problemLink}|{language}|{filepath}|{algorithm}|{summary}|"
        rows.append(MD_Row)
    
    return rows

def update():
    rowsByDifficulty = {key: [] for key in SECTIONS}
    for category in ["easy", "medium", "hard"]:
        if not os.path.exists(category):
            continue
        for questionFolder in os.listdir(category):
            folderPath = os.path.join(category, questionFolder)
            readmePath = os.path.join(folderPath, "readme.md")
            
            if os.path.isdir(folderPath) and os.path.exists(readmePath):
                meta = read_frontmatter(readmePath)
                if meta and 'difficulty' in meta:
                    difficultyType = meta['difficulty'].capitalize()
                    if difficultyType in rowsByDifficulty:
                        newRows = generate_MD_rows(meta, folderPath)
                        problemNumber = int(meta.get("number", 0))
                        rowsByDifficulty[difficultyType].append((problemNumber, newRows))
    root_readme = "readme.md"
    if not os.path.exists(root_readme):
        print(f"Error: {root_readme} not found.")
        return
    with open(root_readme, "r", encoding="utf-8") as file:
        readmeText = file.read()
    
    for difficulty, data in rowsByDifficulty.items():
        markers = SECTIONS.get(difficulty)
        if not markers:
            continue
        data.sort(key=lambda x:x[0])
        flatRows = []
        for _, rows in data:
            flatRows.extend(rows)
            
        newTable = "\n".join(flatRows)
        startTag = markers["start"]
        endTag = markers["end"]
        
        snippet = re.escape(startTag) + r"(.*?)" + re.escape(endTag)
        overwrite = f"{startTag}\n{newTable}\n{endTag}"
        
        readmeText = re.sub(snippet, overwrite, readmeText, flags=re.DOTALL)
    with open(root_readme, "w", encoding="utf-8") as file:
        file.write(readmeText)
    if __name__ == "__main__":
        update()