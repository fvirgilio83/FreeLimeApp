import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Free Lime Prediction", page_icon="../img/supremo.jpg")
st.sidebar.header('What if Prediction')
st.title("FreeLime Prediction")

st.markdown("Predict FreeLime based on the following features:")

# -- Parameters -- #
Torque_Kw = st.number_input(label='Torque_Kw', min_value=50, max_value=200)
Temp_ArSec = st.number_input(label='Temp_ArSec',  min_value=750, max_value=1200)
Nox_caixa = st.number_input(label='Nox_caixa',  min_value=800, max_value=1200)
rpm = st.number_input(label='rpm',  value= 4., min_value=0.0, max_value=6.0)
Temp_C5 = st.number_input(label='Temp_C5', min_value=850, max_value=1200)
KF_LSF = st.number_input(label='KF_LSF', value=100. , min_value=90.0, max_value=120.0)
KF_MA = st.number_input(label='KF_MA', value=1.80, min_value=1.0, max_value=3.0)
KF_MS = st.number_input(label='KF_MS',value = 2.70, min_value=2.0, max_value=3.0)
KF_R90 = st.number_input(label='KF_R90',  min_value=5., max_value=15.)
Kiln_Feed = st.number_input(label='Kiln_Feed', min_value=150, max_value=300)
BZT = st.number_input(label='BZT',  min_value=800, max_value=1250)


# -- Model -- #

with open('models/modelo2.pkl', 'rb') as file:
    modelo = pickle.load(file)

def prediction():
    df_input = pd.DataFrame([{'Torque_Kw':Torque_Kw, 'Temp_ArSec':Temp_ArSec, 'Nox_caixa':Nox_caixa, 'rpm':rpm, 'Temp_C5':Temp_C5,'KF_LSF':KF_LSF,'KF_MA':KF_MA,'KF_MS':KF_MS,'KF_R90':KF_R90,'Kiln_Feed':Kiln_Feed,'BZT':BZT}])
    prediction = modelo.predict(df_input)[0]
    return prediction

# Predict
if st.button('Predict'):
    try:
        freelime = prediction()
        st.success(f'**Predicted Free Lime:** {freelime:,.2f}')
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")
