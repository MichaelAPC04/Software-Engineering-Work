import tkinter as tk
from loginframe import LoginFrame
from create_accountframe import CreateAccountFrame
from ForgotPassword import ForgotPassword

"""
The MainMenuFrame Class is used to display main menu of CodeVenture

Date: 21/10/23
Last Modified: 25/10/23
"""

class MainMenuFrame(tk.Frame):
    """
    The class definition for the MainMenuFrame class.
    """
    button_height = 3
    button_width = 20
    button_font = ("Arial Bold", 12)
    button_background = '#78d6ff'

    def __init__(self, master):
        """
        Constructor for the MainMenuFrame class.
        """
        super().__init__(master=master)
        self.master = master

        # welcome label
        welcome_label = tk.Label(self,text="Welcome to CodeVenture!",
                                 font=("Arial Bold", 25))
        welcome_label.grid(row=1,column=0,padx=10,pady=10)

        #Button to go to login page
        login_button = tk.Button(self,text="Login",
                                 height = self.button_height,
                                 width = self.button_width,
                                 activebackground= self.button_background,
                                 font=self.button_font,
                                 command=self.show_login_frame)
        login_button.grid(row=2,column=0,padx=10,pady=10)

        #Button to go to create account page
        create_acc_button = tk.Button(self,text="Create new account",
                                      height = self.button_height,
                                      width = self.button_width,
                                      activebackground= self.button_background,
                                      font=self.button_font,
                                      command=self.show_create_account_frame)
        create_acc_button.grid(row=3,column=0,padx=10,pady=10)

        #Button for forgot password
        forgot_password_button = tk.Button(self,text="Forgot password",
                                           height = self.button_height,
                                           width = self.button_width,
                                           activebackground= self.button_background,
                                           font=self.button_font,
                                           command=self.show_forgot_password_frame)
        forgot_password_button.grid(row=4,column=0,padx=10,pady=10)

        #Button for exiting
        exit_button = tk.Button(self,text="Exit",
                                height = self.button_height,
                                width = self.button_width,
                                activebackground= self.button_background,
                                font=self.button_font,
                                command=self.exit_confirmation_popup)
        exit_button.grid(row=5,column=0,padx=10,pady=10)

        self.all_button = [login_button, create_acc_button, forgot_password_button, exit_button]

    def show_login_frame(self):
        """
        This function is used to display the login page frame
        """
        self.place_forget()
        login_frame = LoginFrame(self.master, self)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_create_account_frame(self):
        """
        This function is used to display the create account page frame
        """
        self.place_forget()
        create_account_frame = CreateAccountFrame(self.master, self)
        create_account_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_forgot_password_frame(self):
        """
        This function is used to display the forgot pasword page frame
        """
        self.place_forget()
        forgot_password_frame = ForgotPassword(self.master, self)
        forgot_password_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def exit_confirmation_popup(self,width=300,height=100):
        """
        This function display a popup to confirm if user wants to exit the program.
        """
        # disable all button
        # we dont want user clicking on the main window button while popup is displayed
        for button in self.all_button:
            button['state'] = tk.DISABLED

        # create popout
        popup = tk.Toplevel(self)
        popup.geometry(f"{width}x{height}")
        popup.title("Exiting confirmation")

        #get upper left corner coordinate of the main window
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        
        # get the midpoint of the main window and the popup
        mid_width = int((self.master.width - width)/2)
        mid_height = int((self.master.height - height)/2)
        
        #popup is display on the middle of the main window
        popup.geometry(f"+{x+mid_width}+{y+mid_height}")

        button_width = int(width/20)

        popup_label = tk.Label(popup,text="Exit?",font=("Arial Bold", 20))
        confirm_label = tk.Label(popup,text="Are you sure you want to exit?")
        exit_confirm_button = tk.Button(popup,text="Exit",width=button_width,command=self.exit_program)
        cancel_button = tk.Button(popup,text="Cancel",width=button_width,command=lambda:self.cancel_exit(popup))

        popup_label.grid(row=1,column=0,padx=20,pady=1,sticky=tk.W)
        confirm_label.grid(row=2,column=0,columnspan=2,padx=20,pady=1,sticky=tk.W)
        exit_confirm_button.grid(row=3,column=0,padx=10,pady=10,sticky=tk.E)
        cancel_button.grid(row=3,column=1,padx=10,pady=10,sticky=tk.W)

        #if popup is closed enable exit button
        popup.protocol("WM_DELETE_WINDOW",lambda:self.cancel_exit(popup))

    def exit_program(self):
        """
        This function is used to exit the program
        """
        self.quit()

    def cancel_exit(self,popup):
        """
        This function is called when user cancel their exit of the program,
        It enable all the buttons and closes the popup
        """
        # change button state to normal
        for button in self.all_button:
            button['state'] = tk.NORMAL
        # close popout
        popup.destroy()