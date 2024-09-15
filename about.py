from shiny import ui, render

layout_about = ui.page_fluid(
  ui.tags.style("""
    html {
      background: linear-gradient(345deg, #aa80ff, #c39ad7);
    } 
    body {
      background: transparent;
    }
    .groupAbouts {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-gap: 20px;
      margin: 50px 100px 0;
      justify-content: center;
    }
    .aboutDisplay {
      padding: 0 20px 0;
      text-align: center; 
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .aboutDisplay > img {
      height: fit-content !important;
    }
    #TylerJpg, #ShelbyJpg, #JoshPng {
      width: fit-content;
      height: fit-content !important;
      margin: 0 0 10px;
    }
    .aboutLinks {
      display: flex;
      justify-items: center;
    }
    .aboutLinks > a {
      padding: 0 5px;
    }
    .aboutNameDisplay {
      font-weight: bold;
      color: white;
    }
    """),
  ui.div({"class": "ABackground"}),
  ui.div({"class": "groupAbouts"}, 
    ui.div({"class": "aboutDisplay"},
      ui.output_image("TylerJpg"),
      ui.h1({"class": "aboutNameDisplay"}, "Tyler Knapp"),
      ui.markdown("About me:")
    ),
    ui.div({"class": "aboutDisplay"},
      ui.output_image("ShelbyJpg"),
      ui.h1({"class": "aboutNameDisplay"}, "Shelby Wentz"),
      ui.markdown("About me:")
    ),
    ui.div({"class": "aboutDisplay"},
      ui.output_image("JoshPng"),
      ui.h1({"class": "aboutNameDisplay"}, "Joshua Hill"),
      ui.markdown("About me:"),
      ui.div({"class": "aboutLinks"},
        ui.a(
          ui.markdown("GitHub"),
          href="https://github.com/JoshHill1",
          target="_blank"
        ),
        ui.a(
          ui.markdown("LinkedIn"),
          href="https://www.linkedin.com/in/joshuahillaz0d/",
          target="_blank"
        ),
      )
    ),
  ),
),

@render.image  
def TylerJpg():
  return {
    "src": "www/149127780.jpg",
    "style": """
      width: 300px;
      height: auto;
      border-radius: 50%;
      """
}
@render.image  
def  ShelbyJpg():
  return {
    "src": "www/172392281.jpg",
    "style": """
      width: 300px;
      height: auto;
      border-radius: 50%;
      """
}
@render.image  
def JoshPng():
  return {
    "src": "www/JHeadshot.png",
    "style": """
      width: 300px;
      height: auto;
      border-radius: 50%;
      """
}