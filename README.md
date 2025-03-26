# 📝 Web Content Q&A Tool  

A web-based tool that allows users to input one or more URLs, extract their content, and ask questions based strictly on that content. No external knowledge is used, ensuring responses are relevant to the provided sources.  

---

## ✨ Features  
✅ Extracts text from web pages 📄  
✅ Allows users to input multiple URLs 🔗  
✅ Enables querying based only on extracted content 🤖  
✅ Summarizes large text before querying to avoid token limits 📊  
✅ Simple UI with fields for URLs, queries, and answers 🎨  

---

## 🚀 Demo  

---

## 🛠️ Setup & Installation  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/your-username/site-summarizer.git
cd site-summarizer
```

## Create Virtual environmet
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Set Up Environment Variables
Create a .env file in the root directory and add your Groq API Key:
```
GROQ_API_KEY=your-api-key-here

```

## Run the Application
```
python app.py
```
