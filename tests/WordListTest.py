from src.word import Word
from src.wordlist import WordList


class WordListTest:

    def perform_tests(self):
        # Create a test file with some words
        with open("test_words.txt", "w") as f:
            f.write("apple\norange\nbanana")

        word_list = WordList("test_words.txt")
        assert len(word_list.words) == 3
        assert word_list.is_valid_word(Word("apple"))
        assert not word_list.is_valid_word(Word("pear"))

        # Clean up the test file
        import os
        os.remove("test_words.txt")
