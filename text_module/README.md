# Leveraging Amazon Bedrock for Text Generation Tasks

In this module, we'll explore how to use Amazon Bedrock for three key text generation examples: Summarization, Sentiment Analysis, and Q&A. We'll learn how to invoke various foundation models like AI21 Labs, Claude, and Cohere to perform these tasks. Let's dive in!

### How to Run the Code

To execute the provided code and explore these text generation examples, open your terminal and run the following command:

```bash
python text_examples.py
```

Currently, the code for text summarization is already filled out. Your mission, should you choose to accept it, is to complete the sections for sentiment analysis and Q&A.

If you want to see the full completed code check `full_code/text_full_code.py`.

## Summarization with Amazon Bedrock

Text summarization is like the "Cliff's Notes" for machine learning. It's all about condensing long documents into shorter versions, retaining only the most important information. With the volume of text data skyrocketing, summarization can be a real timesaver, whether you're sifting through research papers, news articles, or lengthy reports.

### Code Walkthrough

The function `summarize_text(text)` calls the AI21 Labs model. It takes a lengthy text and returns a concise summary.

```python
def summarize_text(text):
    prompt = f"Summarize the following text: {text}"
    result = run_mid(prompt)
    return result
```
## Sentiment Analysis with Amazon Bedrock

Sentiment analysis is the tech version of reading the room. It gauges the mood or opinion embedded in a piece of text. Businesses use it to understand customer feedback, market trends, and social media conversations, turning qualitative data into actionable insights.

### Code Walkthrough

Right now, the function `sentiment_analysis(text)` is waiting for your touch.

```python
def sentiment_analysis(text):
    # TODO
    result = None
    return result

```

## Q&A with Amazon Bedrock

Question and Answer (Q&A) systems are like your own personal research assistant. They help you extract specific answers from a sea of information. This is incredibly useful in scenarios ranging from customer service bots to extracting insights from large datasets.

### Code Walkthrough

The function `perform_qa(question, text)` is still a template, ready for implementation.

```python
def perform_qa(question, text):
    # TODO
    result = None
    return result
```
