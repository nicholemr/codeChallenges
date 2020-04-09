class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}
        self.add_to_words_to_counts(input_string)

    def add_to_words_to_counts(self, str):

        sindex = 0
        eindex = 0
        temp_word = ''
        for i, char in enumerate(str):
            if char.isalpha():
                # print(char)
                temp_word += char
            elif len(temp_word) > 1 or (len(temp_word) == 1 and temp_word in 'ai'):
                self.words_to_counts[temp_word.capitalize()] = self.words_to_counts.get(
                    temp_word.capitalize(), 0)+1
                temp_word = ''
            else:
                temp_word = ''


input = 'Chocolate cake for dinner and pound cake for dessert'
input = "Allie's Bakery: Sasha's Cakes"
input = 'Strawberry short cake? Yum!'
# input = 'Mmm...mmm...decisions...decisions'
wcd = WordCloudData(input)
print(wcd.words_to_counts)
