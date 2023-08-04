#import packages
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os




#reading PDF file
loader = UnstructuredPDFLoader(r"field-guide-to-data-science.pdf")
data = loader.load()

#splitting text from PDFfile
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)


#api keys
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_API_ENV = os.environ['gcp-starter']

#creating embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

#initializing pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)

index_name = 'demo'


docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)



