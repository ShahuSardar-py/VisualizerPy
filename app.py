import streamlit as st
import matplotlib as plt
import plotly.express as px
import pandas as pd
from io import StringIO
from utils.dataloader import load_csv, data_cleaner
from utils.plot_generator import plot_generator

st.set_page_config(
    page_icon='📊',
    page_title='VisuvalizerPY'
    
)
st.title(":orange[VisualiserPY] 📊📈")
st.caption("A simple data visualiser that uses plotly to generate plots in just three steps from the user input CSV.")
st.subheader("How to Use:")
st.markdown('''
    - Upload Your **CSV** File
    - Select your Axes & Type of chart
    - Click On :green[**Generate Plot**]
            ''')

st.divider()
#file uploaderr
uploaded_file = st.file_uploader("**Upload your CSV to get started**", type=["csv"])


if uploaded_file:
    df,error= load_csv(uploaded_file)
    #columns
    col1,col2=st.columns(2)

    
    


    with col1:
        #displays cleaned dataframe from CSV
        with st.expander("Preview of cleaned data"):
            clean_df,error= data_cleaner(df)

            if error:
                st.error(error)
            else:
                st.dataframe(clean_df.head())
    
    #extract columns
    columns= clean_df.columns.tolist()

    #input feilds
    with col2:
        xaxis= st.selectbox("Select X-axis for the plot", options=columns)
        yaxis=st.selectbox("Select Y-axis for the plot", options=columns)

        #list of plots
        plots=["Bar Chart", "Line Chart", "Scatter Plot"]
        chart=st.selectbox("Select Plot", options=plots)

if st.button("Generate plot"):
    plot_generator(xaxis,yaxis,chart,clean_df)
