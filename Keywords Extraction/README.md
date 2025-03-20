# Keywords Extraction using KeyBERT

This project demonstrates how to use **KeyBERT**, a minimal and easy-to-use Python library, for keyword extraction from financial articles. KeyBERT leverages **BERT (Bidirectional Encoder Representations from Transformers)** embeddings to extract the most relevant keywords or key phrases from a given document. The project includes text preprocessing, keyword extraction, and semantic search to find articles related to specific topics.

---

## Table of Contents
1. [Introduction](#introduction)
2. [KeyBERT Overview](#keybert-overview)
3. [Dataset](#dataset)
4. [Text Preprocessing](#text-preprocessing)
5. [Keyword Extraction](#keyword-extraction)
6. [Semantic Search](#semantic-search)
7. [Results](#results)

---

## Introduction
Keyword extraction is a crucial task in natural language processing (NLP) that involves identifying the most relevant words or phrases from a document. This project uses **KeyBERT**, a Python library that combines BERT embeddings with cosine similarity to extract keywords. The project is applied to a dataset of financial articles, demonstrating how to preprocess text, extract keywords, and perform semantic search to find related articles.

---

## KeyBERT Overview
KeyBERT is a powerful tool for keyword extraction that works as follows:
1. **Input Text**: A document or text is provided for keyword extraction.
2. **Candidate Keywords**: KeyBERT generates candidate keywords or phrases (e.g., n-grams).
3. **BERT Embeddings**: It uses a pre-trained BERT model to generate embeddings for the document and each candidate keyword.
4. **Similarity Calculation**: Cosine similarity is computed between the document embedding and each candidate keyword embedding.
5. **Ranking**: The candidates are ranked based on similarity scores, and the top N keywords are returned.

### Advantages of KeyBERT
- **Context-Aware**: BERT embeddings capture the context of words, making KeyBERT effective for understanding nuanced meanings.
- **Simple and Flexible**: Easy to use and customizable with different BERT models or similarity metrics.
- **No Training Required**: Uses pre-trained BERT models, so no additional training is needed.

---

## Dataset
The dataset used in this project is **Lettria/financial-articles**, which contains financial articles from various sources. The dataset is loaded using the `datasets` library and preprocessed to clean the text for keyword extraction.

---

## Text Preprocessing
The text preprocessing steps include:
- Lowercasing
- Removing URLs, mentions, and hashtags
- Handling consecutive letters and special characters
- Tokenization, lemmatization, and stopword removal using **spaCy**

---

## Keyword Extraction
KeyBERT is used to extract keywords from the preprocessed text. Two approaches are demonstrated:
1. **Index Approach**: Extracts keywords from a specific article in the dataset.
2. **Semantic Search Approach**: Finds articles semantically related to a query term and extracts keywords from those articles.

---

## Semantic Search
The semantic search function uses BERT embeddings to find articles related to a specific query term. It computes the cosine similarity between the query embedding and each document embedding, ranks the articles, and extracts keywords from the top results.

---

## Results
The results include:
- Extracted keywords for specific articles.
- Visualizations of keyword distributions across articles.
- Top articles related to a query term and their keywords.
