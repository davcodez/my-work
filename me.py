import tkinter as tk
from tkinter import ttk

class App:
    def _init_(self):
        self.root = tk.Tk()
        self.root.geometry('350x200')
        self.root.title('BG APP')
        self.mainframe = tk.Frame(self.root, background='ivory')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='''BG's APP Welcomes you to the world of possibilities!
        Are you ready to embark on a journey of love, laughter, and unforgettable connections?
        Our dating app is here to ignite the spark and help you find that special someone
        who will make your heart skip a beat. Join us today and let the adventure begin!''',
                              background='ivory', font=('Brass mono', 12))

        self.text.grid(row=0, column=0, padx=10, pady=10)
        self.root.mainloop()

if __name__ == '_main_':
    App()