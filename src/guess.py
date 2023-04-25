from src.word import Word
from src.wordlist import WordList


class Guess:
    def __init__(self, word: Word):
        self.word = word
        self.is_correct = [False] * len(word.word)
        self.is_anywhere = [False] * len(word.word)
        self.num_attempts = 0

    def reset_marker(self):
        self.is_correct = [False] * len(self.word.word)
        self.is_anywhere = [False] * len(self.word.word)

    def get_num_attempts(self):
        return self.num_attempts

    def read(self, word_list: WordList):
        while True:
            guess = input("Enter your guess: ").strip().upper()
            if word_list.is_valid_word(Word(guess)):
                return Word(guess)

    def print_guess(self):
        for i in range(len(self.word.word)):
            if self.is_correct[i]:
                print(self.word.word[i], end=' ')
            elif self.is_anywhere[i]:
                print(self.word.word[i], end=' ')
            else:
                print('_', end=' ')
        print()

    def compare(self, guess: Word):
        for i in range(len(self.word.word)):
            if guess.word[i] == self.word.word[i]:
                self.is_correct[i] = True
            elif guess.word[i] in self.word.word:
                self.is_anywhere[i] = True
        return all(self.is_correct)

    def run(self, word_list):
        self.reset_marker()
        while self.num_attempts < 6:  # The loop will exit after 6 attempts
            guess = self.read(word_list)
            self.compare(guess)
            self.print_guess()
            if all(self.is_correct):
                return True
            self.num_attempts += 1  # Incrementing the number of attempts
        return False
