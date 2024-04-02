import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=DeprecationWarning)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Data Analysis")
uploaded_file = st.file_uploader("Choose a file")
st.sidebar.header('Section 1')
st.sidebar.write('This is the first section in the sidebar.')
global options
options = []
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    columns = df.columns.tolist()
    options = columns
    st.write(df.head())


def main(selected_option1,selected_option2, selected_option3):
    result = pd.crosstab(df[selected_option1], df[selected_option2])
    result.plot(kind=selected_option3)
    plt.plot()
    st.pyplot()


st.text('Data Visualisation')
selected_option1 = st.sidebar.selectbox("x",options)
selected_option2 = st.sidebar.selectbox("y",options)
selected_option3 = st.sidebar.selectbox("Select Plot", ["bar","scatter","hist"])
submit = st.sidebar.button("Submit")

if submit:
    main(selected_option1,selected_option2, selected_option3)