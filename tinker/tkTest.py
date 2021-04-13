from tkinter import Tk, Text
from woth_api import WothAPI
woth_data = WothAPI.fetch()

print("1")
root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")
print("1")
text = Text(root, height=8)
text.pack()
print("1")
text.insert('1.0', woth_data['word'])#'This is a Text widget demo')
print("1")
root.mainloop()
