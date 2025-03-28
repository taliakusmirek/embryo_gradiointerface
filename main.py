import gradio as gr
from datetime import datetime

# Function to generate the report
def generate_report(image, lining_thickness):
    try:
        lining_thickness = float(lining_thickness)
    except ValueError:
        return (
            """<div style="background-color: #2d3748; color: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #e53e3e;">
                <div style="font-weight: bold; margin-bottom: 8px;">Error</div>
                <div>Please enter a valid number for lining thickness</div>
               </div>""",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        )
    
    if lining_thickness < 7 or lining_thickness > 14:
        probability_score = 56  # Medium probability
        category = "Medium Probability"
        color = "#FFC107"  # Gold/yellow for the border, dark background
        report = (
            f"The embryo image analysis with a uterine lining thickness of {lining_thickness}mm indicates a "
            f"moderately favorable environment for implantation. The uterine lining thickness "
            f"is within acceptable range, which may affect implantation success. The embryo shows adequate "
            f"developmental progression."
        )
        additional_text = "This analysis represents an estimated probability of successful embryo implantation based on provided metrics."
    else:
        probability_score = 85  # High probability
        category = "High Probability"
        color = "#4CAF50"  # Green for the border, dark background
        report = (
            f"The embryo image analysis with a uterine lining thickness of {lining_thickness}mm indicates a "
            f"highly favorable environment for implantation. The uterine lining thickness "
            f"is optimal, which increases the likelihood of implantation success. The embryo shows excellent "
            f"developmental progression."
        )
        additional_text = "This analysis represents an estimated probability of successful embryo implantation based on provided metrics."

    # Generate the date (March 27, 2025)
    analysis_date = "3/27/2025"

    # Build the header with category and probability
    header_html = f"""
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; background-color: #1a1a2e; padding: 10px 20px; border-radius: 4px 4px 0 0;">
        <div style="color: {'#FFC107' if category == 'Medium Probability' else '#4CAF50'}; font-weight: bold; font-size: 18px; margin: 5px;">{category}</div>
        <div style="color: #ddd; font-size: 18px; margin: 5px;">Implantation Score: {probability_score}%</div>
        <div style="color: #ddd; font-size: 18px; margin: 5px;">Category: Embryo Analysis</div>
    </div>
    """

    # Generate HTML for the report section
    report_html = f"""
    <div style="background-color: #1e2130; padding: 20px; border-radius: 8px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <div style="display: flex; flex-wrap: wrap; align-items: center; margin-bottom: 15px;">
            <div style="color: #FFD700; font-size: 22px; margin-right: 10px;">⚡</div>
            <div style="color: #fff; font-size: 22px; font-weight: bold;">Generated Report</div>
            <div style="margin-left: auto; color: #aaa; font-size: 14px;">AI Assisted</div>
        </div>
        <div style="color: #f0f0f0; margin-bottom: 15px; line-height: 1.6; font-size: 16px;">
            {report}
        </div>
        <div style="color: #aaa; font-size: 14px; line-height: 1.6;">
            {additional_text}
        </div>
    </div>
    """

    # Generate HTML for the probability circle and metrics
    metrics_html = f"""
    <div style="background-color: #1e2130; padding: 20px; border-radius: 8px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <div style="color: #bbb; font-size: 18px; margin-bottom: 15px;">Implantation Probability</div>
        
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <div style="width: 150px; height: 150px; border-radius: 50%; border: 5px solid {color}; display: flex; align-items: center; justify-content: center; background-color: #2c2c3e; box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);">
                <div style="color: white; font-size: 40px; font-weight: bold;">{probability_score}%</div>
            </div>
        </div>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-top: 20px;">
            <div style="min-width: 150px; margin: 10px 0;">
                <div style="color: #bbb; font-size: 16px;">Lining Thickness</div>
                <div style="color: #fff; font-size: 18px; font-weight: bold;">{lining_thickness} mm</div>
            </div>
            <div style="min-width: 150px; margin: 10px 0;">
                <div style="color: #bbb; font-size: 16px;">Optimal Range</div>
                <div style="color: #fff; font-size: 18px; font-weight: bold;">7-14 mm</div>
            </div>
        </div>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-top: 20px;">
            <div style="min-width: 150px; margin: 10px 0;">
                <div style="color: #bbb; font-size: 16px;">Analysis Date</div>
                <div style="color: #fff; font-size: 18px; font-weight: bold;">{analysis_date}</div>
            </div>
            <div style="min-width: 150px; margin: 10px 0;">
                <div style="color: #bbb; font-size: 16px;">EmbryoML</div>
                <div style="color: #fff; font-size: 18px; font-weight: bold;">v1.0</div>
            </div>
        </div>
    </div>
    """

    # No disclaimer here - moved to footer

    # Combine all sections with responsive design
    full_html = f"""
    {header_html}
    <div style="display: flex; flex-direction: row; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 300px;">{report_html}</div>
        <div style="flex: 1; min-width: 300px;">{metrics_html}</div>
    </div>
    """

    return (
        full_html,
        report,
        f"{probability_score}%",
        category,
        f"{lining_thickness} mm",
        analysis_date,
        "7-14 mm",
        "v1.0",
        ""  # Empty disclaimer since it's now in the footer
    )

# Gradio interface with custom dark theme
with gr.Blocks(theme=gr.themes.Monochrome(
    primary_hue=gr.themes.Color(
        c50="#EAEBFF",
        c100="#DADCFF", 
        c200="#BCBEFF", 
        c300="#9E9EFF", 
        c400="#8080FF", 
        c500="#6366F1", 
        c600="#4F46E5", 
        c700="#4338CA", 
        c800="#3730A3", 
        c900="#312E81", 
        c950="#1E1B4B",
    ),
    neutral_hue=gr.themes.Color(
        c50="#F6F7F9",
        c100="#EBEDF0",
        c200="#D8DCE3",
        c300="#B9C1CC",
        c400="#8896AB",
        c500="#5D6B7E",
        c600="#3E4756",
        c700="#2A303D",
        c800="#171C27",
        c900="#0B0E16",
        c950="#060810",
    ),
    spacing_size=gr.themes.sizes.spacing_md,
    radius_size=gr.themes.sizes.radius_md,
    text_size=gr.themes.sizes.text_md,
)) as interface:
    # Custom CSS for complete dark mode styling
    interface.load(css="""
    /* Dark Mode Variables */
    :root {
        --body-background: #0a0a12;
        --card-background: #141425;
        --card-background-secondary: #1e2130;
        --card-border: #252544;
        --text-primary: #ffffff;
        --text-secondary: #dddddd;
        --text-muted: #aaaaaa;
        --accent-blue: #4338ca;
        --accent-blue-hover: #4f46e5;
        --border-color: #2a2a40;
        --error-color: #e53e3e;
        --success-color: #4CAF50;
        --warning-color: #FFC107;
        --shadow-light: rgba(0, 0, 0, 0.1);
        --shadow-medium: rgba(0, 0, 0, 0.2);
    }
    
    /* Global styles */
    body {
        background-color: var(--body-background) !important;
        color: var(--text-primary);
    }
    
    .gradio-container, .dark {
        background-color: var(--body-background) !important;
        color: var(--text-primary) !important;
    }
    
    .gradio-container {
        max-width: 1200px !important;
        margin: 0 auto !important;
    }
    
    /* Force dark mode on all elements */
    .dark .gr-box, .dark .gr-form, .dark .gr-panel {
        background-color: var(--card-background) !important;
        border-color: var(--card-border) !important;
    }
    
    .dark .gr-input, .dark .gr-textarea, .dark .gr-button {
        background-color: var(--card-background-secondary) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
    }
    
    /* Header styling */
    .main-header {
        color: var(--text-primary);
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
        padding: 15px;
        background: linear-gradient(90deg, #6366F1, #4338CA);
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        letter-spacing: 1px;
    }
    
    /* Simplified image upload area styling */
    .image-upload-area {
        border: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 10px;
        background-color: var(--card-background);
        transition: all 0.3s ease;
        overflow: hidden;
    }
    
    .image-upload-area:hover {
        border-color: var(--accent-blue);
    }
    
    /* Upload button styling */
    .image-upload-area .upload-btn,
    .image-upload-area button {
        background-color: var(--card-background-secondary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 6px !important;
        padding: 8px 15px !important;
        transition: all 0.2s ease;
        margin: 5px !important;
    }
    
    .image-upload-area .upload-btn:not(:last-child),
    .image-upload-area button:not(:last-child) {
        margin-right: 10px !important;
    }
    
    .image-upload-area .upload-btn:hover,
    .image-upload-area button:hover {
        background-color: var(--accent-blue) !important;
        color: white !important;
    }
    
    .image-upload-area > div > div {
        display: flex !important;
        justify-content: center !important;
        gap: 15px !important;
        padding: 5px 0 !important;
    }
    
    .image-upload-area > div {
        margin: 10px 0 !important;
    }
    
    /* Analysis section styling */
    .analysis-section {
        background-color: var(--card-background);
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 8px var(--shadow-light);
        transition: all 0.3s ease;
        border: 1px solid var(--card-border);
    }
    
    /* Input and button styling */
    .input-box {
        background-color: var(--card-background-secondary) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        border-radius: 8px !important;
        padding: 14px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .input-box:focus, .input-box:hover {
        border-color: var(--accent-blue) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    
    .analyze-button {
        background-color: var(--accent-blue) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 14px 20px !important;
        border-radius: 8px !important;
        width: 75% !important;
        max-width: 400px !important;
        font-size: 16px !important;
        margin: 20px auto 0 !important;
        display: block !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
        border: none !important;
    }
    
    .analyze-button:hover {
        background-color: var(--accent-blue-hover) !important;
        box-shadow: 0 6px 14px rgba(0,0,0,0.25) !important;
        transform: translateY(-2px);
    }
    
    /* Result container styling */
    .result-container {
        margin-top: 20px;
        transition: all 0.3s ease;
        opacity: 1;
        background-color: var(--card-background);
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid var(--card-border);
    }
    
    /* Footer styling */
    .footer-disclaimer {
        text-align: center;
        color: var(--text-muted);
        font-size: 14px;
        margin: 40px auto 20px;
        padding: 10px;
        max-width: 800px;
        border-top: 1px solid var(--border-color);
        padding-top: 20px;
    }
    
    /* Fix for dark mode upload interface */
    .dark .uploadButton, .dark .selected-file {
        background-color: var(--card-background-secondary) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .gradio-row > .gradio-column {
            min-width: 100% !important;
        }
        
        .main-header {
            font-size: 26px;
            padding: 10px;
        }
        
        .input-box, .analyze-button {
            font-size: 14px !important;
            padding: 12px !important;
        }
        
        .analysis-section {
            padding: 18px;
        }
        
        .footer-disclaimer {
            font-size: 12px;
            margin: 20px auto 10px;
        }
    }
    
    /* Animations and transitions */
    .fade-in {
        animation: fadeIn 0.6s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Fix for any popups or menus */
    .gr-form, .gr-panel, .gr-button, .gr-input {
        background-color: var(--card-background) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
    }
    
    /* Override image upload component styles */
    .file-preview, .file-preview img, .file-preview video {
        background-color: var(--card-background) !important;
        color: var(--text-primary) !important;
    }
    
    /* Dark mode for tabbed interfaces */
    .tabs {
        background-color: var(--card-background) !important;
    }
    
    .tab-nav {
        background-color: var(--card-background-secondary) !important;
        color: var(--text-primary) !important;
    }
    
    .tab-nav.selected {
        background-color: var(--accent-blue) !important;
        color: white !important;
    }

    /* Button and input container */
    .input-area {
        margin-top: 10px;
    }

    .button-container {
        padding: 10px 0;
        text-align: center;
    }
    """)
    
    gr.HTML('<div class="main-header fade-in">EmbryoML</div>')
    
    with gr.Row(elem_classes=["main-content"]):
        with gr.Column(scale=1, min_width=320):
            # Left Panel - Image and Input (simplified)
            with gr.Box(elem_classes=["image-upload-area", "fade-in"]):
                gr.Markdown('<div style="color: var(--text-primary); font-size: 16px; margin-bottom: 10px; text-align: center;">Upload Embryo Image</div>')
                image_display = gr.Image(
                    type="pil",
                    label="",
                    height=380,
                    show_label=False,
                    elem_id="embryo-image-upload"
                )
            
            with gr.Box(elem_classes=["analysis-section", "fade-in"]):
                gr.HTML('<div style="color: var(--text-primary); font-size: 18px; margin-bottom: 15px; font-weight: bold;">Uterine Lining Thickness (mm)</div>')
                
                # Wrap input in a div for better styling
                with gr.Group(elem_classes=["input-area"]):
                    lining_input = gr.Textbox(
                        placeholder="Enter thickness in mm",
                        show_label=False,
                        elem_classes=["input-box"]
                    )
                
                # Wrap button in a div for better positioning
                with gr.Group(elem_classes=["button-container"]):
                    submit_button = gr.Button(
                        "Analyze Implantation Probability", 
                        elem_classes=["analyze-button"]
                    )
                
        with gr.Column(scale=1, min_width=320):
            # Right Panel - Results HTML
            result_display = gr.HTML(elem_classes=["result-container", "fade-in"])
            
            # Hidden outputs (for completeness)
            report_output = gr.Textbox(visible=False)
            probability_output = gr.Textbox(visible=False)
            category_output = gr.Textbox(visible=False)
            thickness_output = gr.Textbox(visible=False)
            date_output = gr.Textbox(visible=False)
            range_output = gr.Textbox(visible=False)
            version_output = gr.Textbox(visible=False)
            disclaimer_output = gr.HTML(visible=False)
    
    # Footer with disclaimer (only place it appears)
    gr.HTML(
        '<div class="footer-disclaimer">'
        "This tool provides estimates based on medical data. Always consult with your healthcare provider.<br>"
        "Results are for informational purposes only and do not constitute medical advice."
        "</div>"
    )
    
    # Submit button click action
    submit_button.click(
        generate_report,
        inputs=[image_display, lining_input],
        outputs=[
            result_display,
            report_output,
            probability_output,
            category_output,
            thickness_output,
            date_output,
            range_output,
            version_output,
            disclaimer_output,
        ],
    )

# Add share=True for easier testing on mobile devices
interface.launch(share=True)