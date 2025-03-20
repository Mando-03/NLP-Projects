# Arabic Part-of-Speech (POS) Tagging

## Overview
This project focuses on **Arabic Part-of-Speech (POS) Tagging**, a fundamental task in Natural Language Processing (NLP). POS tagging involves assigning grammatical categories (e.g., noun, verb, adjective) to words in a sentence, which is crucial for understanding the structure and meaning of text. This repository explores two approaches to Arabic POS tagging:
1. **Farasa Model**: A state-of-the-art Arabic NLP toolkit.
2. **XLM-R Fine-Tuning**: Fine-tuning the XLM-RoBERTa (XLM-R) transformer model for Arabic POS tagging.

The project includes data preprocessing, model training, evaluation, and error analysis, providing a comprehensive pipeline for Arabic POS tagging.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Approaches](#approaches)
   - [Farasa Model](#farasa-model)
   - [XLM-R Fine-Tuning](#xlm-r-fine-tuning)
3. [Dataset](#dataset)
4. [Implementation](#implementation)
5. [Results](#results)
6. [Error Analysis](#error-analysis)
7. [Conclusion](#conclusion)
8. [Usage](#usage)

---

## Introduction
**Part-of-Speech (POS) Tagging** is a critical NLP task that assigns grammatical labels (e.g., noun, verb, adjective) to words in a sentence. For Arabic, POS tagging is particularly challenging due to the language's complex morphology and rich grammatical structure. This project explores two methods for Arabic POS tagging:
1. **Farasa**: A powerful Arabic NLP toolkit developed by Qatar Computing Research Institute (QCRI).
2. **XLM-R Fine-Tuning**: Fine-tuning the multilingual XLM-RoBERTa model for Arabic POS tagging.

---

## Approaches

### Farasa Model
Farasa is a state-of-the-art Arabic NLP toolkit that provides various functionalities, including POS tagging. It uses a rule-based approach combined with machine learning to achieve high accuracy in Arabic text processing. In this project, we use the Farasa POS tagger to tag Arabic text and visualize the results.

### XLM-R Fine-Tuning
XLM-RoBERTa (XLM-R) is a multilingual transformer model pre-trained on 100 languages, including Arabic. We fine-tune XLM-R on the **Arabic-PADT** dataset, a widely used dataset for Arabic POS tagging. The fine-tuning process involves tokenization, data preprocessing, model training, and evaluation.

---

## Dataset
The dataset used for this project is the **Arabic-PADT** treebank, which consists of 7,664 sentences (282,384 tokens) from newswire texts. The dataset is in **CoNLL-U format**, where each word is annotated with its POS tag and other linguistic features.

### Dataset Features
- **ID**: Token index.
- **FORM**: Surface form of the word.
- **LEMMA**: Lemma of the word.
- **UPOS**: Universal POS tag.
- **XPOS**: Language-specific POS tag.
- **FEATS**: Additional morphological features.
- **HEAD**: Head of the token in the dependency tree.
- **DEPREL**: Dependency relation.
- **MISC**: Miscellaneous information (e.g., transliteration, gloss).

---

## Implementation

### Farasa Model
- The Farasa POS tagger is used to tag Arabic text.
- The results are visualized using a dependency graph to show the relationships between words and their POS tags.

### XLM-R Fine-Tuning
1. **Data Preprocessing**:
   - Convert the dataset into a format suitable for fine-tuning.
   - Tokenize the text using the XLM-R tokenizer.
   - Align the POS tags with the tokenized input.
2. **Model Training**:
   - Fine-tune the XLM-R model using the Hugging Face `Trainer` API.
   - Evaluate the model on the test set using metrics like F1 score and accuracy.
3. **Error Analysis**:
   - Analyze the model's errors by examining high-loss examples and confusion matrices.

---

## Results
- The fine-tuned XLM-R model achieves an **F1 score of 97%** on the test set.
- The Farasa model provides accurate POS tagging for Arabic text, but its performance is not quantitatively evaluated in this project.
![img](https://i.imgur.com/UTgWPUM.png)

---

## Error Analysis
- The model struggles with certain tokens, such as **non-POS tokens (X)** and **punctuation marks**.
- Some errors are due to incorrect annotations in the dataset (e.g., labeling "نحن" as `X` instead of `PRON`).
- The confusion matrix and high-loss examples provide insights into the model's weaknesses.

---

## Conclusion
- The fine-tuned XLM-R model performs well on Arabic POS tagging, achieving high accuracy.
- Farasa is a reliable tool for Arabic POS tagging, but it may require additional customization for specific use cases.
- Future work could focus on refining the dataset and exploring other transformer models for Arabic NLP tasks.

---

## Usage
1. **Farasa Model**:
   - Run the notebook cells related to Farasa to tag Arabic text and visualize the results.

2. **XLM-R Fine-Tuning**:
   - Follow the steps in the notebook to preprocess the data, fine-tune the model, and evaluate its performance.

---
