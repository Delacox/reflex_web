import reflex as rx

class FormState(rx.State):
    form_data: dict = {}
    error_terms: bool = False
    
    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        # Si no está marcado => mostramos error
        if not self.form_data.get("terms"):
            self.error_terms = True
            return
        # Si está marcado => limpiamos error
        self.error_terms = False
        return rx.window_alert(str(self.form_data))

def simple_form():
    return rx.form(
        rx.vstack(
            rx.form.field(
                rx.form.label("Nombre"),
                rx.form.control(
                    rx.input(
                        placeholder="Tu nombre",
                        name="name",
                        required=True,
                    ),
                    as_child=True,
                ),
                rx.form.message(
                    "El nombre es obligatorio",
                    match="valueMissing",
                ),
                name="name",
            ),
            rx.form.field(
                rx.form.label("Email"),
                rx.form.control(
                    rx.input(
                        placeholder="Tu email",
                        name="email",
                        type="email",
                        required=True,
                    ),
                    as_child=True,
                ),
                rx.form.message(
                    "Por favor ingresa un email válido",
                    match="typeMismatch",
                ),
                rx.form.message(
                    "Email is required",
                    match="valueMissing",
                ),
                name="email",
            ),
            rx.form.field(
                rx.form.label("Acepto los términos"),
                rx.checkbox(name="terms", value="accepted"),
                rx.form.message(
                    "Debes aceptar los términos",
                    force_match=FormState.error_terms,
                ),
                name="terms",
            ),
            rx.button(
                "Enviar",
                type="submit",
            ),
            spacing="4",
        ),
        on_submit=FormState.handle_submit,
        reset_on_submit=True,
    )
