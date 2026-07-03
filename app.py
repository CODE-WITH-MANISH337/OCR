import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

st.set_page_config(page_title="Handwriting OCR", page_icon="✍️", layout="centered")

MODEL_NAME = "CODE-WITH-MANISH337/trocr-iam-handwriting"

@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained(MODEL_NAME)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
    model.eval()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return processor, model, device

processor, model, device = load_model()

st.title("✍️ Handwriting OCR")
st.caption("TrOCR fine-tuned with LoRA on the IAM handwriting dataset")

uploaded_file = st.file_uploader("Upload an image of handwritten text", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Recognize Text", type="primary"):
        with st.spinner("Recognizing..."):
            pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)
            with torch.no_grad():
                generated_ids = model.generate(pixel_values, max_length=128)
            text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        st.subheader("Recognized Text")
        st.success(text)
        st.text_area("Copy text", text, height=100)
else:
    st.info("Upload a handwriting image to get started.")