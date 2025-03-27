import gradio as gr
from datetime import datetime

# Function to generate the report
def generate_report(lining_thickness):
    if lining_thickness < 7 or lining_thickness > 14:
        probability_score = 56  # Medium probability
        category = "Medium Probability"
        color = "orange"
        report = (
            f"The embryo image analysis with a uterine lining thickness of {lining_thickness}mm "
            "indicates a moderately favorable environment for implantation. The uterine lining thickness "
            "is within acceptable range, which may affect implantation success. The embryo shows adequate "
            "developmental progression."
        )
    else:
        probability_score = 85  # High probability
        category = "High Probability"
        color = "green"
        report = (
            f"The embryo image analysis with a uterine lining thickness of {lining_thickness}mm "
            "indicates a highly favorable environment for implantation. The uterine lining thickness "
            "is optimal, which increases the likelihood of implantation success. The embryo shows excellent "
            "developmental progression."
        )

    # Ensure the day is set to 5
    day = 5
    analysis_date = datetime(2025, 3, day).strftime("%m/%d/%Y")

    # Generate HTML for the color-coded circle with the probability score
    circle_html = f"""
    <div style="display: flex; align-items: center; justify-content: center; height: 150px;">
        <div style="width: 120px; height: 120px; border-radius: 50%; background-color: {color}; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; color: white;">
            {probability_score}%
        </div>
    </div>
    """

    return (
        circle_html,
        report,
        f"{probability_score}%",
        category,
        f"{lining_thickness} mm",
        analysis_date,
        "7–14 mm",
        "EmbryoML v1.0",
    )

# Gradio interface
with gr.Blocks(css=".container { max-width: 100%; margin: auto; }") as interface:
    gr.Markdown("# EmbryoML", elem_id="title")
    
    with gr.Row(elem_id="main-row"):
        with gr.Column(scale=4, elem_id="image-column"):
            gr.Image("test.png", label="Embryo Image", elem_id="embryo-image")  # Placeholder image
            lining_input = gr.Slider(5, 20, step=0.1, label="Lining Thickness (mm)", elem_id="lining-input")
            submit_button = gr.Button("Generate Report", elem_id="submit-button")
        with gr.Column(scale=3, elem_id="text-column"):
            gr.Markdown("### Generated Report", elem_id="report-title")
            circle_output = gr.HTML(label="Probability Indicator", elem_id="circle-output")
            with gr.Row():
                category_output = gr.Textbox(label="Category", interactive=False, elem_id="category-output")
                probability_output = gr.Textbox(label="Probability Score", interactive=False, elem_id="probability-output")
                thickness_output = gr.Textbox(label="Lining Thickness", interactive=False, elem_id="thickness-output")
            with gr.Row():
                date_output = gr.Textbox(label="Analysis Date", interactive=False, elem_id="date-output")
                range_output = gr.Textbox(label="Optimal Range", interactive=False, elem_id="range-output")
                version_output = gr.Textbox(label="Version", interactive=False, elem_id="version-output")
            # Add a scrollable textbox for the long explanation
            report_output = gr.Textbox(
                label="Generated Report",
                interactive=False,
                elem_id="report-output",
                lines=5,  # Fixed height
                max_lines=5,  # Scrollable if content exceeds
            )
    
    submit_button.click(
        generate_report,
        inputs=[lining_input],
        outputs=[
            circle_output,
            report_output,
            probability_output,
            category_output,
            thickness_output,
            date_output,
            range_output,
            version_output,
        ],
    )

# Add custom CSS for styling
interface.css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.container {
    font-family: 'Poppins', Arial, sans-serif;
    background-color: #1e1e2f;
    color: #ffffff;
    overflow: hidden;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
}

#title {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    color: #ffcc00;
}

#main-row {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: space-between;
    margin-top: 20px;
}

#image-column {
    text-align: center;
    flex: 1;
}

#embryo-image {
    width: 100%;
    max-height: 400px;
    object-fit: contain;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}

#text-column {
    padding-left: 20px;
    flex: 1;
}

#report-title {
    font-size: 1.8rem;
    font-weight: bold;
    margin-bottom: 10px;
    color: #ffcc00;
}

#circle-output {
    margin-top: 20px;
}

#report-output {
    font-size: 1rem;
    margin-bottom: 10px;
    background-color: #2e2e3f;
    border: none;
    color: #ffffff;
    padding: 10px;
    border-radius: 5px;
    overflow-y: auto; /* Scrollable content */
}

#lining-input {
    margin-top: 20px;
}

#submit-button {
    font-size: 1rem;
    font-weight: bold;
    margin-top: 20px;
    background-color: #4a4a4a;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

#submit-button:hover {
    background-color: #6a6a6a;
}
"""

interface.launch()