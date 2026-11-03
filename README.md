
# Intelligent Sentence Analyzer Using NLP

## 1. Project Overview

The **Intelligent Sentence Analyzer Using NLP** is a web-based application developed using Python and Natural Language Processing (NLP) techniques.

The application accepts a sentence or paragraph as input and performs linguistic analysis to identify sentence structure, grammatical relationships, and important language features.

It uses the spaCy English language model for NLP processing and Streamlit to provide an interactive user interface.

## 2. Objectives

The main objectives of this project are:

- To perform sentence segmentation and tokenization.
- To identify the parts of speech of words.
- To perform lemmatization and stemming.
- To analyze grammatical relationships using dependency parsing.
- To visualize sentence structure through dependency parse trees.
- To identify named entities in the input text.
- To identify stopwords and punctuation.
- To export the analysis results as a CSV file.

## 3. Features

### 3.1 Sentence Segmentation
Divides the input paragraph into individual sentences.

### 3.2 Tokenization
Splits sentences into individual words and punctuation marks.

### 3.3 Part-of-Speech Tagging
Identifies grammatical categories such as:

- Noun
- Verb
- Adjective
- Adverb
- Pronoun
- Determiner
- Preposition

### 3.4 Lemmatization
Converts words into their dictionary or base forms.

Example:

- running → run
- studies → study

### 3.5 Stemming
Uses two stemming algorithms:

- Porter Stemmer
- Snowball Stemmer

### 3.6 Dependency Parsing
Identifies grammatical relationships between words in a sentence.

The application generates a separate hierarchical dependency parse tree for each sentence.

Some dependency labels include:

- ROOT – Main word of the sentence
- nsubj – Nominal subject
- obj – Object
- det – Determiner
- amod – Adjectival modifier

### 3.7 Named Entity Recognition (NER)
Identifies named entities such as:

- PERSON
- ORGANIZATION
- LOCATION
- DATE
- MONEY

### 3.8 Stopword and Punctuation Analysis
Identifies common stopwords and punctuation marks in the input text.

### 3.9 CSV Export
Allows users to download the complete token-level analysis as a CSV file.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| spaCy | NLP processing and dependency parsing |
| NLTK | Porter and Snowball stemming |
| Pandas | Data handling and CSV generation |
| Matplotlib | Dependency tree visualization |

## 5. Project Structure

```text
Intelligent_Sentence_Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## 6. Installation and Setup

### Step 1: Install Python

Install Python 3.8 or a compatible newer version.

### Step 2: Clone or Download the Project

Download the project files and open the project folder in your terminal or command prompt.

### Step 3: Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

### Step 4: Download the spaCy English Model

Run:

```bash
python -m spacy download en_core_web_sm
```

## 7. Running the Application

Open the terminal in the project directory and execute:

```bash
streamlit run app.py
```

The application will open in your default web browser.

If it does not open automatically, use the local URL displayed in the terminal.

## 8. How to Use the Application

1. Open the application in your browser.
2. Select an example sentence or choose Custom input.
3. Enter a sentence or paragraph in the text area.
4. Click the **Analyze Text** button.
5. View the analysis summary.
6. Explore sentence segmentation and tokenization.
7. Examine POS tags, lemmas, and stemmed words.
8. View the dependency parse tree generated separately for each sentence.
9. Examine the named entities, stopwords, and punctuation.
10. Download the complete analysis using the CSV export button.

## 9. Example Input

```text
The boy eats an apple.
His sister drinks milk.
Neena reads a book.
```

The application processes all three sentences and generates a separate dependency parse tree for each sentence.

## 10. Expected Output

The application displays:

- Total number of tokens.
- Total number of sentences.
- Number of alphabetic tokens.
- Number of named entities.
- Sentence segmentation results.
- Tokenization results.
- POS tagging table.
- Lemmatization and stemming table.
- Individual dependency parse trees.
- Dependency relationship details.
- Named entity recognition results.
- Stopwords and punctuation.
- Downloadable CSV file.

## 11. Limitations

- The application primarily supports English text.
- NLP predictions depend on the pretrained spaCy model.
- Stemming may produce word forms that are not dictionary words.
- Dependency parsing may not always identify complex grammatical structures correctly.
- Named entity recognition may miss some entities.
- The application does not train a new NLP model from scratch.

## 12. Future Enhancements

Possible future improvements include:

- Support for multiple languages.
- Integration of transformer-based NLP models.
- Sentiment analysis.
- Text summarization.
- Grammar checking and correction.
- Improved dependency tree visualization.
- Interactive parse trees.
- Support for larger documents and file uploads.

## 13. Conclusion

The Intelligent Sentence Analyzer Using NLP provides an interactive platform for understanding the grammatical and linguistic structure of text.

By combining sentence segmentation, tokenization, POS tagging, stemming, lemmatization, dependency parsing, and named entity recognition, the application demonstrates how NLP techniques can be used to analyze natural language.

The project also provides visual dependency trees and downloadable CSV results, making the analysis easier to understand and reuse.

## 14. References

1. spaCy Documentation: https://spacy.io/usage
2. Streamlit Documentation: https://docs.streamlit.io/
3. NLTK Documentation: https://www.nltk.org/
4. Pandas Documentation: https://pandas.pydata.org/docs/
5. Matplotlib Documentation: https://matplotlib.org/stable/

