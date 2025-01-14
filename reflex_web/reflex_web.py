import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.pages.index import index
from reflex_web.pages.contact import contact
from reflex_web.pages.about_us import about_us
from reflex_web.pages.prices import prices
from reflex_web.pages.signup import signup
from reflex_web.pages.login import login



# Configuramos el state
class state(rx.State):
    """Clase state"""


# Configura la aplicación.

app = rx.App(
    style=styles.BASE_STYLE, 
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
      
)
