# Задание №3
import requests
from collections import defaultdict

from translate import Translator




# Задание №5
memory = defaultdict(list)
class TextAnalysis():
# Задание №1
    memory = {}
    def __init__(self, text, owner):

        # Задание №2
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")
        TextAnalysis.memory[owner].append(self)

        # Задание №6
        self.response = self.get_answer()

    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        # Задание №4
        except:
            return "Перевод не удался"


