import matplotlib.pyplot as plt


class OutputDisplay:
    def __init__(self):
        pass

    def display_text_output(self, search_word, count):
        """
        Display text-based output
        """
        if count == 0:
            print(f"Your word ({search_word}) was not found.")
        else:
            print(f"Your word ({search_word}) frequency is: {count}")


    def display_chart_output(self, search_word, count, text_or_file):
        """
        Display chart-based output
        """
        if count == 0:
            print(f"No data to display - word '{search_word}' was not found.")
            return

        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar([search_word], [count], color='skyblue', edgecolor='navy', linewidth=2)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_xlabel('Word', fontsize=12)
        ax.set_title(f'Word Frequency Analysis\nSource: {text_or_file}', fontsize=14, fontweight='bold')

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

        ax.grid(True, alpha=0.3, axis='y')
        ax.set_ylim(0, count * 1.2)

        plt.tight_layout()
        plt.show()


    def display_both_outputs(self, search_word, count, text_or_file):
        """
        Display both text and chart outputs
        """
        self.display_text_output(search_word, count)

        self.display_chart_output(search_word, count, text_or_file)


    def get_output_choice(self):
        """
        Get user's choice for output type
        """
        while True:
            print("\nPlease choose your output type:")
            print("1. Text")
            print("2. Chart")
            print("3. Both (Chart and Text)")

            choice = input("Enter your choice (1-3): ").strip()

            if choice in ['1', '2', '3']:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")



output_display = OutputDisplay()
