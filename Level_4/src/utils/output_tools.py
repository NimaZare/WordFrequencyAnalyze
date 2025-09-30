import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

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
    
    def save_to_pdf(self, search_word, count, text_or_file, filename=None):
        """
        Save output to PDF file with text and chart
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Level_4/outputs/word_frequency_{search_word}_{timestamp}.pdf"
        
        with PdfPages(filename) as pdf:
            fig = plt.figure(figsize=(8.5, 11))
            
            fig.text(0.5, 0.95, 'Word Frequency Analysis Report', 
                    ha='center', fontsize=16, fontweight='bold')
            fig.text(0.5, 0.90, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                    ha='center', fontsize=10, style='italic')
            
            fig.text(0.1, 0.82, f'Your search word is: "{search_word}"',
                    fontsize=14, fontweight='bold')
            
            if count == 0:
                fig.text(0.1, 0.77, f'Result: The word was not found in the source.',
                        fontsize=12, color='red')
            else:
                fig.text(0.1, 0.77, f'Frequency: {count} occurrence(s)',
                        fontsize=12, color='green', fontweight='bold')
            
            fig.text(0.1, 0.72, f'Source: {text_or_file}',
                    fontsize=10, style='italic')
            
            if count > 0:
                ax = fig.add_subplot(111)
                ax.set_position([0.15, 0.15, 0.7, 0.45])
                
                bars = ax.bar([search_word], [count], color='skyblue', 
                             edgecolor='navy', linewidth=2)
                ax.set_ylabel('Frequency', fontsize=12)
                ax.set_xlabel('Word', fontsize=12)
                ax.set_title('Frequency Chart', fontsize=13, fontweight='bold', pad=20)
                
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width() / 2., height,
                           f'{int(height)}',
                           ha='center', va='bottom', fontsize=12, fontweight='bold')
                
                ax.grid(True, alpha=0.3, axis='y')
                ax.set_ylim(0, count * 1.2)
            
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
        
        print(f"\n🟢 PDF saved successfully as: {filename}")
        return filename
    
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

    def display_output(self):
        while True:
            print("\nPlease choose your output show mode:")
            print("1. Just Show")
            print("2. Save to PDF")

            choice = input("Enter your choice (1-2): ").strip()

            if choice in ['1', '2']:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")



output_display = OutputDisplay()
