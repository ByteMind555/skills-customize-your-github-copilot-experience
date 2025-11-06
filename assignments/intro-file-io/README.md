# 📘 Assignment: Intro to File I/O

## 🎯 Objective

Learn how to read from and write to files in Python. Students will practice opening files, reading and parsing text, writing output, and handling simple file errors.

## 📝 Tasks

### 🛠️	Build a small file I/O utility

#### Description
Write a command-line program that can read lines from a text file, display a short preview to the user, and write a transformed version of the contents to a new file. The program should be well-structured using functions and include simple input validation.

#### Requirements
Completed program should:

- Accept a path to an input text file and an output file path (via command-line arguments or user input)
- Read the input file safely and show the first N lines as a preview (N can be fixed, e.g., 5)
- Transform the contents before writing (examples: convert to lowercase, strip extra whitespace, or reverse line order)
- Write the transformed content to the output file
- Handle common errors gracefully (file not found, permission denied) and show helpful messages
- Include a small usage/help message or docstring explaining how to run the program

### 🛠️	Optional Challenge: Line Statistics

#### Description
Add a feature that computes and prints simple statistics about the input file: number of lines, number of words, and number of characters.

#### Requirements
Completed program should:

- Print line/word/character counts for the input file when requested (e.g., via a --stats flag)
- Not crash on empty files
- Include the stats output in the README or program help text

---

## Starter files

This folder includes `starter-code.py` — a minimal scaffold you can extend. Replace or extend it as needed.
