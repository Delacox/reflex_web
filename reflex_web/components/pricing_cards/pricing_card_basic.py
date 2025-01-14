import reflex as rx

def feature_item(text: str) -> rx.Component:
    return rx.hstack(
        rx.icon("check", color=rx.color("grass", 9)),
        rx.text(text, size="4"),
    )


def features() -> rx.Component:
    return rx.vstack(
        feature_item("1 Hora de soporte informático"),
        rx.divider(width="90%", margin="auto"),
        feature_item("Consultas ilimitadas"),
        rx.divider(width="90%", margin="auto"),
        feature_item("Asistencia en tus compras"),
        rx.divider(width="90%", margin="auto"),
        feature_item("Gestión de expertos"),
        width="100%",
        align_items="start",
    )


def pricing_card_basic() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Basico", weight="bold", size="6"),
            rx.text(
                "Ideal choice for personal use & for your next project.",
                size="4",
                opacity=0.8,
                align="center",
            ),
            rx.hstack(
                rx.text(
                    "39,99€",
                    weight="bold",
                    font_size="3rem",
                    trim="both",
                ),
                rx.text(
                    "/mes",
                    size="4",
                    opacity=0.8,
                    trim="both",
                ),
                width="100%",
                align_items="end",
                justify="center",
            ),
            width="100%",
            align="center",
            spacing="6",
        ),
        features(),
        rx.button(
            "Contratar",
            size="3",
            variant="solid",
            width="100%",
            color_scheme="green",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="350px",
        justify="center",
        border_radius="0.5rem",
        color_scheme="green",
        height="100%",
  
        
    )