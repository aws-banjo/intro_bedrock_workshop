# Building LangChain Agents with Amazon Bedrock

In this module, we will focus on building an Agent using LangChain and Amazon Bedrock.

## Building with Bedrock

Now, let's dive into building the agent. We will be updating the code in the `bedrock_langchain_agent.py` using your favorite code editor.

## Creating Tools

Tools are self-contained functions designed to perform a specific task. They require the following attributes:

* **name:** a label telling the agent which tool to pick. For example, a tool named "GetCurrentWeather" tells the agent that it's for finding the current weather.
* **description:** a short instruction manual that explains when and why the agent should use the tool.
* **args_schema:** Communicates the interface of the tool for the agent. It typically draws from the wrapped function's signature and permits additional validation logic on tool inputs.
* **_run and _arun functions:** These define the tool's inner workings. It could be something simple like returning the current time or more complex like sending a message or controlling a robot.

The first tool we are building is designed to query the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). This tool leverages embeddings and vector database to deliver relevant answers to user queries.

### Embeddings

An embedding is a vector (list) of floating-point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

Use cases include:

1. **Semantic search:** Find the best matches (closest vector distances) to the query string.
2. **Classification:** Group sentences into classes, based on the relatedness of the sentence embeddings.
3. **Recommendations:** Recommend similar items based on the user-selected item. The recommended items have the highest relatedness to the input item.

Here is some sample code on how we would embed text using the Titan Embeddings Model.

```python
def get_embedding(body, modelId, accept, contentType):
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    embedding = response_body.get('embedding')
    return embedding

body = json.dumps({"inputText": "explain black holes to 8th graders"})
modelId = 'amazon.titan-embed-text-v1'
accept = 'application/json'
contentType = 'application/json'

embedding = get_embedding(body, modelId, accept, contentType)
print(embedding)
```

For the AWS Well-Architected Framework, we have already embedded the data so you can use it for this workshop. The code to generate the embeddings is in `ingest.py`

### Querying the AWS Well-Architected Framework

We will be using [Langchain](https://python.langchain.com/docs/get_started/introduction.html) a popular framework for developing applications powered by language models to help build our tool. Langchain provides an interface to use Bedrock Embeddings with a [local vector database](https://github.com/facebookresearch/faiss) to retrieve documents relevant to a user's query. Using the documents, we can then send a request to Bedrock to get a response back with relevant context. this is known as [Retrieval Augmented Generation (RAG)]( https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html).

![AWS Well-Architected Framework Tool](/static/text-gen/well_arch_tool.png)

Here is the complete code for the tool.

```python
def well_arch_tool(query: str) -> Dict[str, Any]:
    """Returns text from AWS Well-Architected Framework releated to the query"""
    embeddings = BedrockEmbeddings(
        client=bedrock_runtime,
        model_id="amazon.titan-embed-text-v1",
    )
    vectorstore = FAISS.load_local("local_index", embeddings)
    docs = vectorstore.similarity_search(query)

    resp_json = {"docs": docs}

    return resp_json
```

## Demo Tools

Now it’s your turn, to develop some of the demo tools. You will have to fill out the stubbed-out tools for `get_current_time` in `multiplier` in `bedrock_langchain_agent.py`. Remember you can CodeWhisperer to help.  

Afterwards, can you think of cool tool to build?  

The full code is located in `full_code/agent_full_code.py`

