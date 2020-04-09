class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_alph_arr = self.create_char_list(S)
        t_alph_arr = self.create_char_list(T)

        return s_alph_arr == t_alph_arr

    def create_char_list(self, arr):
        alph_arr = []
        for char in arr:
            if char.isalpha():
                alph_arr.append(char)
            elif len(alph_arr) >= 1:
                alph_arr.pop()

        return alph_arr


sol = Solution()
S, T = "a##c", "#a#c"
S = "a#c"
T = "b"
S = "ab##"
T = "c#d#"
print(sol.backspaceCompare(S, T))
