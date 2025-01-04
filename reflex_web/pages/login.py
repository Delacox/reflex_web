import reflex as rx
import reflex_web.utils as utils
from reflex_web.components.navbar import navbar_buttons
from reflex_web.routers import Route
from reflex_web.components.login_form import login_form
from reflex_web.views.footer.footer import footer




# Definimos la interfaz.
# Lo que creemos con el decorador rx.page sera una pagina 
@rx.page(
    route = Route.LOGIN.value,
    title=utils.login_title,
    description=utils.login_description,
    image=utils.preview,
    meta=utils.login_meta,
)
def login() -> rx.Component:
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
                    # codigo para la pagina
                    login_form()
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
        rx.container(
            footer(),
            size="4"
        ),
        width="100%",
        min_height="100vh",
        background_color=rx.color_mode_cond(
            light="rgba(225, 230, 222, 1)",
            dark="rgba(0, 0, 0, 1)"
        ),
    )


