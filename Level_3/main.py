import src.utils as utils


def main():
    count = 0
    text = ""
    file_path = ""
    text_source = ""

    print("=" * 30)
    print("Welcome to Word Analyzer!")
    print("=" * 30)

    while True:
        input_type = input(
            "\nPlease choose your input type: \n"
            "1. Text\n"
            "2. File(.txt)\n"
            "Enter choice (1-2): "
        )
        if input_type in ['1', '2']:
            break
        print("Invalid input type. Please enter 1 or 2.")


    if input_type == "1":
        text = input("\nPlease enter your text: \n")
        text_source = "Direct Text Input"
    elif input_type == "2":
        file_path = input("\nPlease enter the text file path: \n")
        text_source = f"File: {file_path}"

    search_word = input("\nPlease enter the word to search for: \n")

    if input_type == "1":
        count = utils.WordCounter.word_frequencies(text, search_word)
    elif input_type == "2":
        count = utils.WordCounter.file_word_frequencies(file_path, search_word)

    output_choice = utils.OutputDisplay.get_output_choice()

    print("\n" + "*" * 60)
    print("ANALYSIS RESULTS")
    print("*" * 60)

    if output_choice == "1":
        utils.OutputDisplay.display_text_output(search_word, count)
    elif output_choice == "2":
        utils.OutputDisplay.display_chart_output(search_word, count, text_source)
    elif output_choice == "3":
        utils.OutputDisplay.display_both_outputs(search_word, count, text_source)

    print("\nThank you for using Word Analyzer!")
    print("+" * 60)


if __name__ == "__main__":
    main()
