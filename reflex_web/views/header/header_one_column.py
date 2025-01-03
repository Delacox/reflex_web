import reflex as rx
from reflex_web.components.logo import logo

def header_one_column() -> rx.Component:
    return rx.box(
        # Desktop view
        rx.desktop_only(
            rx.container(
                rx.center(
                    rx.flex(
                        # Heading
                        rx.badge(
                            rx.flex(
                                rx.icon("laptop"),
                                rx.text("Soporte técnico remoto",
                                    size="3",
                                    #color=rx.color("gray", 12),
                                    ),
                                width="100%",
                                spacing="4",
                                align="center",
                                padding_x="5px",
                                ),
                            variant="soft",
                            margin_x="auto",
                            radius="large"
                            ),
                        
                        rx.heading(
                            "Siempre tranquilo y actualizado con ",
                            rx.text.span(
                                "Tu ",
                                color=rx.color("green", 11),
                                align="center"
                            ),
                            "informático Online",
                            font_size="3.2rem",
                            as_="h1",
                            text_align="center",
                            width="95%",
                            margin_bottom="10px",
                            z_index="4",
                            line_height="1.1",
                            margin_x="auto"
                        ),
                        # Video with enhanced background effect
                        rx.box(
                            rx.video(
                                url="https://youtu.be/OEHzxw4O-U4",
                                border_radius="10px",
                                light=True, #Poner true para ver imagen destacada
                                
                            ),
                            class_name="video-container",  # Aplica la clase CSS
                            position="relative",
                            z_index="1",
                            border_radius="10px",
                            overflow="hidden",
                            box_shadow="0px 12px 50px rgba(61, 214, 140, 0.7), 0px 0px 100px rgba(61, 214, 140, 0.4)",
                            margin="0 auto",
                            animation="pulse-smooth 6s ease-in-out infinite",  # Animación más fluida
                        ),
                        rx.box(
                            rx.center(
                                rx.button(
                                  rx.hstack(
                                      rx.icon("phone"),
                                      rx.text("Llámanos"),
                                      align="center"
                                  ),  
                                  size="4",
                                  variant="soft",
                                  margin_top="1em",                                  
                                  color_scheme="green",
                                  padding_x="2em",
                                  ),
                                
                                )
                            ),
                        width="100%",
                        justify="center",
                        flex_direction="column",
                        spacing="6",
                    ),
                ),
            ),
        ),
        # Mobile and tablet view
        rx.mobile_and_tablet(
            rx.container(
                rx.center(
                    rx.vstack(
                        # Heading
                        rx.badge(
                            rx.flex(
                                rx.icon("laptop"),
                                rx.text("Soporte técnico remoto",
                                    size="3",
                                    variant="surface",
                                    ),
                                width="100%",
                                spacing="4",
                                align="center",
                                padding_x="5px"
                                ),
                            
                            margin_x="auto",
                            radius="large"
                            ),
                        rx.heading(
                            "Siempre tranquilo y actualizado con ",
                            rx.text.span(
                                "Tu ",
                                color=rx.color("green", 11),
                            ),
                            "informático Online",
                            size="8",
                            as_="h1",
                            text_align="center",
                            width="100%",
                            margin_bottom="10px",
                            z_index="4"
                        ),
                        # Video with simpler effect for mobile
                        rx.box(
                            rx.video(
                                url="https://tuinformatico.online/wp-content/uploads/2024/11/03_Bienvenida.mp4",
                                width="auto",
                                height="auto",
                                border_radius="10px",
                            ),
                            class_name="video-container",  # Aplica la clase CSS
                            position="relative",
                            z_index="1",
                            border_radius="10px",
                            overflow="hidden",
                            box_shadow="0px 12px 50px rgba(61, 214, 140, 0.7), 0px 0px 100px rgba(61, 214, 140, 0.4)",
                            margin="0 auto",
                            animation="pulse-smooth 6s ease-in-out infinite",  # Animación más fluida
                        ),
                        rx.box(
                            rx.center(
                                rx.button(
                                  rx.hstack(
                                      rx.icon("phone"),
                                      rx.text("Llámanos"),
                                      align="center"
                                  ),  
                                  size="4",
                                  variant="soft",
                                  margin_top="1em",                                  
                                  color_scheme="green",
                                  padding_x="2em",
                                  ),
                                
                                ),
                            width="100%"                            
                            ),
                        width="100%",
                        spacing="7",
                    ),
                ),
            ),
        ),
        width="100%",
    )
