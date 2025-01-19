import streamlit as st
import pandas as pd
import json

# Streamlit App
st.title("CSV to JSON Transformer")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Load the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    
    # Process the CSV data into JSON format
    output = []  
    for _, row in data.iterrows():
        transformed_rec = {
            "title": row["title"],
            "subCategory": [],  # Static empty list
            "recommendation_content": row["recommendation_content"],
            "guide_title": row["guide_title"],
            "rating": row["rating"],
            "stage": [" "],  # Static list containing a single space
            "disease": [" "],  # Static list containing a single space
            "rationales": [],  # Static empty list
            "references": [],  # Static empty list
            "specialty": row["specialty"].split(", "),  # Split specialties by commas into a list
            "recommendation_class": row["recommendation_class"]
        }
        output.append(transformed_rec)

    # Convert output to JSON format
    json_data = json.dumps(output, indent=2)
    
    # Allow the user to download the JSON file
    st.download_button(
        label="Download JSON file",
        data=json_data,
        file_name="recommendations_output.json",
        mime="application/json"
    )

    # Preview JSON data in the app
    st.subheader("Preview of the Transformed JSON")
    st.json(json_data)

