from src.word import Word


class WordTest:

    def perform_tests(self):
        word = Word("hello")
        assert str(word) == "HELLO"
