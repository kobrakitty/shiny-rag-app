from shiny import ui

layout_about = ui.page_fluid(
  ui.tags.style("""                  
    tab-pane {
      display: none !important;
    }    
    """),
  ui.page_sidebar(
    ui.sidebar(
      ui.markdown("Hello World!"),
      # Used to block out the extra padding on the sides of the page_liquid
      class_="p-0"
    ),
  ),
),