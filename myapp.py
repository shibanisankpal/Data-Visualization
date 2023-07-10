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
            data = pd.read_excel(uploaded_file, engine='openpyxl')
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
            "Count Plot": count_plot,
            "Bar Chart": bar_chart
        }

        selected_options = []
        selected_columns = []
        for option in visualization_options.keys():
            if st.checkbox(option):
                selected_options.append(option)
                column = st.selectbox(f"Select a column for {option}", data.columns)
                selected_columns.append(column)

        if selected_options:
            for option, column in zip(selected_options, selected_columns):
                st.subheader(option)
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
    fig_count, ax_count = plt.subplots(figsize=(10, 6))
    sns.countplot(data[column])
    st.pyplot(fig_count)

def bar_chart(data, column):
    fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
    ax_bar = sns.barplot(data=data, x=data.index, y=column)
    ax_bar.set_xticklabels(ax_bar.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig_bar)

if __name__ == "__main__":
    main()
