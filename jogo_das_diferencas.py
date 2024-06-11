#importar
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image, ImageDraw
import time
import base64
from streamlit_modal import Modal
import random

imagem1= "Nivel6o.jpg"
original_image1 = Image.open(imagem1)
new_size = (300, 300)
resized_image = original_image1.resize(new_size)

