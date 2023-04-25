from random import shuffle

from src.word import Word


class WordList:
    def __init__(self, filename: str):
        with open(filename, 'r') as f:
            self.words = [Word(line.strip()) for line in f]
        shuffle(self.words)
        self.counter = 0

    def get_next_word(self):
        if self.counter < len(self.words):
            word = self.words[self.counter]
            self.counter += 1
            return word
        return None

    def is_valid_word(self, word: Word):
        return word in self.words
