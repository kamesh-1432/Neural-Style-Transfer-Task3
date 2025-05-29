
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np

st.title("🎨 Neural Style Transfer App")

@st.cache_resource
def load_model():
    return hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

model = load_model()

# File uploaders
content_image = st.file_uploader("Upload Content Image", type=["jpg", "png"])
style_image = st.file_uploader("Upload Style Image", type=["jpg", "png"])

def preprocess(img, max_dim=512):
    img = Image.open(img).convert('RGB')
    img.thumbnail((max_dim, max_dim))
    img = np.array(img).astype(np.float32)[np.newaxis, ...] / 255.0
    return tf.convert_to_tensor(img)

def tensor_to_image(tensor):
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        tensor = tensor[0]
    return Image.fromarray(tensor)

if content_image and style_image:
    st.subheader("Uploaded Images")
    st.image(content_image, caption="Content", width=300)
    st.image(style_image, caption="Style", width=300)

    if st.button("✨ Stylize Image"):
        content = preprocess(content_image)
        style = preprocess(style_image)
        result = model(content, style)[0]
        result_image = tensor_to_image(result)

        st.subheader("Stylized Result 🎨")
        st.image(result_image, caption="Output", width=400)
