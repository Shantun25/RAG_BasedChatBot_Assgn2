# RAG System for Question Answer

** This project implements a Retrieval-Augmented Generation (RAG) system for Question Answering (QA) on a collection of research papers. The entire application is wrapped in a user-friendly Streamlit web interface. **


## ✅ Features: 

  - Document Preprocessing: Loads and chunks PDF documents from a local directory.

  - Vectorization: Uses Hugging Face's all-MiniLM-L6-v2 model to create vector embeddings of document chunks.

  - Retrieval System: Employs a Chroma vector store to quickly find the most relevant document chunks for a given query.

  - Answer Generation: Integrates the Llama3 model via the Groq API to generate accurate, context-aware answers.

  - Source Attribution: Displays the source documents and specific text chunks used to formulate the answer.



  ## 🧱 Project Structure


      /
        ├── main.py                  # Streamlit app handles multiple pdf file uploads
        ├── requirements.txt         # Not Included (Need to Install dependencies)
        ├── .env                     # Not Included (Requires Google API Key)
        ├── README.md                


  ## 📄 requirements.txt

    streamlit
    langchain
    langchain-community pymupdf
    langchain-text-splitters
    langchain-chroma
    langchain-google-genai


  ## ⚙️ Setup Instructions

  ### 1. Clone the Repository

  ### 2. Create a `.env` File

  Create a `.env` file in the root directory with the following contents:

    GOOGLE_API_KEY="your API Key"

  ### 3. Install Python Dependencies

    pip install -r requirements.txt


  ## 🚀 Running the App

    streamlit run "yourpath/main.py"


  ## ⚠️ Disclaimer

  This project is intended for educational purposes only.

---

## 🙌 Author

**SB**  

