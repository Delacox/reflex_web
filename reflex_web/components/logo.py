import reflex as rx

def logo(font_size) -> rx.Component:
    return rx.heading(
        rx.vstack(
            rx.text("Tu",
                    trim="both",
                    color= rx.color("green", 11),
                    font_size=font_size, ),
            rx.text("informático",
                            trim="both",
                            font_size=font_size, ),
            rx.text("Online",
                    trim="both",
                    font_size=font_size, ),
        ),
        weight="bold",
        font_family="Poppins",
        margin="0.5em",
),


