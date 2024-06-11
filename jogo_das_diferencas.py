#importar
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image, ImageDraw
import time
import base64
from streamlit_modal import Modal
import random

# Function to get base64 of image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_background(image):
    bin_str = get_base64_of_bin_file(image)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('data:image/png;base64,%s');
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set background image
background_image_path = "fundo.png"
set_background(background_image_path)

