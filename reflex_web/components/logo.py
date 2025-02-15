import reflex as rx

def logo(font_size) -> rx.Component:
    return rx.heading(
        rx.vstack(
            rx.text("Tu",
                    trim="both",
                    color= rx.color("green", 11),
                    font_size=font_size, ),
            rx.text("informáticoo",
                            trim="both",
                            font_size=font_size,
                            color = rx.color("slate", 12),),
            rx.text("Online",
                    trim="both",
                    font_size=font_size,
                    color = rx.color("slate", 12),),
        ),
        weight="bold",
        font_family="Poppins",
        
),


