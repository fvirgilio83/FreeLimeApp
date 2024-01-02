import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.set_page_config(page_title="Free Lime Prediction", page_icon="../img/grafico.jpg")
st.sidebar.header('Trends')
st.title("FreeLime Prediction x FreeLime Real")


st.markdown("First add your file on File Prediction page to trend the results")
st.markdown("Trend based on the last 20 values:")


grafico =st.session_state["data"] 

c= [i for i in range(1,21,1)]
fig, ax =plt.subplots(figsize=(10,8), layout='constrained')


x1= grafico.iloc[grafico.shape[0]-20:grafico.shape[0]+1,-2]
x2 = grafico.iloc[grafico.shape[0]-20:grafico.shape[0]+1,-1]


ax.scatter(c,x1,facecolor = 'C1', edgecolor= 'k', label='FreeLime_Real')
ax.plot(c, x2, 'o--', label='FreeLime_Predicted')
ax.set_ylabel(' Free Lime ')
ax.set_xlabel(' Last 20 results ')
ax.legend()


st.pyplot(fig)
