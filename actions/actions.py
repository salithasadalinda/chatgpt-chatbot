# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from typing import Text, Dict, Any, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction

# class ActionProductInfo(Action):
#     def name(self) -> Text:
#         return "action_product_info"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # Extract the product entity from the tracker
#         product = tracker.get_slot("product")

#         # Hardcoded product_price for demonstration purposes
#         product_price = 100

#         # Formulate the response
#         response = f"{product} is priced at ${product_price}."

#         # Send the response to the user
#         dispatcher.utter_message(response)

#         return []

import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProductInfo(Action):
    def name(self) -> Text:
        return "action_product_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the product entity from the tracker
        product = tracker.get_slot("product")

        # Load product information from the JSON file
        with open("products.json", "r") as file:
            products_data = json.load(file)

        # Get the product details from the JSON file
        product_details = products_data.get(product, {})
        product_price = product_details.get("price", "unknown")

        # Respond with the product information
        response = f"{product} is priced at ${product_price}."
        dispatcher.utter_message(response)

        return []
