import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    st.title("Data Visualization with Streamlit")
    
    # Upload file
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        # Check file content length
        content = uploaded_file.getvalue()
        if len(content) < 100:
            st.write("Invalid file. Please ensure the file is not empty or incomplete.")
            return
        
        # Read file
        data = read_data(uploaded_file)
        
        if data is not None:
            # Display data
            st.subheader("Data")
            st.write(data)
            
            # Data visualization options
            st.sidebar.subheader("Visualization Options")
            plot_type = st.sidebar.selectbox("Select a plot type", ["Histogram", "Box Plot", "Scatter Plot"])
            
            # Perform visualization based on selected plot type
            if plot_type == "Histogram":
                histogram(data)
            elif plot_type == "Box Plot":
                box_plot(data)
            elif plot_type == "Scatter Plot":
                scatter_plot(data)
        else:
            st.write("Invalid file format. Please upload a CSV or Excel file.")
            st.write("Uploaded file type:", uploaded_file.type)
            st.write("File contents:")
            st.write(uploaded_file.getvalue())
            st.write("File length:", len(uploaded_file.getvalue()))

def read_data(file):
    if file.type == "csv":
        try:
            data = pd.read_csv(file, delimiter=",")
        except pd.errors.ParserError:
            data = pd.read_csv(file, delimiter=";")    
    elif file.type == "xlsx":
        data = pd.read_excel(file)
    else:
        data = None
    return data

def histogram(data):
    column = st.sidebar.selectbox("Select a column", data.columns)
    plt.hist(data[column].dropna())
    st.pyplot()

def box_plot(data):
    column = st.sidebar.selectbox("Select a column", data.columns)
    sns.boxplot(data[column].dropna())
    st.pyplot()

def scatter_plot(data):
    x_column = st.sidebar.selectbox("Select X-axis column", data.columns)
    y_column = st.sidebar.selectbox("Select Y-axis column", data.columns)
    plt.scatter(data[x_column], data[y_column])
    st.pyplot()

if __name__ == "__main__":
    main()
