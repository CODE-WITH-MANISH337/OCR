# ✍️ Handwriting OCR (TrOCR + Streamlit)

Turn handwritten text images into digital text using a **TrOCR** handwriting model, delivered through a lightweight **Streamlit** app.

## 🌐 Live Demo
https://nljyjyfk79ca8utujkeepj.streamlit.app/

[MIT License](LICENSE)

---

## ✨ Features
- Upload handwritten images (`.png`, `.jpg`, `.jpeg`)
- Runs inference locally using **PyTorch** (CPU or GPU if available)
- Displays:
  - the uploaded image
  - the **recognized text**
  - a copyable text area

---

## 🔧 Tech Stack
- **Streamlit** (UI)
- **Transformers** (TrOCR processor + model)
- **PyTorch** (inference)
- **Pillow** (image loading)

---

## 🧠 Model
This app uses:
- `TrOCRProcessor`
- `VisionEncoderDecoderModel`

Model loaded from:
- `CODE-WITH-MANISH337/trocr-iam-handwriting`

> The app caption notes it is **TrOCR fine-tuned with LoRA on the IAM handwriting dataset**.

---

## 🚀 Run Locally

### 1) Install dependencies
```bash
pip install -r requirements.txt
```

### 2) Start the Streamlit app
```bash
streamlit run app.py
```

### 3) Use the app
1. Upload an image of handwritten text
2. Click **Recognize Text**
3. Copy the recognized output from the text box

---

## ✅ Usage Notes / Tips
- Use clear, well-lit images with readable handwriting
- If possible, crop to the text region (reduces background noise)
- For best results:
  - keep the text relatively large in the image
  - avoid heavy blur or extreme angles

---

## ⚠️ Limitations
- Recognition quality depends heavily on image clarity and formatting
- Inference currently uses a fixed generation limit:
  - `max_length=128`
- Performance varies by hardware (CPU vs CUDA-enabled GPU)

---

## 🧾 Requirements
- streamlit
- transformers
- torch
- pillow

---

## 📝 License
MIT (see [LICENSE](LICENSE)).
