# Sentiment Analysis using BERT

## Overview
This project focuses on performing **Sentiment Analysis** using the **BERT (Bidirectional Encoder Representations from Transformers)** model. The goal is to classify tweets into two sentiment categories: **Positive** or **Negative**. The project leverages the `bert-base-uncased` model from the Hugging Face Transformers library and fine-tunes it on the **Sentiment140 dataset**, which contains 1.6 million labeled tweets.

The project includes:
- Data preprocessing and cleaning.
- Fine-tuning the BERT model for binary sentiment classification.
- Evaluation of the model using accuracy, loss, and a confusion matrix.
- Inference on custom sentences to predict sentiment.

---

## Table of Contents
1. [Dataset](#dataset)
2. [Preprocessing](#preprocessing)
3. [Model Training](#model-training)
4. [Evaluation](#evaluation)
5. [Results](#results)


---

## Dataset
The dataset used is the **Sentiment140 dataset**, which contains 1.6 million tweets labeled as either **Positive (1)** or **Negative (0)**. The dataset is available on Kaggle:
- [Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

The dataset is preprocessed to:
- Balance the number of positive and negative samples.
- Clean tweets by removing URLs, mentions, hashtags, and special characters.
- Filter out tweets with fewer than 5 words.

---

## Preprocessing
The preprocessing steps include:
1. **Cleaning Tweets**:
   - Remove URLs, mentions, and hashtags.
   - Replace emojis and special characters.
   - Convert text to lowercase.
   - Remove non-ASCII characters.
2. **Tokenization**:
   - Use the `bert-base-uncased` tokenizer to convert text into input IDs and attention masks.
3. **Dataset Splitting**:
   - Split the dataset into training (90%), validation (7%), and test (3%) sets.

---

## Model Training
The `bert-base-uncased` model is fine-tuned for binary sentiment classification. Key details:
- **Optimizer**: AdamW with a learning rate of `2e-5`.
- **Batch Size**: 128.
- **Epochs**: 3.
- **Learning Rate Scheduler**: Linear scheduler with warmup.

The model is trained on a GPU (if available) and saved after each epoch if the validation loss improves.

---

## Evaluation
The model is evaluated on the test set using:
- **Accuracy**: The percentage of correctly classified tweets.
- **Confusion Matrix**: Visualizes true vs. predicted labels.
- **Classification Report**: Provides precision, recall, and F1-score for each class.
---
### Results
- **Test Accuracy**: ~92%
- **Confusion Matrix**:
  ![img](https://i.imgur.com/4sezgwL.png)





```python
test_sentences = [
    "I hate the selfishness in you",
    "The movie was fantastic!"
]

results = process_and_predict_sentences(test_sentences, model, tokenizer)
for result in results:
    print(result)
```

Output:
```
{'Sentence': 'I hate the selfishness in you', 'label': 'negative'}
{'Sentence': 'The movie was fantastic!', 'label': 'positive'}
```
---
- The fine-tuned BERT model achieves **92% accuracy** on the test set.
- The model performs well on both positive and negative sentiment classification, as shown in the confusion matrix and classification report.
