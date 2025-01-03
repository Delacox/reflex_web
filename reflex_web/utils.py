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


# Contact
contact_title = "Contacto | Tu Informático Online"
contact_description = "Contacto Servicios profesionales de informática y tecnología"
contact_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
contact_meta.extend(_meta)