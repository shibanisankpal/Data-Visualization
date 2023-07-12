import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Custom Dataset Dashboard")

    # Load and explore the dataset
    uploaded_file = st.file_uploader("Upload a CSV or Excel file")
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            data = pd.read_csv(uploaded_file, encoding='utf-8')
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            try:
                data = pd.read_excel(uploaded_file)
            except Exception as e:
                st.write("Error reading Excel file:", str(e))
                return
        else:
            st.write("Invalid file format. Please upload a CSV or Excel file.")
            return

        st.subheader("Data")
        st.write(data)

        # Create visualizations
        st.subheader("Data Visualizations")

        visualization_options = {
            "Histogram": histogram,
            "Pie Chart": pie_chart,
            "Count Plot": count_plot
        }

        for option in visualization_options.keys():
            num_visualizations = st.number_input(f"Number of {option}s", min_value=1, value=1, step=1)
            if num_visualizations > 0:
                for i in range(num_visualizations):
                    st.subheader(f"{option} {i+1}")
                    column = st.selectbox(f"Select a column for {option} {i+1}", data.columns)
                    visualization_options[option](data, column)

def histogram(data, column):
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(data[column].dropna())
    st.pyplot(fig_hist)

def pie_chart(data, column):
    fig_pie, ax_pie = plt.subplots()
    data[column].value_counts().plot.pie(autopct='%1.1f%%')
    ax_pie.set_ylabel("")
    st.pyplot(fig_pie)

def count_plot(data, column):
    fig_count, ax_count = plt.subplots()
    sns.countplot(data[column])
    st.pyplot(fig_count)

if __name__ == "__main__":
    main()

