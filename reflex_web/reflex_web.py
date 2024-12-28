import reflex as rx
from reflex.style import toggle_color_mode
 

# Clase de estado para gestionar el tema.
class State(rx.State):
    pass

# Definimos la interfaz.
def index() -> rx.Component:
    return rx.box(
            
            rx.vstack(
                rx.button(
                    rx.color_mode_cond(light=rx.image(src="/dark.png"), dark=rx.image(src="/light.png")),
                    color=rx.color_mode_cond(light="white", dark="black"),
                    background_color= rx.color("green", 11),
                    on_click=toggle_color_mode,
                    width="50px",
                ),
                align="end",
                margin="1em",
            ),
            
            rx.box(
                rx.text(
                        rx.text.span(
                        "Tu ",
                        color=rx.color("green", 11),
                        ),
                        "informático",
                        color=rx.color_mode_cond(light="black", dark="white"),
                        font_size="48px",
                        font_weight= 600,                    
                    ),   
                rx.text(
                        "Online",
                        color=rx.color_mode_cond(light="black", dark="white"),
                        font_size="48px",
                        font_weight= 600,
                        
                    ),
                
                    
                
                
                font_family="Poppins",
                margin="3em",
            ),
    )  
    
    
                
        

# Configura la aplicación.
 
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
    ],
    theme=rx.theme(
        appearance="dark"
    )
    
        
)

app.add_page(index)
