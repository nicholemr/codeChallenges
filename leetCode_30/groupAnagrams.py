class Solution:
    def groupAnagrams(self, strs):

        d = {}
        for word in strs:
            sorted_letters = sorted(list(word))
            sorted_word = "".join(sorted_letters)

            if d.get(sorted_word):
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]

        res = []
        for k, v in d.items():
            res.append(v)

        print(res)


sol = Solution()
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol.groupAnagrams(a)
