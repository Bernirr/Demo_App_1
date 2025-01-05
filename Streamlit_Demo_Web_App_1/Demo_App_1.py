#https://numberslider.streamlit.app/

#Here’s a basic example of a Streamlit app:
#This code creates an interactive app where users can input their name,
#use a slider, and see a dynamically updated plot.

import streamlit as st

# Title and text
st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

# Input widget
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Slider and chart
slider_value = st.slider("Pick a number", 0, 100)
st.write(f"You picked {slider_value}")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x) * slider_value
plt.plot(x, y)
st.pyplot(plt)
