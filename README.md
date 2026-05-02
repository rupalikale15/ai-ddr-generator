# 🛠️ AI DDR Report Generator

## 📌 Overview

This project is an AI-powered system that converts **Inspection Reports** and **Thermal Reports** into a structured **Detailed Diagnostic Report (DDR)**.

It extracts text + images, analyzes them using LLMs, and generates a **client-ready report with severity, root cause, and recommendations**.

---

## 🚀 Features

* 📄 PDF Text Extraction (Inspection + Thermal)
* 🖼️ Image Extraction from PDFs
* 🔥 Thermal Image Analysis (AI Vision)
* 🧠 Structured DDR Generation using LLM
* 📑 Automatic Word Report Generation
* ⚠️ Handles Missing Data ("Not Available")

---

## 🏗️ System Workflow

1. Upload Inspection Report (PDF)
2. Upload Thermal Report (PDF)
3. Extract:

   * Text
   * Images
4. Analyze:

   * Observations
   * Thermal anomalies
5. Generate:

   * Structured JSON DDR
   * Final Word Report (.docx)

---

## 🧠 Tech Stack

* Python
* Streamlit
* PyMuPDF
* OpenAI GPT-4o / Groq LLM
* python-docx
* Pillow

---

## 📂 Project Structure

├── app.py
├── processor.py
├── document_processor.py
├── llm_handler.py
├── report_generator.py
├── prompts.py
├── templates.py
├── requirements.txt

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---


## 📦 Output Example

* Main_DDR_Report.docx
* JSON structured output
* Images embedded in report

---

## ⚠️ Limitations

* Image-to-area mapping is basic
* Large PDFs increase processing time
* Depends on API latency

---

## 🔮 Future Improvements

* Intelligent image mapping using embeddings
* Batch processing support
* Fine-tuned domain-specific model
* Better UI/UX

---

## 📜 Assignment Compliance

✔ Uses only provided data (no hallucination)
✔ Handles missing/conflicting data
✔ Combines inspection + thermal insights
✔ Generates structured DDR format

---

## 👤 Author

Rupali Kale
