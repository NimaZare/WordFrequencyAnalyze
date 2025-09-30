# Word Frequency Analyzer

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

A simple Python project for analyzing and counting word occurrences in a given text.  
This project is organized with a modular structure, making it easy to extend and maintain.

---

## 📂 Project Structure

```
Level_4/
│
├── src/
│   └── utils/
│       ├── __init__.py         # Makes utils a package
│       └── counting_tools.py   # Contains functions for counting words
│       └── output_tools.py     # Contains functions for showing output
│
├── outputs/
│   └── # output pdf files save here
│
├── main.py                 # Entry point of the application
├── flowchart.png           # application flowchart
├── output.png              # display app output
└── README.md
```

---

## ⚡ Features

- Counts occurrences of a **specific word** in a given text (text or file .txt)
- Modular design for easy maintenance and scalability  
- Simple and beginner-friendly codebase  
- Show Chart, Text, Both (Chart and Text) in Output
- Can choose output display mode Just Show or Save to PDF (*new*)

---

## 🚀 Installation & Setup

1. **Clone this repository:**

```bash
git clone https://github.com/NimaZare/WordFrequencyAnalyze.git
cd WordFrequencyAnalyze/Level_4
```

2. **Run the project:**

```bash
python main.py
```

---

## 🛠️ Requirements

* Python 3.11+ (no external dependencies)

---

## 📌 Future Improvements

* Count all unique words and their frequencies
* Ignore punctuation and support more robust tokenization
* Add CLI for user input

---
