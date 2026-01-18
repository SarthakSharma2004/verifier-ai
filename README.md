<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3.x-green)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![GPT](https://img.shields.io/badge/Model-GPT--OSS--120B-purple)
![Tavily](https://img.shields.io/badge/Search-Tavily-red)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)
![macOS](https://img.shields.io/badge/Platform-macOS%20M1-black)

</div>



<div align="center">

# 🔍 VERIFY AI — Intelligent Fact Verification Engine

</div>


### Live Demo:

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?style=for-the-badge)](https://my-assignment-verifier-ai.streamlit.app/)


### Demo Video:

[![Demo Video](https://img.shields.io/badge/Demo%20Video-Watch-blue?style=for-the-badge)](https://drive.google.com/file/d/1tgvK5NflEvgn-XuglWhDHR5a8iP7EzyK/view?usp=sharing)



---



## 📌 OVERVIEW

Verify AI is a fact-checking web application that extracts factual claims from PDFs, verifies them using live web data, and classifies them as:


- ✅ Verified : The evidence clearly supports the claim.

- ⚠️ Inaccurate : The claim is partially correct, outdated, or has incorrect details.

- ❌ False : The evidence contradicts the claim or no reliable evidence exists.


Each claim is backed by real-time sources to ensure transparency and trust.



---



## 🚀 KEY FEATURES

- 📄 PDF Upload & Parsing
- 🧠 LLM-based Claim Extraction
- 🌐 Real-time Web Verification using Tavily
- ⚖️ Verdict Classification
- 📚 Source Citations
- 🎨 Clean Streamlit UI
- ⏳ Time-Aware Verification (Detects outdated claims using current date context)




---



## 🧱 TECH STACK

- **Frontend:** Streamlit  
- **Backend:** Python 3.13, Langchain  
- **LLM:** Groq (Model -> GPT-OSS-120B)
- **Search API:** Tavily  
- **PDF Parsing:** PyPDF  
- **Deployment:** Streamlit Cloud



---



## ⚙️ WORKING

1. The user uploads a PDF containing factual statements and claims.  

2. LLM processes the document and extracts only verifiable factual 
claims, returning them as structured JSON (claim + type).  

3. Each extracted claim is searched against the live web using the Tavily 
API.  

4. The system compares the claim with real-time web evidence using an LLM-based verifier.  

5. Every claim is classified as Verified, Inaccurate, or False, along with cited sources.  

6. The final results are displayed in a clean, interactive UI.



---



## 🛠 SETUP

#### Install Requirements

```bash
pip install -r requirements.txt
```

### Inject ENV Variables

```bash
GROQ_API_KEY=
TAVILY_API_KEY=
GOOGLE_API_KEY=
```

### RUN THE APP
```bash
streamlit run app.py
```



