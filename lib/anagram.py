


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = [i for i in word_list if sorted(i) == sorted(self.word)]
        return anagrams


