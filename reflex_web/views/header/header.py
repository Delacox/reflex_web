import reflex as rx
from reflex_web.components.logo import logo

def header() -> rx.Component:
    return rx.box(  
        rx.desktop_only(
            rx.container(
                rx.hstack(
                    logo(font_size="56px"),
                    rx.spacer(),
                    rx.image(
                        src="/header.webp",
                        width="50%",
                        max_width="400px",
                        height="auto",
                        border_radius="5%",
                        border="2px solid",
                        border_color=rx.color("green", 11),
                        box_shadow="0px 2px 5px rgba(61, 214, 140, 0.3)",
                        
                    ),
                    width="100%",
                    max_width="1200px",
                ),
                size="4",
            )
),
        rx.mobile_and_tablet(
            rx.vstack(
                logo(font_size="48px"),
                rx.image(
                    src="/header.webp",
                    width="100%",
                    max_width="800px",
                    height="auto",
                    border_radius="5%",
                    
                    box_shadow="4px 6px 3px rgba(61, 214, 140, 0.3)",
                ),
                width="100%",
            ),
            width="100%",
        
    ),
    width = "100%",
   
)
