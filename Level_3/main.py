import src.utils as Utils
    

def main():
    input_type = input("Please choose your input type: \n1. Text\n2. File(.txt)\n")
    if input_type == "1":
        text = input("Please enter your text: \n")
    elif input_type == "2":
        file_path = input("Please enter the text file path: \n")
    else:
        print("Invalid input type.")
        return

    search_word = input("Please enter the word to search for: \n")
    word_counter = Utils.WordCounter()
    if input_type == "1":
        count = word_counter.word_frequencies(text, search_word)
        if count == 0:
            print(f"Your word ({search_word}) was not found.")
            return
        print(f"Your word ({search_word}) frequency is:", count)
    elif input_type == "2":
        count = word_counter.file_word_frequencies(file_path, search_word)
        if count == 0:
            print(f"Your word ({search_word}) was not found.")
            return
        print(f"Your word ({search_word}) frequency is:", count)


if __name__ == "__main__":
    main()
