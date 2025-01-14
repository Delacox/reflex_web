import reflex as rx

class ContactFormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        return rx.window_alert(str(form_data))

def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )




def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="green",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Envianos un mensaje",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Rellena el formulario para contactar con nosotros",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Nombre",
                            "Nombre",
                            "text",
                            "nombre",
                        ),
                        form_field(
                            "Apellidos",
                            "Apellidos",
                            "text",
                            "apellidos",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Email",
                            "user@tuinformatico.online",
                            "email",
                            "email",
                        ),
                        form_field(
                            "Telefono", "Telefono", "tel", "telefono"
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje",
                            style={
                                "fontSize": "15px",
                                "fontWeight": "500",
                                "lineHeight": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Mensaje",
                            name="mensaje",
                            resize="vertical",
                        ),
                        
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.field(
                        rx.flex(
                            rx.checkbox(
                                "Acepto la política de privacidad",
                                name="politica",
                                required=True
                            ),
                            rx.form.message(
                                "Debes aceptar la política de privacidad",
                                match="valueMissing",
                                force_match=False,
                                color="var(--red-11)"
                            ),
                            direction="column",
                            spacing="2",
                        ),
                        name="politica",
                        server_invalid=False
                    ),
                    rx.form.submit(
                        rx.button("Enviar"),
                        as_child=True,
                        
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),

                on_submit=ContactFormState.handle_submit,
                reset_on_submit=True
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )