import src.utils as Utils
    

def main():
    text = input("Please enter your text: \n")
    search_word = input("Please enter the word to search for: \n")
    word_counter = Utils.WordCounter()
    print(f"Your word ({search_word}) frequency is:", word_counter.word_frequencies(text, search_word))


if __name__ == "__main__":
    main()
