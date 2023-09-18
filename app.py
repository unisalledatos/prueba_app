import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Titulo de la app")

X = np.random.normal(0, 1, 1000)

fig, ax = plt.subplots(1, 1)
ax.hist(X, bins=50)

st.pyplot(fig)

st.header("Un nuevo cambio")