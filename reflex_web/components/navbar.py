import reflex as rx
from reflex_web.components.logo import logo

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color=rx.color("slate", 12),), href=url
    )

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    logo(font_size="16px"),
                    spacing="0"
                ),
                rx.spacer(),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Nosotros", "/#"),
                    navbar_link("Precios", "/#"),
                    navbar_link("Contacto", "/contacto"),
                    spacing="5",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.button(
                        "Registro",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding_x="2em"
            ),
                
                   
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    logo(font_size="16px"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Inicio", href="/"),
                        rx.menu.item("Nosotros"),
                        rx.menu.item("Precios"),
                        rx.menu.item("Contacto", href="/contacto"),
                        rx.menu.separator(),
                        rx.menu.item("Registro"),
                        rx.menu.item("Sign up"),
                        side="left",
                        background_color=rx.color_mode_cond(
                                light="rgba(250, 255, 245, 0.95)",  # fondo semi-transparente
                                dark="rgba(31, 31, 35, 0.95)"
                            ),
                        
                    ),
                    modal=False, # Hace que no bloque la pagina ni desaparezca el scroll
                    justify="end",
                ),
                justify="between",
                align_items="center",
                margin="0.2em",
                margin_x="2em",
                
            ),
            width="100%"
        ),
        width=["80%", "80%", "80%"],  # mobile, tablet, desktop
        margin_x="auto",  # centra la caja horizontalmente
        border_radius="12px",  # bordes redondeados para efecto flotante
        position="fixed",
        top="1em",
        left="50%",
        transform="translate(-50%, 0)",  # centra la caja usando transform
        backdrop_filter="blur(8px)",  # efecto de vidrio esmerilado opcional
        background_color=rx.color_mode_cond(
            light="rgba(250, 255, 245, 0.6)",  # fondo semi-transparente
            dark="rgba(31, 31, 35, 0.6)"
        ),
        box_shadow="0px 2px 5px rgba(61, 214, 140, 0.3)",
        z_index="999"
        
        
    )
    
    
    