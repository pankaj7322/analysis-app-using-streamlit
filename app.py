import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category=DeprecationWarning)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Data Analysis")
st.sidebar.header("Visualisation Selector")
st.sidebar.text("Select the Charts/Plots accordingly:")

uploaded_file = st.file_uploader("Choose a file")
global options,cat_col, num_col
options = []
cat_col = []
num_col = []
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    columns = df.columns.tolist()
    options = columns
    cat_col = df.select_dtypes(include = ['object','category'])
    num_col = df.select_dtypes(exclude = ['object', 'category'])
    st.write(df.head())


def main(selected_option1,selected_option2, selected_option3):
    result = pd.crosstab(df[selected_option1], df[selected_option2])
    result.plot(kind=selected_option3)
    plt.plot()
    st.pyplot()


st.text('Visualisation Type')

selected_option3 = st.sidebar.selectbox("Select Plot:", ["bar","line","hist"])
selected_option1 = st.sidebar.selectbox("x",options)
selected_option2 = st.sidebar.selectbox("y",options)



submit = st.sidebar.button("Submit")
if submit:
    main(selected_option1,selected_option2, selected_option3)