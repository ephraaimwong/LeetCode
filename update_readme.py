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
    "Easy": {"start": "<!-- START Easy -->", "end": "<!-- END Easy -->"},
    "Medium": {"start": "<!-- START Medium -->", "end": "<!-- END Medium -->"},
    "Hard": {"start": "<!-- START Hard -->", "end": "<!-- END Hard -->"}
}

GREENCHECK = "\u2705"
REDCROSS = "\u274C"

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
            readmePath = os.path.join(folderPath, "README.md")
            
            if os.path.isdir(folderPath) and os.path.exists(readmePath):
                print(f"{GREENCHECK} {questionFolder} README.md found.")
                meta = read_frontmatter(readmePath)
                # if meta and 'difficulty' in meta:
                if meta:
                    difficultyType = category.capitalize()
                    if difficultyType in rowsByDifficulty:
                        newRows = generate_MD_rows(meta, folderPath)
                        problemNumber = int(meta.get("number", 0))
                        rowsByDifficulty[difficultyType].append((problemNumber, newRows))
                        print(f" Mapped LC{problemNumber} to {difficultyType} table")
                    else:
                        print(f"{REDCROSS} Error: {difficultyType} is not a valid difficulty table.")
            else:
                print(f"{REDCROSS} {questionFolder} README.md not found.")
            
    root_readme = "README.md"
    if not os.path.exists(root_readme):
        print(f"{REDCROSS} Error: Root {root_readme} not found.")
        return
    with open(root_readme, "r", encoding="utf-8") as file:
        readmeText = file.read()
    
    for difficulty, data in rowsByDifficulty.items():
        markers = SECTIONS.get(difficulty)
        if not markers:
            continue
        
        header = [
            "| LeetCode #| Language | Solution |Algorithm/Approach|<div style= \"width:150px;\">Key Concept(s) </div>|",
            "| --- | --- | --- | --- | --- |"
            ]
            
        data.sort(key=lambda x:x[0])
        flatRows = []
        for _, rows in data:
            flatRows.extend(rows)
            
        newTable = "\n".join(header+flatRows)
        startTag = markers["start"]
        endTag = markers["end"]
        
        snippet = re.escape(startTag) + r"(.*?)" + re.escape(endTag)
        overwrite = f"{startTag}\n{newTable}\n{endTag}"
        
        
        # match = re.search(snippet, readmeText, flags=re.DOTALL)
        # if match:
        #     print(f"✅ FOUND tags for {difficulty}!")
        # else:
        #     print(f"❌ COULD NOT FIND tags for {difficulty}. Check your README spacing.")
        
        
        readmeText = re.sub(snippet, overwrite, readmeText, flags=re.DOTALL)
    with open(root_readme, "w", encoding="utf-8") as file:
        file.write(readmeText)
# if __name__ == "__main__":
#     update()
    
# def update():
#     print("🚀 STARTING DEBUG RUN...")
    
#     rowsByDifficulty = {key: [] for key in SECTIONS}
    
#     # 1. LOOP THROUGH CATEGORIES
#     # ⚠️ Check: Do your actual folders match these lowercase names exactly?
#     categories = ["easy", "medium", "hard"]
    
#     for category in categories:
#         if not os.path.exists(category):
#             print(f"⚠️  Skipping '{category}' (Folder not found)")
#             continue
            
#         print(f"📂 Scanning category: {category}...")
        
#         # 2. LOOP THROUGH PROBLEM FOLDERS
#         for questionFolder in os.listdir(category):
#             folderPath = os.path.join(category, questionFolder)
#             readmePath = os.path.join(folderPath, "readme.md") # Ensure this matches your file name!
            
#             # Check if it's a folder and has a readme
            # if os.path.isdir(folderPath):
            #     if os.path.exists(readmePath):
            #         print(f"   📄 Found README in {questionFolder}. Parsing...")
                    
            #         # 3. READ METADATA
            #         meta = read_frontmatter(readmePath)
                    
            #         if meta:
            #             # Check Difficulty
            #             if 'difficulty' in meta:
            #                 diff = meta['difficulty'].capitalize() # Force "Medium"
            #                 print(f"      ✅ Difficulty found: {diff}")
                            
            #                 if diff in rowsByDifficulty:
            #                     newRows = generate_MD_rows(meta, folderPath)
            #                     print(f"      🎉 Generated {len(newRows)} rows.")
            #                     problemNumber = int(meta.get("number", 0))
            #                     rowsByDifficulty[diff].append((problemNumber, newRows))
            #                 else:
            #                     print(f"      ❌ '{diff}' is not in SECTIONS keys!")
            #             else:
            #                 print(f"      ❌ Missing 'difficulty' key in YAML.")
            #         else:
            #             print(f"      ❌ YAML Parsing Failed (Check indentation/tabs).")
            #     else:
            #         print(f"   ⚠️  No readme.md found in {questionFolder}")

#     # 4. UPDATE THE ROOT README
#     root_readme = "readme.md" 
#     if not os.path.exists(root_readme):
#         print(f"❌ Error: {root_readme} not found.")
#         return

#     with open(root_readme, "r", encoding="utf-8") as file:
#         readmeText = file.read()
    
#     for difficulty, data in rowsByDifficulty.items():
#         markers = SECTIONS.get(difficulty)
#         if not markers:
#             continue
            
#         header = ["| LeetCode #| Language | Solution |Algorithm/Approach|<div style= \"width:150px;\">Key Concept(s) </div>|", "| --- | --- | --- | --- | --- |"]
        
#         # Debug: Tell us if we are about to update
#         if len(data) > 0:
#             print(f"💾 Updating {difficulty} with {len(data)} problems...")
#         else:
#             print(f"∅  No solutions found for {difficulty}.")

#         data.sort(key=lambda x:x[0])
#         flatRows = []
#         for _, rows in data:
#             flatRows.extend(rows)
            
#         newTable = "\n".join(header+flatRows)
#         startTag = markers["start"]
#         endTag = markers["end"]
        
#         snippet = re.escape(startTag) + r"(.*?)" + re.escape(endTag)
#         overwrite = f"{startTag}\n{newTable}\n{endTag}"
        
#         readmeText = re.sub(snippet, overwrite, readmeText, flags=re.DOTALL)
        
#     with open(root_readme, "w", encoding="utf-8") as file:
#         file.write(readmeText)
#     print("🏁 DONE.")

if __name__ == "__main__":
    update()