import streamlit as st
import pandas as pd
import re
import os

st.info("This page will be updated every 5 minutes based on the latest data from the CSV file. The data will be null at every 5-minute interval. Please refresh the page to avoid this.")

# Title
st.title("SSV_MS_TEST_NODE_REPORT.CSV")

# Load CSV directly from a path
csv_path = " Raw data file path fro .csv format likr "test_nodes_report.csv""  # Update this if needed

try:
    df = pd.read_csv(csv_path)

    # Drop columns that are completely empty
    df = df.dropna(axis=1, how='all')

    # Show dataframe
    st.subheader("Data Preview")
    st.dataframe(df)

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Plotting
    st.subheader("Column-wise Histogram")

    # Filter columns with at least some non-null values
    valid_columns = [col for col in df.columns if df[col].notnull().any()]

    if valid_columns:
        column = st.selectbox("Select column to plot", valid_columns)
        cleaned_data = df[column].dropna()
        if not cleaned_data.empty:
            st.bar_chart(cleaned_data.value_counts())
        else:
            st.warning("Selected column has no valid data to plot.")
    else:
        st.warning("No valid columns available for plotting.")

except FileNotFoundError:
    st.error(f"CSV file not found at: {csv_path}")


# Set the path to your log file
log_file_path = "error log path"

st.title("Failed systems Error messages and exceptions")

# Check if the file exists
if os.path.exists(log_file_path):
    with open(log_file_path, "r") as file:
        log_content = file.read()
        st.text_area("Log Viewer", log_content, height=500)
    # Display the raw log content
    
        # with st.expander("View Full Log"):
        
        #     st.code(log_content, language="text")

    # st.code(log_content, language="vscode")
    # st.markdown(log_content)
    # st.line_chart(log_content)
    # st.c(log_content)
    # st.bar_chart(log_content, *)
else:
    st.error(f"Log file not found at: {log_file_path}")

##fun
# wordcloud = WordCloud(width=800, height=400).generate(log_content)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# st.pyplot(plt)
