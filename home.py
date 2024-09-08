from shiny import ui
from styles import styles_app

layout_home = ui.page_fluid(
    ui.output_image("background"),
    ui.tags.style(styles_app),
    ui.page_sidebar(
        ui.sidebar(
            ui.h2("File Upload", style="color: #0E4878;"),
            ui.input_file("file_upload", "Upload a file by clicking Browse below", multiple=True),
            ui.output_text_verbatim("file_info"),
            ui.accordion(
                ui.accordion_panel(
                    ui.markdown("### Uploaded files:"),
                    ui.output_ui("uploaded_files_list"),
                )
            ),
            ui.input_action_button("process_button", "Process Selected Files", class_="btn-primary mt-2 PSDbtn"),
            ui.input_action_button("summarize_button", "Summarize Selected Files", class_="btn-primary mt-2 PSDbtn"),
            ui.input_action_button("delete_button", "Delete Selected Files", class_="btn-danger mt-2 PSDbtn"),
            ui.div(
                ui.input_text_area("user_question", "Ask a question about the file(s):"),
                ui.input_action_button("submit_question", "Submit Question", class_="btn-primary mt-2"),
                class_="mt-3"
            ),
            ui.div(
                ui.input_text("openai_api_key", "Enter OpenAI API Key:", placeholder="sk-..."),
                class_="mt-3"
            ),
        open="open"),
        ui.div({"class": "logoWelcome"}, 
            ui.output_image("TSJ", inline=True),
            ui.div({"class": "time-display-column"},
                ui.output_text("time_display"),
                ui.h1({"class": "greeting"}, "Welcome!"),
                ),
            ),
        ui.div({"class": "instructions-output"},
            ui.h3("Instructions:"),
            ui.tags.ul(
                ui.tags.li("In the sidebar to the left, click 'Browse' to select your files."),
                ui.tags.li("Click 'Process Selected Files' to initiate processing."), 
                ui.tags.li("Enter your OpenAI API key to use gpt-4o-mini for summarization and answering questions."),
                ui.tags.li("Select files and click 'Summarize Selected Files' or 'Submit Question.'"),
                ui.tags.li("Output will be displayed below."),
            ),
            ui.h3("Output:", class_="section-header"),
            ui.output_text_verbatim("process_output"),
            ui.download_button("download_chat", "Download Chat", class_="btn-primary mt-2"),
        ),
        ui.output_text_verbatim("api_key_info"),
        ui.output_text_verbatim("progress_output"),
    ),
    # Used to block out the extra padding on the sides of the page_liquid
    class_="p-0",
)

