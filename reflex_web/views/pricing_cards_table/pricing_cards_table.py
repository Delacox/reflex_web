import reflex as rx
from reflex_web.components.pricing_cards.pricing_card_basic import pricing_card_basic
from reflex_web.components.pricing_cards.pricing_card_advanced import pricing_card_avanced
#from reflex_web.components.pricing_cards.pricing_card_premium import pricing_card_premium

def pricing_cards_table() -> rx.Component:
    return rx.box(
        rx.flex(
            pricing_card_basic(),
            pricing_card_avanced(),
            pricing_card_basic(),
            spacing="4",
            width="100%",
            justify="center", # Recuerda con el flex centramos con justify
            align_items="center",
            flex_direction=["column", "column", "row"],
        ),
        width="90%",
        margin_x="auto",
        
        
    )
