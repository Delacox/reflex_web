import reflex as rx
from reflex_web.components.logo import logo
from reflex_web.components.dark_mode import dark_mode_toggle


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["start", "start", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "RESOURCES", size="4", weight="bold", as_="h3"
        ),
        footer_item("Blog", "/#"),
        footer_item("Case Studies", "/#"),
        footer_item("Whitepapers", "/#"),
        footer_item("Webinars", "/#"),
        footer_item("E-books", "/#"),
        spacing="4",
        text_align=["start", "start", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.divider(
            width="80%",
            align="center",
            margin_x="auto",
            margin_y="2em",
            ),
        rx.container(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            logo(font_size="1em"),
                            
                        ),
                        rx.text(
                            "© 2024 Tu informático Online",
                            size="3",
                            white_space="nowrap",
                            weight="medium",
                        ),
                        dark_mode_toggle(),
                        spacing="4",
                        align_items=[
                            "start",
                            "start",
                            "start",
                        ],
                    ),
                    footer_items_1(),
                    footer_items_2(),
                    justify="between",
                    spacing="6",
                    flex_direction=["column", "column", "row"],
                    width="100%",
                ),
                rx.divider(),
                rx.hstack(
                    rx.hstack(
                        footer_item("Privacy Policy", "/#"),
                        footer_item("Terms of Service", "/#"),
                        spacing="4",
                        align="center",
                        width="100%",
                    ),
                    socials(),
                    justify="between",
                    width="100%",
                ),
                spacing="5",
                width="80%",
                margin_x="auto",
            ),
            size="4",
            margin_x="auto",
        ),
        width="100%",
        padding_y="1em",
        margin_x="auto",
        background=rx.color_mode_cond(
            light="#E0E4DB",
            dark="linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(37,36,36,1) 61%, rgba(36,36,36,1) 64%, rgba(38,38,38,1) 81%, rgba(17,17,17,1) 100%, rgba(214,241,227,1) 100%);"
        ),
    )