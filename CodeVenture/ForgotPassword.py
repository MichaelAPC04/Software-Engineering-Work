import tkinter as tk
from ast import literal_eval

from Databases.UserDataBase import UserDataBase

"""
This is the ForgotPassword class. It is responsible for allowing a user of CodeVenture to change their password if they
forget it. A user's data is directly accessed and updated when needed within the "user_data.csv" file.

Author: Michael APC
Date: 20/10/23
Version: 1.2.0
Last Modified: 23/10/23
"""


class ForgotPassword(tk.Frame):
    """
    Class definition for the ForgotPassword class.
    """

    # Font for the normal text.
    text_font = font = ("Arial Bold", 13)

    def __init__(self, master, main_menu_frame):
        """
        Constructor for the ForgotPassword class.
        """
        super().__init__(master=master)
        self.reset_password_input_result = None
        self.reset_password_string_input = None
        self.reset_password_input = None
        self.phone_input_result = None
        self.phone_number_string_input = None
        self.phone_number_input = None
        self.question_three_string_input = None
        self.question_three_input = None
        self.question_two_string_input = None
        self.question_two_input = None
        self.question_one_string_input = None
        self.question_one_input = None
        self.frame = tk.Frame(self.master)
        self.email_string_input = None
        self.email_input_result = None
        self.email_input = None
        self.master = master
        self.main_menu_frame = main_menu_frame
        self.db_user = UserDataBase()
        self.user_data = []

        # Return to main menu button.
        main_menu_button = tk.Button(self, text="Return to main menu", command=self.main_menu, font=("Arial Bold", 10))
        main_menu_button.grid(row=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        # Forgot password widget title label.
        forgot_password_label = tk.Label(self, text="Forgot Password", font=("Arial Bold", 15))
        forgot_password_label.grid(row=1, columnspan=2, padx=10, pady=10, sticky=tk.N)

        # Username label and input.
        username_input = tk.Label(self, text="Please enter your username:", font=self.text_font)
        username_input.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.username = tk.StringVar()
        self.username_string_input = tk.Entry(master=self, textvariable=self.username)
        self.username_string_input.grid(row=2, column=1, sticky=tk.E, padx=10, pady=10)
        username_button = tk.Button(self, text="Enter", command=self.username_verification, font=("Arial Bold", 10))
        username_button.grid(row=3, columnspan=2, sticky=tk.S, padx=10, pady=10)
        self.username_string_input_result = tk.Label(master=self)
        self.username_string_input_result.grid(row=4, columnspan=2, padx=10, pady=10)

    def username_verification(self):
        username = self.username.get()
        user_data = self.db_user.get_user(username)
        if len(user_data) > 0:   # If the user data exists, move onto the next stage, email verification.
            self.user_data = user_data
            self.email_verification()
        else:
            self.username_string_input_result.config(text="Username verification failed, please try again."
                                                          "\nOr call customer support at: 703-482-0623.",
                                                     font=("Arial Bold", 10), fg="#ff0000")

    def main_menu(self):
        """
        Function to return to the main menu.
        """
        if self.frame.winfo_viewable():
            self.frame.place_forget()   # For all other frames that are not the first frame.
        else:
            self.place_forget()   # For the first frame.

        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def email_verification(self):
        for widget in self.master.winfo_children():
            widget.place_forget()   # Forget previous frame (this is used in all the following frames/ methods).

        self.frame = tk.Frame(self.master)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Return to main menu button.
        main_menu_button = tk.Button(self.frame, text="Return to main menu", command=self.main_menu,
                                     font=("Arial Bold", 10))
        main_menu_button.pack(pady=10)

        # User email entry.
        email_label = tk.Label(self.frame, text="Please enter your email:", font=self.text_font)
        email_label.pack(pady=10)
        self.email_input = tk.StringVar()
        self.email_string_input = tk.Entry(master=self.frame, textvariable=self.email_input)
        self.email_string_input.pack(pady=10)
        email_button = tk.Button(self.frame, text="Enter", command=self.email_check, font=("Arial Bold", 10))
        email_button.pack(pady=10)
        self.email_input_result = tk.Label(master=self.frame)
        self.email_input_result.pack(pady=10)

    def email_check(self):
        if self.email_input.get() == str(self.user_data[1]):  # Check if email input matches existing email in database.
            self.question_verification()   # If successful, move onto the next stage, question verification.
        else:
            self.email_input_result.config(text="Email verification failed, please try again.\nOr call customer "
                                                "support at: 703-482-0623.", font=("Arial Bold", 10), fg="#ff0000")

    def question_verification(self):
        for widget in self.master.winfo_children():
            widget.place_forget()

        self.frame = tk.Frame(self.master)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Return to main menu button.
        main_menu_button = tk.Button(self.frame, text="Return to main menu", command=self.main_menu,
                                     font=("Arial Bold", 10))
        main_menu_button.pack(pady=10)

        # Q1 entry.
        question_one_label = tk.Label(self.frame, text="What was your first pet's name?", font=self.text_font)
        question_one_label.pack(pady=10)
        self.question_one_input = tk.StringVar()
        self.question_one_string_input = tk.Entry(master=self.frame, textvariable=self.question_one_input)
        self.question_one_string_input.pack(pady=10)

        # Q2 entry.
        question_two_label = tk.Label(self.frame, text="Where did you go the first time you flew on a plane?",
                                      font=self.text_font)
        question_two_label.pack(pady=10)
        self.question_two_input = tk.StringVar()
        self.question_two_string_input = tk.Entry(master=self.frame, textvariable=self.question_two_input)
        self.question_two_string_input.pack(pady=10)

        # Q3 entry.
        question_three_label = tk.Label(self.frame, text="What was your childhood nickname?", font=self.text_font)
        question_three_label.pack(pady=10)
        self.question_three_input = tk.StringVar()
        self.question_three_string_input = tk.Entry(master=self.frame, textvariable=self.question_three_input)
        self.question_three_string_input.pack(pady=10)

        question_button = tk.Button(self.frame, text="Enter", command=self.verify_question,
                                    font=("Arial Bold", 10))
        question_button.pack(pady=10)

    def verify_question(self):
        # Check if Q1,2,3 inputs match existing answers in database, move onto the reset pw stage if successful.
        animal_lst = literal_eval(str(self.user_data[3]))
        if [self.question_one_input.get(), self.question_two_input.get(),
                self.question_three_input.get()] == animal_lst:
            self.reset_password()
        else:
            self.phone_verification()   # If unsuccessful, move onto the phone verification stage.

    def phone_verification(self):
        for widget in self.master.winfo_children():
            widget.place_forget()

        self.frame = tk.Frame(self.master)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Return to main menu button.
        main_menu_button = tk.Button(self.frame, text="Return to main menu", command=self.main_menu,
                                     font=("Arial Bold", 10))
        main_menu_button.pack(pady=10)

        # Phone number entry.
        phone_number_label = tk.Label(self.frame, text="Please enter your phone number:", font=self.text_font)
        phone_number_label.pack(pady=10)

        self.phone_number_input = tk.StringVar()
        self.phone_number_string_input = tk.Entry(master=self.frame, textvariable=self.phone_number_input)
        self.phone_number_string_input.pack(pady=10)
        phone_number_button = tk.Button(self.frame, text="Enter", command=self.phone_number_check,
                                        font=("Arial Bold", 10))
        phone_number_button.pack(pady=10)
        self.phone_input_result = tk.Label(master=self.frame)
        self.phone_input_result.pack(pady=10)

    def phone_number_check(self):
        string_phone_number = self.phone_number_input.get()
        try:
            integer_phone_number = int(string_phone_number)   # Only integers can be inputted.
        except ValueError:
            self.phone_input_result.config(text="Invalid input, please enter a valid phone number.",
                                           font=("Arial Bold", 10), fg="#ff0000")
            return

        if integer_phone_number == int(self.user_data[4]):
            self.reset_password()   # If phone input matches existing data in database, user can now reset pw.
        else:
            self.phone_input_result.config(text="Phone number verification failed, please try again.\nOr call customer "
                                                "support at: 703-482-0623.", font=("Arial Bold", 10), fg="#ff0000")

    def reset_password(self):
        for widget in self.master.winfo_children():
            widget.place_forget()

        self.frame = tk.Frame(self.master)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Return to main menu button.
        main_menu_button = tk.Button(self.frame, text="Return to main menu", command=self.main_menu,
                                     font=("Arial Bold", 10))
        main_menu_button.pack(pady=10)

        # New password entry for reset.
        reset_password_label = tk.Label(self.frame, text="Please enter your new password:", font=self.text_font)
        reset_password_label.pack(pady=10)
        self.reset_password_input = tk.StringVar()
        self.reset_password_string_input = tk.Entry(master=self.frame, textvariable=self.reset_password_input)
        self.reset_password_string_input.pack(pady=10)
        reset_password_button = tk.Button(self.frame, text="Enter",
                                          command=self.update_password, font=("Arial Bold", 10))
        reset_password_button.pack(pady=10)
        self.reset_password_input_result = tk.Label(master=self.frame)
        self.reset_password_input_result.pack(pady=10)

    def update_password(self):
        new_password = self.reset_password_input.get()
        if len(new_password) >= 8:   # Minimum len if new pw.
            self.db_user.update_password_on_username(self.username.get(), new_password)   # Update the pw in database.
            self.reset_password_input_result.config(text="Records successfully updated!\nPlease return to the"
                                                         " main menu.",
                                                    font=("Arial Bold", 10), fg="#008000")
        else:
            self.reset_password_input_result.config(text="Password must be at least have 8 characters",
                                                    font=("Arial Bold", 10), fg="#ff0000")
