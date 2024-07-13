class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} # mapping the character count to the list of anagrams

        for element in strs:
            count = [0] * 26 # only 26 since the characters consist of lowercase English letters
            for char in element:
                count[ord(char)-ord("a")] += 1
            keyCount = tuple(count)
            if keyCount in result:
                result[keyCount].append(element)
            else:
                result[keyCount] = [element]
            
        groupedAnagrams = []
        for value in result.values():
            groupedAnagrams.append(value)
        return groupedAnagrams