from tkinter import *
#https://docs.python.org/3/library/tkinter.html
from woth_api import WothAPI

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Python Tkinter")
        self.minsize(500, 400)
    
    def generate_text(self):
        word_data = WothAPI.fetch()
        self.word = word_data['word']
        self.text = self.word
        self.definitions = word_data['definitions']['english']
        for definition in self.definitions:
            self.text += "\n " + definition + "\n"
        self.translations = word_data['translations']
        self.text += "\n"
        for language, translation in self.translations.items():
            self.text += " " + language + ": " + translation + "\n"

    def insert_text_into_window(self):
        self.textWindow = Text(root, height=10)
        self.textWindow.pack()
        self.textWindow.insert('2.0', self.text)


root = Root()
root.generate_text()
print(root.text)
root.insert_text_into_window()
print(root.text)
root.mainloop()

