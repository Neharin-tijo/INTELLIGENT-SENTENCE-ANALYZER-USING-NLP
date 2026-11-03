
# Evaluation Plan
## Intelligent Sentence Analyzer Using NLP

## 1. Introduction

The purpose of this evaluation plan is to assess the functionality, correctness, usability, and performance of the Intelligent Sentence Analyzer Using NLP.

The application accepts English sentences and paragraphs and performs various Natural Language Processing operations using spaCy and NLTK.

The evaluation focuses on verifying whether each implemented feature works correctly and produces meaningful results.

## 2. Evaluation Objectives

The main objectives of evaluation are:

- To verify correct sentence segmentation.
- To check tokenization of input text.
- To evaluate Part-of-Speech (POS) tagging.
- To verify lemmatization and stemming.
- To examine dependency parsing and parse tree visualization.
- To test Named Entity Recognition (NER).
- To verify stopword and punctuation identification.
- To test CSV export functionality.
- To evaluate the usability and reliability of the application.

## 3. Evaluation Strategy

The application will be evaluated using functional testing, output validation, usability testing, and basic performance testing.

### 3.1 Functional Testing

Each feature will be tested independently to verify that it performs its intended operation.

### 3.2 Output Validation

The generated NLP results will be examined to check whether the output is reasonable and consistent with the input text.

### 3.3 Usability Testing

The user interface will be evaluated based on ease of use, clarity of output, and accessibility of features.

### 3.4 Performance Testing

The application will be tested with inputs of different lengths to observe its response time and stability.

## 4. Test Environment

| Component | Configuration |
|---|---|
| Programming Language | Python |
| Interface | Streamlit |
| NLP Library | spaCy |
| English Model | en_core_web_sm |
| Stemming Library | NLTK |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Operating System | Windows / Linux |
| Input Format | English text |
| Output Format | Web interface and CSV |

## 5. Test Cases

| Test ID | Test Description | Input | Expected Result |
|---|---|---|---|
| TC01 | Single sentence input | The boy eats an apple. | Sentence should be analyzed successfully. |
| TC02 | Multiple sentences | Three sentences in one input | Each sentence should be identified separately. |
| TC03 | Paragraph input | A paragraph containing multiple sentences | All sentences should be processed. |
| TC04 | Tokenization | The boy eats an apple. | Individual tokens should be displayed. |
| TC05 | POS tagging | The boy eats an apple. | Words should receive grammatical tags. |
| TC06 | Lemmatization | running, studies | Base forms should be generated. |
| TC07 | Stemming | playing, studies | Porter and Snowball stems should be displayed. |
| TC08 | Dependency parsing | The boy eats an apple. | A dependency tree should be displayed. |
| TC09 | Multiple dependency trees | Three sentences | A separate tree should be generated for each sentence. |
| TC10 | Named Entity Recognition | Neha lives in India. | Recognized entities should be displayed if detected by the model. |
| TC11 | Stopword identification | The boy is in the garden. | Stopwords should be identified. |
| TC12 | Punctuation detection | Hello, world! | Punctuation marks should be identified. |
| TC13 | Empty input | Blank text | A warning message should be displayed. |
| TC14 | CSV export | Any valid input | A CSV file should be downloadable. |
| TC15 | Custom paragraph | User-entered paragraph | All implemented NLP operations should run successfully. |

## 6. Evaluation Metrics

The following criteria will be used to evaluate the application.

### 6.1 Functional Correctness

Checks whether each NLP operation produces the expected type of output.

### 6.2 Sentence Segmentation Accuracy

Checks whether the input text is divided into appropriate individual sentences.

### 6.3 Tokenization Correctness

Checks whether words and punctuation marks are separated appropriately.

### 6.4 POS Tagging Quality

Checks whether grammatical categories are assigned appropriately.

### 6.5 Dependency Parsing Quality

Checks whether syntactic relationships and root words are identified reasonably.

### 6.6 Named Entity Recognition Quality

Checks whether names of people, locations, organizations, dates, and other supported entities are identified.

### 6.7 Response Time

Measures the time taken by the application to process the input and display results.

### 6.8 Usability

Evaluates the clarity of the interface and ease of interaction.

## 7. Expected Results

The application is expected to:

- Process individual sentences and paragraphs.
- Display the number of sentences and tokens.
- Generate POS tagging and morphological information.
- Display lemma and stem forms.
- Generate separate dependency parse trees for individual sentences.
- Identify named entities when present.
- Display stopwords and punctuation marks.
- Provide downloadable CSV results.
- Display appropriate warnings for invalid or empty input.

## 8. Evaluation Procedure

The following steps will be followed during evaluation:

1. Start the Streamlit application.
2. Enter a simple English sentence.
3. Verify sentence segmentation and tokenization.
4. Examine POS tags and morphological information.
5. Check lemmatization and stemming results.
6. Verify the dependency parse tree.
7. Enter multiple sentences and verify that separate trees are generated.
8. Enter a paragraph and inspect the complete analysis.
9. Test Named Entity Recognition.
10. Check stopword and punctuation identification.
11. Download the CSV file and verify its contents.
12. Test empty input and other edge cases.
13. Record observations and identify any errors.

## 9. Evaluation Result Recording

The following table can be completed after testing the application.

| Test ID | Test Status | Observations |
|---|---|---|
| TC01 | Not Tested | |
| TC02 | Not Tested | |
| TC03 | Not Tested | |
| TC04 | Not Tested | |
| TC05 | Not Tested | |
| TC06 | Not Tested | |
| TC07 | Not Tested | |
| TC08 | Not Tested | |
| TC09 | Not Tested | |
| TC10 | Not Tested | |
| TC11 | Not Tested | |
| TC12 | Not Tested | |
| TC13 | Not Tested | |
| TC14 | Not Tested | |
| TC15 | Not Tested | |

*Update the test status to Pass or Fail after executing each test case.*

## 10. Limitations

- The application primarily supports English text.
- Results depend on the pretrained spaCy language model.
- POS tagging and dependency parsing may produce errors for ambiguous or complex sentences.
- Stemming does not always produce valid dictionary words.
- NER may fail to recognize unfamiliar names and domain-specific entities.
- Performance may vary depending on input length and system resources.
- The application does not independently train or fine-tune an NLP model.

## 11. Conclusion

This evaluation plan provides a systematic approach to testing the Intelligent Sentence Analyzer Using NLP.

By conducting functional, output validation, usability, and performance testing, the reliability and usefulness of the application can be assessed.

The evaluation will help identify implementation issues and provide directions for future improvements.
