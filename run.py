from main import docsearch, OPENAI_API_KEY
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")


while True:
    query = input("Question: ")
    docs = docsearch.similarity_search(query, include_metadata=True)
    answer = chain.run(input_documents=docs, question=query)
    print(f"Answer: {answer}")