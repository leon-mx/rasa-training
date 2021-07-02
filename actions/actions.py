# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.database_connection import save_data
from rasa_sdk.events import UserUtteranceReverted
from actions.database_connection import save_form

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_name", usuario_name = tracker.get_slot("name"))

        return []

class ActionPhone(Action):

    def name(self) -> Text:
        return "action_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_phone", usuario_phone = tracker.get_slot("phone"))

        return []

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("name")
        user_number = tracker.get_slot("phone")
        user_age = tracker.get_slot("age")
        save_data(user_name, user_age, user_number)
        # final_message = user_name + "," + user_number + "," + user_age + "\n"
        # with open ("User_details.txt", "a") as file:
        #    file.write(final_message)
        dispatcher.utter_message(response = "utter_confirmation")

        return []


class ActionSubmitForm(Action):

    def name(self) -> Text:
        return "action_submit_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("name")
        user_number = tracker.get_slot("phone")
        user_email = tracker.get_slot("email")
        save_form(user_name, user_number, user_email)
        # final_message = user_name + "," + user_number + "," + user_age + "\n"
        # with open ("User_details.txt", "a") as file:
        #    file.write(final_message)
        dispatcher.utter_message(response = "utter_confirmation")

        return []

class FallbackResponse(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_rephrase")

        return [UserUtteranceReverted()]








# Collect the following detials from the user Name, phone number, age. Store with the slots Then save it to the slots and then store in a text file.

# "a" append mode adding data coming from multiple users

# pip install mysql-connector-python


# Socket io

# Restarted()