# Text to Handwriting Converter

A simple Python project that converts typed text into a handwritten-style image using the PyWhatKit library.

## Features

- Convert text into handwriting style
- Save output as an image file
- Easy and beginner-friendly
- Simple Python implementation

## Technologies Used

- Python
- PyWhatKit

## Installation

Install the required library:

```bash
pip install pywhatkit
```

## Usage
```python
import pywhatkit as pw

text = """
Hello!
My name is Zoya Rana.
This text is converted into Handwritten.
"""

pw.text_to_handwriting(
    text,
    save_to="handwritten.png"
)

print("Handwritten image saved successfully")
```

## Output
The program generates a handwritten-style image and saves it as:

```text
handwritten.png
```

## Project Structure
```text
Text-to-Handwriting-Converter/
│
├── main.py
├── handwritten.png
└── README.md
```

## Learning Outcomes
- Working with Python libraries
- Function usage
- Image generation
- Basic project development

## Author
Zoya Sarwar
