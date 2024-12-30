import reflex as rx
from reflex_web.components.dark_mode import dark_mode_toggle
from reflex_web.components.navbar import navbar_buttons
from reflex_web.views.header.header import header
from reflex_web.views.header.header_one_column import header_one_column

style = {
    "html": {
        "overflow_y": "scroll",
    },
    "body": {
        "overflow_y": "scroll",
    }
}

# Clase de estado para gestionar el tema.
class State(rx.State):
    pass

# Definimos la interfaz.
def index() -> rx.Component:
    return rx.box(
        rx.box(
            navbar_buttons(),
        ),
        rx.box(
            dark_mode_toggle(),
            padding_top="7em",
        ),
        rx.center(
            rx.vstack(
                
                header_one_column(),
                header(),
                header(),
                header(),
                header(),
                width="80%",
            ),
            width="100%",
        ),
        width="100%",
        min_height="100vh",
        background_color=rx.color_mode_cond(
            light="#f4f4f4",  
            dark="#232323"   
        )
         
    ) 
    
    
                
        

# Configura la aplicación.
 
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
        "/styles.css"
    ],
    theme=rx.theme(
        appearance="light",
        has_background=True,
        panel_background="solid",
        accent_color= "green",
        font_family="Poppins",
    ),
    style=style,

 

        
)

app.add_page(index)
