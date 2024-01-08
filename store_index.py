from src.helper import load_data, text_split, download_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_data("C:\Project\Medical_chatbot_AI\Medical_ChatBot\Data")
text_chunks = text_split(extracted_data)
embeddings = download_embeddings()


#Initializing the Pinecone
pinecone.init(api_key = PINECONE_API_KEY,
              environment = PINECONE_API_ENV)


index_name="medchatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)