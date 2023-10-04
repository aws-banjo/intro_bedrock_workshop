import boto3
import json

# Setup bedrock
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)


# Call AI21 labs model
def run_mid(prompt):
    prompt_config = {
        "prompt": prompt,
        "maxTokens": 5147,
        "temperature": 0.7,
        "stopSequences": [],
    }

    body = json.dumps(prompt_config)

    modelId = "ai21.j2-mid"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("completions")[0].get("data").get("text")
    return results


def claude_prompt_format(prompt: str) -> str:
    # Add headers to start and end of prompt
    return "\n\nHuman: " + prompt + "\n\nAssistant:"


# Call Claude model
def call_claude(prompt):
    prompt_config = {
        "prompt": claude_prompt_format(prompt),
        "max_tokens_to_sample": 4096,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": [],
    }

    body = json.dumps(prompt_config)

    modelId = "anthropic.claude-v2"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("completion")
    return results


# Call Cohere model
def call_cohere(prompt):
    prompt_config = {
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0.7,
    }

    body = json.dumps(prompt_config)

    modelId = "cohere.command-text-v14"
    accept = "application/json"
    contentType = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())

    results = response_body.get("generations")[0].get("text")
    return results


def summarize_text(text):
    """
    Function to summarize text using a generative AI model.
    """
    prompt = f"Summarize the following text: {text}"
    result = run_mid(prompt)
    return result


def sentiment_analysis(text):
    """
    Function to return a JSON object of sentiment from a given text.
    """
    # TODO
    # Can you write a prompt to help answer these questions?
    result = None
    return result


def perform_qa(question, text):
    """
    Function to perform a Q&A operation based on the provided text.
    """
    # TODO
    # Can you write a prompt to help answer these questions?

    result = None
    return result


if __name__ == "__main__":
    # Sample text for summarization
    text = "This April, we announced Amazon Bedrock as part of a set of new tools for building with generative AI on AWS. Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies, including AI21 Labs, Anthropic, Cohere, Stability AI, and Amazon, along with a broad set of capabilities to build generative AI applications, simplifying the development while maintaining privacy and security Today, I'm happy to announce that Amazon Bedrock is now generally available! I'm also excited to share that Meta's Llama 2 13B and 70B parameter models will soon be available on Amazon Bedrock."

    print("\n=== Summarization Example ===")
    summary = summarize_text(text)
    print(f"Summary: {summary}")

    print("\n=== Sentiment Analysis Example ===")
    sentiment_analysis_json = sentiment_analysis(text)
    print(f"Sentiment_Analysis JSON:\n{sentiment_analysis_json}")

    print("\n=== Q&A Example ===")

    q1 = "How many models does Amazon Bedrock support?"
    print(q1)
    answer = perform_qa(q1, text)
    print(f"Answer: {answer}")

    q2 = "What models are coming soon to Amazon Bedrock?"
    print(q2)
    answer = perform_qa(q2, text)
    print(f"Answer: {answer}")

    q3 = "When was Amzozn Bedrock announced?"
    print(q3)
    answer = perform_qa(q3, text)
    print(f"Answer: {answer}")
