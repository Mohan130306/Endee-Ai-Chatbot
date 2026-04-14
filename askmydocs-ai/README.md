# 

https://github.com/user-attachments/assets/994e1844-17a0-417a-9891-0674ba491406

 AskMyDocs AI – RAG-based Document Chatbot using Endee

##  Overview

AskMyDocs AI is an AI-powered document question-answering system that allows users to input text documents and ask questions based on their content.
The system uses **vector embeddings** and **semantic search** powered by the **Endee Vector Database** to retrieve relevant information and generate responses.

This project demonstrates a practical implementation of **Retrieval-Augmented Generation (RAG)** using modern AI infrastructure.

---

##  Features

*  Input and store documents
*  Semantic search using vector embeddings
*  Question answering based on document context
*  Fast retrieval using vector similarity
*  Simple and interactive UI using Streamlit

---

##  How It Works (RAG Pipeline)

1. **Document Input**

   * User provides document text

2. **Embedding Generation**

   * Text is converted into vector embeddings using Sentence Transformers

3. **Vector Storage (Endee)**

   * Embeddings are stored in the Endee vector database

4. **Query Processing**

   * User query is converted into embedding

5. **Semantic Search**

   * Similar vectors are retrieved from Endee

6. **Response Generation**

   * Relevant context is returned as the answer

---

##  Project Structure

```
askmydocs-ai/
│
├── app.py               # Streamlit UI
├── embedder.py          # Embedding generation
├── vector_store.py      # Vector storage & retrieval
├── rag_pipeline.py      # RAG logic
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## Tech Stack

* Python 
* Streamlit (UI)
* Sentence Transformers (Embeddings)
* Endee (Vector Database)
* Scikit-learn (Similarity search)

---

##  How to Run

### 1️⃣ Clone the Repository

```
git clone <your-forked-repo-link>
cd endee/askmydocs-ai
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
streamlit run app.py
```

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---

##  Demo

* Enter document text
* Click **"Store Document"**
* Ask a question related to the document
* Get AI-generated answers

(Add screenshot here)

---

## Example

**Input Document:**

```
Filter design is a process used in signal processing...
```

**Query:**

```
What is filter design?
```

**Output:**

```
Based on documents: Filter design is a process...
```

---

##  Use of Endee

This project utilizes **Endee Vector Database** to:

* Store high-dimensional embeddings of documents
* Perform efficient similarity search
* Retrieve context for RAG-based responses

Endee enables fast and scalable semantic search capabilities for AI applications.

---

##  Future Improvements

* Integration with LLMs (OpenAI / Gemini)
* PDF & file upload support
* Conversational memory
* Deployment on cloud (Streamlit Cloud / Render)

---

## 👨‍💻 Author

* Mohan Kumar A

---

##  License

This project is developed as part of the Endee Internship Evaluation.
