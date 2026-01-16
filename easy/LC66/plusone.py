class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        """
        ---- Solution Intent 1 (Convert to num then array) ----
        use 10**power to get number from array
        use %10 to extract rightmost digit, push to array then reverse
        """
        power = 0
        num = 0
        for i in range(len(digits)-1, -1, -1):
            num += digits[i] * (10**power)
            power+=1
        num +=1
        print(num)
        array = []
        i = 1
        while num > 0:
            array.append(num % 10)
            num //= 10
            i += 1
        print(array)
        array.reverse()
        print(array)
        return array
        """
        ---- Solution Intent 2 (Directly Manipulate Array) ----    
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits # will only reach here if all 9's