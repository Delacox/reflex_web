import reflex as rx
from reflex_web.components.logo import logo

def header_one_column() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.container(
                rx.flex(
                    rx.heading(
                        "Siempre tranquilo y actualizado con ",
                        rx.text.span(
                            "Tu ",
                            color=rx.color("green", 11),
                        ),
                        "informático Online",
                        size="9",
                        as_="h1",
                        width="100%",
                        align="center"
                    ),
                    width="100%",
                    justify="center",
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.container(
                rx.flex(
                    rx.heading(
                        "Siempre tranquilo y actualizado con ",
                        rx.text.span(
                            "Tu ",
                            color=rx.color("green", 11),
                        ),
                        "informático Online",
                        size="8",
                        as_="h1",
                        width="100%",
                        align="center"
                    ),
                    width="100%",
                    justify="center",
                ),
            ),
            ),
        width="100%",
    )