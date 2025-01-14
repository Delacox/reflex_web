import reflex as rx
import reflex_web.utils as utils
from reflex_web.components.navbar import navbar_buttons
from reflex_web.routers import Route
from reflex_web.components.contact_form import contact_form
from reflex_web.views.footer.footer import footer



# Definimos la interfaz.
# Lo que creemos con el decorador rx.page sera una pagina 
@rx.page(
    route = Route.CONTACT.value,
    title=utils.contact_title,
    description=utils.contact_description,
    image=utils.preview,
    meta=utils.contact_meta,
)
def contact() -> rx.Component:
    return rx.box(
        utils.lang(),
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
                    padding_top="9em"
                ),
                rx.container(
                    rx.center(
                        rx.heading(
                            "Dejo dos formularios para ver el comportamiento responsive",
                            padding="1em",
                            text_align="center",                            
                        ),
                        rx.flex(
                            contact_form(),contact_form(),
                            flex_direction=["column", "column", "row"],
                            spacing="5", 
                        ),

                    size="4",
                    direction="column",
                    ) 
                    
                    
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


        rx.box(
            footer(),
            
        ),
        width="100%",
        min_height="100vh",
        background_color=rx.color_mode_cond(
            light="rgba(225, 230, 222, 1)",
            dark="rgba(0, 0, 0, 1)"
        ),
    )


