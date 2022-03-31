# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from tkinter import Button
from turtle import title
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher


class ActionService(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/hero', "title": "Hemophilia"},
            {"payload":'/hero', "title": "A, Hemophilia"},
            {"payload":'/hero', "title": "Abdominal Aortic Aneurysm"},
            {"payload":'/hero', "title": "Scar Tissue"},
            {"payload":'/hero', "title": "Heat Cramps"},
            {"payload":'/hero', "title": "Abdominal Cramps"},
            {"payload":'/hero', "title": "Tummy Tuck"},
            {"payload":'/hero', "title": "Infertility"},
            {"payload":'/hero', "title": "Bite, Snake"},
            {"payload":'/hero', "title": "Biventricular Pacemaker"},
            {"payload":'/hero', "title": "Foot Problems, Diabetes"},
            {"payload":'/hero', "title": "Diabetes Foot Problems"},
            {"payload":'/hero', "title": "Foot, Broken"},
            {"payload":'/hero', "title": "Foot, Gangrene"},
            {"payload":'/hero', "title": "Head Injury"},
            {"payload":'/hero', "title": "Head Lice"},
            {"payload":'/hero', "title": "Headache"},
            {"payload":'/hero', "title": "Sinus Headache"},
            {"payload":'/hero', "title": "Headache, Sinus"},
            {"payload":'/hero', "title": "Spinal Headaches"},
            {"payload":'/hero', "title": "Wrestler's Ear"},
            {"payload":'/hero', "title": "Wrestlers' Herpes"},
            {"payload":'/hero', "title": "Wrinkles"},
            {"payload":'/hero', "title": "Yeast Infections"},
            {"payload":'/hero', "title": "Yeast Vaginitis"},
            {"payload":'/hero', "title": "Yeast, Oral"},
            {"payload":'/hero', "title": "Oral Yeast"},
            {"payload":'/hero', "title": "Yellow Fever"},
            {"payload":'/hero', "title": "Yellow Poop"},
            {"payload":'/hero', "title": "Yellow Stools"},
            {"payload":'/hero', "title": "Younger Children, Sleep"},
            {"payload":'/hero', "title": "Sleep Younger Children"},
            {"payload":'/hero', "title": "Zygote Intrafallopian Transfer"}
        ]
        dispatcher.utter_message(text="In Which disease you are in? ",buttons=buttons)

        return []


class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conversation=tracker.events
        import os
        if not os.path.isfile('chats.csv'):
            with open('chats.csv','w') as file:
                file.write("user_input,bot_reply\n")
        chat_data=''
        for i in conversation:
            
            if i["event"]=="user":
                chat_data+=i['text']+','

            elif i['event']=='bot':
                try:
                    chat_data+=i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.csv', 'a', encoding="utf-8") as file:
                file.write(chat_data)

        dispatcher.utter_message()

        return []