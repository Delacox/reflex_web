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
        # Contenedor principal con fondo y color base
        rx.box(
            # Capa de imagen de fondo con desenfoque
            rx.box(
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                background_image=rx.color_mode_cond(
                    light="linear-gradient(to bottom, rgba(225, 230, 222, 0.3) 80%, rgba(255, 255, 255, 1) 100%), url('/fondo_bosque.jpg')",
                    dark="linear-gradient(to bottom, rgba(0, 0, 0, 0.2) 80%, rgba(0, 0, 0, 1) 100%), url('/fondo_bosque.jpg')"
                ),
                background_position="center",
                background_size="cover",
                filter="blur(3px) brightness(0.9)",
                z_index="0",
            ),
            # Contenido principal
            rx.box(
                rx.box(
                    navbar_buttons(),
                ),
                rx.box(
                    padding_top="8em"
                ),
                rx.center(
                    rx.vstack(
                        header_one_column(),
                        width="80%",
                    ),
                    width="100%",
                ),
                position="relative",
                z_index="1",
                width="100%",
                min_height="100vh",
                background_color=rx.color_mode_cond(
                    light="rgba(225, 230, 222, 0.7)",
                    dark="rgba(0, 0, 0, 0.4)"
                ),
            ),
            position="relative",
            width="100%",
            min_height="100vh",
            overflow="hidden",
        ),
        # Box para el dark mode toggle
        rx.box(
            dark_mode_toggle(),
            
        ),
        width="100%",
        min_height="100vh",
        background_color=rx.color_mode_cond(
            light="rgba(225, 230, 222, 1)",
            dark="rgba(0, 0, 0, 1)"
        ),
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
        accent_color= "green",
        font_family="Poppins",
    ),
    style=style,

 

        
)

app.add_page(
    index,
    title="Inicio | Tu Informático Online",
    description="Servicios profesionales de informática y tecnología", 
    meta=[
        {"name": "keywords", "content": "informático,servicios,tecnología"},
        {"name": "robots", "content": "index, follow"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)