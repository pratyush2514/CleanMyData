import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Function to clean the data
def clean_data(df):
    # Remove null values
    df_cleaned = df.dropna()
    # Additional data cleaning operations can be added here
    return df_cleaned

# Streamlit app starts here
st.title("CleanMyData")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Try reading the CSV file
    try:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        # Display basic data summary
        st.subheader("Data Summary")
        st.write("Number of Rows:", df.shape[0])
        st.write("Number of Columns:", df.shape[1])
        st.write("Data Types:", df.dtypes)
        st.write("Unique Values:")
        for column in df.columns:
            st.write(f"- {column}: {df[column].nunique()}")

        # Data cleaning
        if st.button("Clean Data"):
            cleaned_df = clean_data(df)
            st.write("Data cleaned successfully.")
            st.write(cleaned_df)

            # Generate a bar chart
            st.subheader("Bar Chart")
            column_name = st.selectbox("Select a column for visualization", df.columns)
            chart_data = cleaned_df[column_name].value_counts().reset_index()
            chart_data.columns = ['Value', 'Count']

            # Create the bar chart using Seaborn
            fig, ax = plt.subplots(figsize=(15, 8))
            sns.barplot(x="Value", y="Count", data=chart_data, ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
        st.write("Unable to load data.")

else:
    st.warning("Please upload a CSV file.")
