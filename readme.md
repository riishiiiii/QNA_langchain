# Fine-Tuning LLM Model Project

This project aims to fine-tune a large language model (LLM) using OpenAI's technology and Pinecone as vector database. The fine-tuned model can answer to the questions from the PDF formated book which is used to fine tune the Model

### Installation
To install the required dependencies, navigate to the project directory in your terminal and run the following command:

`pip install -r requirements.txt`

### Usage

Before running the project, you need to provide your OpenAI API key and Pinecone API key. Follow these steps:

1. OpenAI API Key: Obtain your API key from the OpenAI website. Once you have the key, set it as an environment variable named OPENAI_API_KEY.

`export OPENAI_API_KEY="your_openai_api_key_here"`

2. Pinecone API Key: Sign up for Pinecone and obtain your API key from the Pinecone dashboard. Set it as an environment variable named PINECONE_API_KEY.

`export PINECONE_API_KEY="your_pinecone_api_key_here"`

Once you've set the API keys, you can run the project using the following command:

`python run.py`

This command will execute the script run.py, which contains the code for fine-tuning the LLM model.

### Requirements
Make sure you have Python installed on your system. The project dependencies are listed in the requirements.txt file.