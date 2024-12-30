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
                        rx.heading(
                            "Siempre tranquilo y actualizado con ",
                            rx.text.span(
                                "Tu ",
                                color=rx.color("green", 11),
                            ),
                            "informático Online",
                            size="9",
                            as_="h1",
                            text_align="center",
                            width="100%",
                            margin_bottom="10px",
                        ),
                        # Video with enhanced background effect
                        rx.box(
                            rx.video(
                                url="https://tuinformatico.online/wp-content/uploads/2024/11/03_Bienvenida.mp4",
                                width="600px",
                                height="auto",
                                border_radius="10px",
                            ),
                            class_name="video-container",  # Aplica la clase CSS
                            position="relative",
                            z_index="1",
                            border_radius="10px",
                            overflow="hidden",
                            box_shadow="0px 8px 35px rgba(61, 214, 140, 0.6)",
                            margin="0 auto",
                            animation="pulse 6s ease-in-out infinite",  # Ajusta velocidad y fluidez
                        ),
                        width="100%",
                        justify="center",
                        flex_direction="column",
                        spacing="1",
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
                        rx.heading(
                            "Siempre tranquilo y actualizado con ",
                            rx.text.span(
                                "Tu ",
                                color=rx.color("green", 11),
                            ),
                            "informático Online",
                            size="7",
                            as_="h1",
                            text_align="center",
                            width="100%",
                            margin_bottom="10px",
                        ),
                        # Video with simpler effect for mobile
                        rx.box(
                            rx.video(
                                url="https://tuinformatico.online/wp-content/uploads/2024/11/03_Bienvenida.mp4",
                                width="100%",
                                max_width="400px",
                                height="auto",
                                border_radius="10px",
                            ),
                            box_shadow="0px 6px 30px rgba(61, 214, 140, 0.5)",
                            margin="0 auto",
                            animation="pulse 6s ease-in-out infinite",  # Ajusta velocidad y fluidez
                        ),
                        width="100%",
                        spacing="1",
                    ),
                ),
            ),
        ),
        width="100%",
    )
