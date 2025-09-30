import string


class WordCounter:
    def __init__(self):
        self.text = ""
        self.search_word = ""

    def word_frequencies(self, text: str, search_word: str) -> int:
        """
        Count occurrences of a specific word in a given text (case-insensitive).
        """
        try:
            self.text = text
            self.search_word = search_word.lower()

            translator = str.maketrans("", "", string.punctuation)
            cleaned_text = self.text.translate(translator).lower()

            words = cleaned_text.split()
            counter = sum(1 for word in words if word == self.search_word)

            return counter
        except Exception as e:
            print("Error:", e)
            return 0

    def file_word_frequencies(self, file_path: str, search_word: str) -> int:
        """
        Count occurrences of a specific word in a text file (case-insensitive).
        """
        try:
            with open(file_path.replace('"', ''), 'r') as file:
                text = file.read()
            return self.word_frequencies(text, search_word)
        except Exception as e:
            print("Error:", e)
            return 0


word_counter = WordCounter()
