from ikea_api import IkeaApi
from emilio import send_email

api = IkeaApi(
    token=...,  # If you already have a token and stored it somewhere
    country_code="us",
    language_code="en",
)

api.login_as_guest()

cart = api.Cart
# print(cart.show())
try:
    # Vallentuna hillared dark grey Cushion
    cart.add_items({"s59149810": 1})
    api.OrderCapture(zip_code="02215", state_code="ma")
    send_email("Vallentuna hillared dark grey cushion")

except Exception as ex:
    print("Something went wrong...", ex)


try:
    # Vallentuna hillared dark grey cover
    cart.add_items({"30329519": 1})
    api.OrderCapture(zip_code="02215", state_code="ma")
    send_email("Vallentuna hillared dark grey cover")

except Exception as ex:
    print("Something went wrong...", ex)
