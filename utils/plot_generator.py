import plotly.express as px
import matplotlib as plt
import streamlit as st 

def plot_generator(x,y,plot,df):
    try: 
        if plot=='Bar Chart':
            fig= px.bar(df,x=x,y=y)
        elif plot=='Line Chart':
            fig=px.line(df,x=x,y=y)
        else:
            st.error("eoor")
            return
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"An error occurred while generating the plot: {e}")