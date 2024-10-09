import gradio as gr
import pandas as pd
import json

# Function to convert dataframe input to JSON format
def generate_rubric_json(df):
    rubric = {"criteria": []}
    for _, row in df.iterrows():
        criterion_data = {
            "criterion": row["Criterion"],
            "description": row["Description"],
            "levels": {
                "NOT EVIDENT": row["NOT EVIDENT"],
                "EMERGING": row["EMERGING"],
                "DEVELOPING": row["DEVELOPING"],
                "PROFICIENT": row["PROFICIENT"],
                "EXEMPLARY": row["EXEMPLARY"]
            }
        }
        rubric["criteria"].append(criterion_data)
    
    return json.dumps(rubric, indent=4)

# Set up initial data for Dataframe component
initial_data = {
    "Criterion": ["Introduction of Thesis with Research", "Critical Analysis", "Summarize the Paper", "Writing Mechanics", "Sources", "APA Formatting"],
    "Description": ["Thesis is well developed with detailed research and information.", 
                    "Highlights three or more learning theories, including UDL.",
                    "Summary written and well organized with details supporting the paper.",
                    "Minimal spelling, grammar, and/or punctuation errors present.",
                    "Consistent use of sources to support statements throughout the paper.",
                    "Citations, references, and formatting follow APA style guide."],
    "NOT EVIDENT": ["" for _ in range(6)],
    "EMERGING": ["" for _ in range(6)],
    "DEVELOPING": ["" for _ in range(6)],
    "PROFICIENT": ["" for _ in range(6)],
    "EXEMPLARY": ["" for _ in range(6)],
}

# Convert initial data to DataFrame
initial_df = pd.DataFrame(initial_data)

# Define Gradio interface
iface = gr.Interface(
    fn=generate_rubric_json,
    inputs=gr.Dataframe(
        headers=["Criterion", "Description", "NOT EVIDENT", "EMERGING", "DEVELOPING", "PROFICIENT", "EXEMPLARY"],
        value=initial_df,
        datatype="str",
        row_count=(6, "dynamic"),
        col_count=(7, "fixed")
    ),
    outputs="text",
    title="Dynamic Rubric to JSON Converter",
    description="Enter the rubric criteria, descriptions, and levels in the table below to generate a JSON representation."
)

# Launch the interface
iface.launch()
