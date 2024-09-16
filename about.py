from shiny import ui, render

layout_about = ui.page_fluid(
  ui.tags.style("""
    html {
      background: linear-gradient(345deg, #aa80ff, #c39ad7), no-repeat center center fixed;
      background-size: cover;
      height: 100%;
    } 
    body {
      background: transparent;
      height: 100%;
      margin: 0;
      padding: 0;
    }
    .groupAbouts {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-gap: 20px;
      margin: 445px 100px 0;
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
    .topSection {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      margin: 50px 225px;
    }
    .topSection img {
      width: 1000px;
      height: auto;
    }
    .description {
      font-size: 1.2em;
      color: white;
      max-width: 500px;
      margin-left: 50px;
    }
    """),

      # Top section with image and description
  ui.div({"class": "topSection"}, 
    ui.output_image("ProcessFlowPng"),
    ui.div({"class": "description"}, 
      ui.h2("Shiny RAG App"),
      ui.p("Welcome to our website! This platform utilizes Retrieval-Augmented Generation (RAG) technology to provide advanced document searching capabilities within your organization, powered by AI and seamless integration. Feel free to explore and enjoy our application!")
    )
  ),

  # Grid with the tam members
  ui.div({"class": "ABackground"}),
  ui.div({"class": "groupAbouts"}, 
    ui.div({"class": "aboutDisplay"},
      ui.output_image("TylerJpg"),
      ui.h1({"class": "aboutNameDisplay"}, "Tyler Knapp"),
       ui.div({"class": "aboutLinks"},
      ui.a(
            ui.output_image("githubTyler", inline=True),
            href="https://github.com/Tyler-KD",
            target="_blank"
        ),
        ui.a(
          ui.output_image("linkedinTyler", inline=True),
            href="https://www.linkedin.com/in/tyler-knapp-8717862a7/",
            target="_blank"
        ),
       ),
    ),
    ui.div({"class": "aboutDisplay"},
      ui.output_image("ShelbyJpg"),
      ui.h1({"class": "aboutNameDisplay"}, "Shelby Wentz"),
       ui.div({"class": "aboutLinks"},
      ui.a(
            ui.output_image("githubShelby", inline=True),
            href="https://github.com/kobrakitty",
            target="_blank"
        ),
        ui.a(
          ui.output_image("linkedinShelby", inline=True),
            href="https://www.linkedin.com/in/shelby-w/",
            target="_blank"
        ),
       ),
    ),
    ui.div({"class": "aboutDisplay"},
      ui.output_image("JoshPng"),
      ui.h1({"class": "aboutNameDisplay"}, "Joshua Hill"),
      ui.div({"class": "aboutLinks"},
        ui.a(
            ui.output_image("githubJosh", inline=True),
            href="https://github.com/JoshHill1",
            target="_blank"
        ),
        ui.a(
          ui.output_image("linkedinJosh", inline=True),
            href="https://www.linkedin.com/in/joshuahillaz0d/",
            target="_blank"
        ),
      )
    ),
  ),
),

@render.image
def githubTyler():
  return {"src": "www/github-mark.png", "style": "text-align: center; width: 35px; height: 35px;"}    

@render.image
def githubShelby():
  return {"src": "www/github-mark.png", "style": "text-align: center; width: 35px; height: 35px;"}    

@render.image
def githubJosh():
  return {"src": "www/github-mark.png", "style": "text-align: center; width: 35px; height: 35px;"}    

@render.image
def linkedinTyler():
  return {"src": "www/logo-linkedin.png", "style": "text-align: center; width: 35px; height: 35px;"}  

@render.image
def linkedinShelby():
  return {"src": "www/logo-linkedin.png", "style": "text-align: center; width: 35px; height: 35px;"}  

@render.image
def linkedinJosh():
  return {"src": "www/logo-linkedin.png", "style": "text-align: center; width: 35px; height: 35px;"}  

@render.image
def ProcessFlowPng():
  return {
    "src": "www/Shiny RAG App Process Flow.png",
  }
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