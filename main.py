import streamlit as st
import tempfile
from langchain.chat_models import init_chat_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA


import os
import getpass
from dotenv import load_dotenv



def load_document(uploaded_file):

    '''This method will upload pdf files'''
    all_docs = []
    for file in uploaded_file:
        suffix = file.name.split('.')[-1].lower()

        if suffix == "pdf":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.getbuffer())
                tmp_path = tmp.name
            loader = PyMuPDFLoader(tmp_path)
            all_docs.extend(loader.load_and_split())


    return all_docs
   

def main():
    st.title("📚 Load PDF File and Ask")

    # Load environment variables
    load_dotenv()

    # Check for Google API Key
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please create a .env file and add it.")


    # upload multiple pdf files
    uploaded_file = st.file_uploader("Upload your file (PDF)", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_file:
        # Loading
        docs = load_document(uploaded_file)
        st.success("Document loaded successfully!")

        # model selection
        llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

        # Embed and store vectors
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = Chroma(collection_name="uplds",
                            embedding_function=embeddings,
                            persist_directory="./App2/upload2",  # Where to save data locally, remove if not necessary
                                            )

        #Retrieval
        vector_store = Chroma.from_documents(docs, embedding=embeddings)
        retriever = vector_store.as_retriever()

        
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff"
        )

        user_question = st.text_input("Ask a question about the uploaded file:")
        if user_question:
            answer = qa.run(user_question)
            st.markdown("### 💬 Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
