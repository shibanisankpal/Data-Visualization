import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Custom Dataset Dashboard")

    # Load and explore the dataset
    uploaded_file = st.file_uploader("Upload a CSV or Excel file")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("Data")
        st.write(data)

        # Create visualizations
        st.subheader("Data Visualizations")

        visualization_options = {
            "Histogram": histogram,
            "Pie Chart": pie_chart,
            "Scatter Plot": scatter_plot,
            "Count Plot": count_plot
        }

        selected_options = []
        for option in visualization_options.keys():
            if st.checkbox(option):
                selected_options.append(option)

        if selected_options:
            for option in selected_options:
                st.subheader(option)
                visualization_options[option](data)

def histogram(data):
    column_hist = st.selectbox("Select a column for histogram", data.columns)
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(data[column_hist].dropna())
    st.pyplot(fig_hist)

def pie_chart(data):
    column_pie = st.selectbox("Select a column for pie chart", data.columns)
    counts = data[column_pie].value_counts()
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(counts, labels=counts.index, autopct='%1.1f%%')
    ax_pie.set_aspect('equal')
    st.pyplot(fig_pie)

def scatter_plot(data):
    column_x = st.selectbox("Select X-axis column", data.columns)
    column_y = st.selectbox("Select Y-axis column", data.columns)
    fig_scatter, ax_scatter = plt.subplots(figsize=(8, 6))
    ax_scatter.scatter(data[column_x], data[column_y])
    ax_scatter.set_xlabel(column_x)
    ax_scatter.set_ylabel(column_y)
    st.pyplot(fig_scatter)


def count_plot(data):
    column_count = st.selectbox("Select a column for count plot", data.columns)
    fig_count, ax_count = plt.subplots(figsize=(10, 6))
    sns.countplot(data[column_count])
    st.pyplot(fig_count)


if __name__ == "__main__":
    main()