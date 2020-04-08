import unittest

# with additional data structure:


def unique(str):
    char_set = set()
    for char in str:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# without additional data structure:


# def unique(str):
#     for char in str:
#         count = 0
#         for letter in str:
#             if char == letter:
#                 count += 1
#         if count > 1:
#             return False
#     return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
