from shiny import ui

styles_app = ui.page_fluid(
    ui.tags.style("""
        @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');

        body, button, input, select, textarea {
            font-family: 'Fredoka One', cursive;
            font-weight: 600;
            font-size: 1.1em;
            color: #FF61D8;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
        }

        h1, h2, h3, h4, h5, li {
            color: #8A64FF;
        }

        .btn:hover {
            transform: scale(1.05);
            transition: transform 0.2s ease;
        }

        html {
            overflow: hidden !important;
        }
        body {
            overflow: hidden !important;
            height: fit-content; #makes sure the background image isn't cut off
        }
        .row {
          overflow-x: hidden;
          --bs-gutter-x: 0;
        }
        #background img {
            object-fit: contain !important;
            overflow: hidden !important;
            width: 100vw !important;
            height: auto !important;
        }
        #background {
            position: absolute;
            top: 0;
            left: 0;
        }
        .bslib-sidebar-layout {
            --_sidebar-width: 25vw !important; /* Override the sidebar width to 1/4 of the screen */
            background-image: url('www/background1.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .bslib-sidebar-layout>.sidebar {
            border-right: 0;
            backdrop-filter: blur(2px);
            background: rgba(255, 255, 255, 0.07);
        }
        .bslib-sidebar-layout>.sidebar>.sidebar-content {
            padding: 24px;
            gap: 0;
        }
        #file_info {
            margin: 20px 0;
        }
        .form-group,.form-check, .shiny-input-container .checkbox, .shiny-input-container .radio {
            margin: 0;
        }
        #fixedFileSpacing>.mb-2,uploaded-files-spacing {
            margin-bottom: 18px !important;
        }
        .checkbox label {
            width: 100%;
            cursor: default !important;
        }
        .checkbox label input {
            cursor: pointer;         
        }
        .bslib-sidebar-layout>.sidebar>.sidebar-content>.accordion:not(:last-child) .accordion-item:last-child {
            border: none !important;
        }
        .accordion-body {
            padding: 8px 20px 0;
        }
        .sidebar {
            height: 100vh;
            box-shadow: 2px 0 5px rgba(0,0,0,0.2);
            overflow-y: auto;
        }
        .sidebar::-webkit-scrollbar {
            width: 18px;
        }
        .sidebar::-webkit-scrollbar-track {
            background: #1E0F3C; // Deep purple
        }
        .sidebar::-webkit-scrollbar-thumb {
            background: #FF61D8; // Bright pink
        }
        .btn-primary {
            background-color: #8A64FF; // Soft purple
            border-color: #8A64FF;
            color: #FFFFFF;
        }
        .btn-primary:hover, .file-input:hover::file-selector-button {
            background-color: #FF9EE5; // Soft pink
            border-color: #FF9EE5;
            color: #4B0082; // Dark purple for contrast
        }
        .btn-danger {
            background-color: #FF6B9E; // Soft red
            border-color: #FF6B9E;
            color: #FFFFFF;
        }
        .btn-danger:hover {
            background-color: #FFB6C1; // Light pink
            border-color: #FFB6C1;
            color: #4B0082; // Dark purple for contrast
        }
        .form-control:focus {
            border-color: #589FD5;
            box-shadow: 0 0 0 0.2rem rgba(88, 159, 213, 0.25);
        }
        #process_output {
            background-color: #F5F5F5;
            border: 1px solid #E0E0E0;
            padding: 15px;
            margin-top: 20px;
            border-radius: 7px;
            white-space: pre-wrap;
        }
        h1, h2, h3, h4, h5, li {
            color: #8A64FF;
        }
        .mt-2 {
            margin-top: 0.5rem;
        }
        .mt-3 {
            margin-top: 1rem;
        }
        .sidebar .form-check-label {
            color: #4E4E4E;
        }
        .logoWelcome {
            display: flex;
            justify-content: space-between;
        }
        #time_display {
            text-align: right;
        }
        .time-display-column {
            font-size: 1.1em;
            display: flex;
            flex-direction: column;
            jusify-content: space-between;
        }
        .time-display-column {
            justify-content: space-between;
        }
        .time-display-column > h1.greeting {
            font-size: 2.5em;
            font-weight: bold;
            font-style: italic;
            margin: 0;
        }
        # .language-toggle {
        #     margin-top: 20px;
        #     margin-bottom: 20px;
        # }
        .file-input::file-selector-button {
            background-color: #64C8FF; // Soft blue
            color: #FFFFFF;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
        }
        .file-input:hover::file-selector-button {
            background-color: #9EE5FF; // Light blue
            color: #4B0082; // Dark purple for contrast
        }
        .shiny-input-container:not(.shiny-input-container-inline) {
            width: 100%;
        }
        .sensitive-file {
            color: red;
            font-weight: bold;
        }
        #download_chat {
            margin-top: 10px;
            margin-bottom: 20px;
        }
        .instructions-output>h3 {
            font-weight: bold;
            font-size: 58px;
            color: #FFF;
            -webkit-text-stroke: 3px #8A64FF;
        }
    """)
)