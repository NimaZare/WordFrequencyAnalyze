import string


class WordCounter:
    def __init__(self):
        self.text = ""
        self.search_word = ""

    def word_frequencies(self, text: str, search_word: str) -> int:
        """
        Count occurrences of a specific word in a given text (case-insensitive).
        """
        self.text = text
        self.search_word = search_word.lower()

        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = self.text.translate(translator).lower()

        words = cleaned_text.split()
        counter = sum(1 for word in words if word == self.search_word)

        return counter
