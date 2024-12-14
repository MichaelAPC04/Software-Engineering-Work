import tkinter as tk 
from main_menuframe import MainMenuFrame

class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=1280, height=720):
        """
        Constructor for the Interface class,
        the main window for the CodeVenture.
        :param title: str
        :param width: int - default 1280 pixels
        :param height: int - default 720 pixels
        """
        super().__init__()
        self.width = width
        self.height = height
        self.title(title)
        self.geometry(f"{width}x{height}")
if __name__ == '__main__':
    root = Interface("Codeventure")
    main_menu = MainMenuFrame(root)
    main_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.mainloop()