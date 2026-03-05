# NLP-Syntax-Parsing-and-Text-Analysis-of-The-Picture-of-Dorian-Gray
## Overview

This project performs Natural Language Processing (NLP) analysis on *The Picture of Dorian Gray* by Oscar Wilde using Python and the NLTK library.

The goal of the project is to explore the structure of literary text through tokenization, part-of-speech tagging, and syntactic chunking. By analyzing noun phrases and verb phrases, we can gain insights into how language is used throughout the novel.

The project also includes visualizations such as word clouds and frequency plots to better understand patterns in the text.

---

## Features

* Text preprocessing and normalization
* Sentence and word tokenization
* Part-of-speech tagging
* Noun phrase and verb phrase chunking
* Frequency analysis of phrase structures
* Word cloud visualization
* Syntax tree visualization

---

## Technologies Used

* Python
* NLTK (Natural Language Toolkit)
* Matplotlib
* WordCloud
* Collections (Counter)

---

## Dataset

The text used in this project is *The Picture of Dorian Gray* by Oscar Wilde, sourced from **Project Gutenberg**.

Project Gutenberg Link:
https://www.gutenberg.org/ebooks/174

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/nlp-dorian-gray-analysis.git
cd nlp-dorian-gray-analysis
```

Install required libraries:

```bash
pip install nltk matplotlib wordcloud
```

Download required NLTK datasets:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
```

---

## Project Structure

```
nlp-dorian-gray-analysis
│
├── syntax_parsing_analysis.py
├── dorian_gray.txt
└── README.md
```

---

## Example Analysis

### Most Common Noun Phrases

The analysis extracts the most frequently occurring noun phrases in the novel, which often correspond to characters and descriptive objects.

### Most Common Verb Phrases

Verb phrase analysis highlights common actions and dialogue patterns used throughout the story.

### Visualizations

The project generates:

* Word clouds showing prominent words in the novel
* Bar charts of the most frequent noun phrases
* Syntax tree visualizations for parsed sentences

---

## Example Output

Word Frequency Visualization
Syntax Tree Parsing
Phrase Frequency Charts

These visualizations help reveal linguistic patterns in Oscar Wilde's writing style.

---

## Learning Outcomes

This project demonstrates:

* NLP preprocessing techniques
* Linguistic structure analysis
* Text mining
* Python-based data analysis
* Visualization of textual patterns

---

## Future Improvements

Possible extensions to this project include:

* Named Entity Recognition (NER) to analyze characters
* Sentiment analysis across chapters
* Topic modeling of themes in the novel
* Comparative analysis with other literary works

---

## Author
Nishka Mehta


Created as part of a Natural Language Processing learning project using Python and NLTK.
