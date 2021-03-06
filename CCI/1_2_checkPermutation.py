import unittest


def check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    str1_d = {}

    for char in str1:

        str1_d[char] = str1_d.get(char, 0) + 1

    for char in str2:
        if str1_d.get(char) and str1_d.get(char) > 0:
            str1_d[char] -= 1
        else:
            return False

    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
