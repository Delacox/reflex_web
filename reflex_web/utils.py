import reflex as rx

# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'") # Idioma de la pagina

preview = "/preview.jpg"

_meta=[
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "keywords", "content": "informático,servicios,tecnología"},
    {"name": "robots", "content": "index, follow"},
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
]


# index
index_title = "Inicio | Tu Informático Online"
index_description = "Servicios profesionales de informática y tecnología"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)


# About us
about_us_title = "Nosotros | Tu Informático Online"
about_us_description = "Nosotros Servicios profesionales de informática y tecnología"
about_us_meta = [
    {"name": "og:title", "content": about_us_title},
    {"name": "og:description", "content": about_us_description},
]
about_us_meta.extend(_meta)

# Prices
prices_title = "Precios | Tu Informático Online"
prices_description = "Precios Servicios profesionales de informática y tecnología"
prices_meta = [
    {"name": "og:title", "content": prices_title},
    {"name": "og:description", "content": prices_description},
]
prices_meta.extend(_meta)

# Contact
contact_title = "Contacto | Tu Informático Online"
contact_description = "Contacto Servicios profesionales de informática y tecnología"
contact_meta = [
    {"name": "og:title", "content": contact_title},
    {"name": "og:description", "content": contact_description},
]
contact_meta.extend(_meta)

# Signup
signup_title = "Registro | Tu Informático Online"
signup_description = "Registro Servicios profesionales de informática y tecnología"
signup_meta = [
    {"name": "og:title", "content": signup_title},
    {"name": "og:description", "content": signup_description},
]
signup_meta.extend(_meta)

# Login
login_title = "Login | Tu Informático Online"
login_description = "Login Servicios profesionales de informática y tecnología"
login_meta = [
    {"name": "og:title", "content": login_title},
    {"name": "og:description", "content": login_description},
]
login_meta.extend(_meta)