class Word:
    def __init__(self, word: str):
        self.word = word.upper()

    def __str__(self):
        return self.word

    def __eq__(self, other):
        return self.word == other.word

    def __hash__(self):
        return hash(self.word)

    def __len__(self):
        return len(self.word)

    def __getitem__(self, index):
        return self.word[index]

    def __iter__(self):
        return iter(self.word)

    def __contains__(self, item):
        return item in self.word