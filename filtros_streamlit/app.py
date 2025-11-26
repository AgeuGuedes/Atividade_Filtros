import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("Filtros de Imagem")

uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.subheader("Imagem original")
    st.image(img, use_container_width=True)

    filtro = st.selectbox(
        "Escolha um filtro",
        [
            "Original",
            "Preto e branco",
            "Desfoque Gaussiano",
            "Blur de média",
            "Tom verde",
            "Tom vermelho",
            "Contraste alto"
        ]
    )

    if filtro == "Preto e branco":
        img_proc = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    elif filtro == "Desfoque Gaussiano":
        img_proc = cv2.GaussianBlur(img, (15, 15), 0)

    elif filtro == "Blur de média":
        img_proc = cv2.blur(img, (15, 15))

    elif filtro == "Tom verde":
        img_proc = img.copy()
        img_proc[:, :, 0] = 0  
        img_proc[:, :, 2] = 0  

    elif filtro == "Tom vermelho":
        img_proc = img.copy()
        img_proc[:, :, 1] = 0  
        img_proc[:, :, 2] = 0  

    elif filtro == "Contraste alto":
        img_proc = cv2.convertScaleAbs(img, alpha=1.8, beta=10)

    else:
        img_proc = img

    st.subheader("Imagem com filtro")
    st.image(img_proc, use_container_width=True)

else:
    st.write("Envie uma imagem para começar.")