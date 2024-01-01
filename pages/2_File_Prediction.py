import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Free Lime Prediction", page_icon="../img/supremo.jpg")
st.sidebar.header('File Prediction')
st.title("Free Lime prediction")

st.markdown("Predict Clinker Free Lime using a excel file:")
st.markdown("Features names must be equals as described on Project Description page")

# -- Model -- #
with open('models/modelo2.pkl', 'rb') as file:
    modelo = pickle.load(file)

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_excel(data)
    freelime_prediction = modelo.predict(df_input)
    df_output = df_input.assign(prediction=freelime_prediction)

    st.markdown('Free Lime prediction:')
    st.write(df_output)
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='predicted_freelime.csv'
        )

    if "data" not in st.session_state:
        st.session_state["data"]=df_output