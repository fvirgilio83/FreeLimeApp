import streamlit as st

st.set_page_config(
    page_title="Predição de Cal livre",
    page_icon="img/supremo.jpg",
)

st.sidebar.header('Project Description')

st.write("# Welcome to the FreeLime Prediction App ")
st.write("\n\n")

st.image('img/forno.jpg')
st.write("\n\n")

st.markdown(
    """
    Cal livre é definido como o cálcio presente no clínquer, apresentado na forma de óxido de cálcio (CaO). No processo de clinquerização pode ser usado como
    um indicador na operação do forno mostrando se há necessidade de mais calor dentro do forno ou se é possível diminuir o consumo de combustível no queimador
    principal gerando economia com consumo térmico menor. O target de cal livre varia de acordo com cada planta, sendo 1.8 um valor referência.
    O principal objetivo deste aplicativo é gerar insights em uma maior frequência para tomada de ações mais rápidas no forno, visto que o resultado do laboratório
    é gerado a cada 2horas. 

    Este App objetiva predizir o resultado de cal livre usando as seguintes features:
    'Torque_Kw', 'Temp_ArSec', 'Nox_caixa', 'rpm', 'Temp_C5', 'KF_LSF', 'KF_MA', 'KF_MS', 'KF_R90', 'Kiln_Feed', 'BZT'
    
    """
)

st.success('Please **go to the next pages** to get the predictions.')
st.sidebar.markdown("Desenvolvido por ***Fernando Virgilio***")
