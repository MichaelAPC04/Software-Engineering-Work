import tkinter as tk
from user_typeframe import UserTypeFrame
from Databases.UserDataBase import UserDataBase
import re

"""
The CreateAccountFrame Class is used to display entries for user to enter details for them
to create an account.

Date: 21/10/23
Last Modified: 25/10/23
"""

class CreateAccountFrame(tk.Frame):
    """
    The class definition for the CreateAccountFrame class.
    """
    # Initialise the UserDataBase class
    userdata_base = UserDataBase()
    # list of security question 
    security_question = ["What was your first pet's name? ",
                        "Where did you go the first time you flew on a plane? ",
                        "What was your childhood nickname? "]
    # width of all the entry in CreateAccountFrame
    entry_width = 30
    def __init__(self, master, main_menu_frame):
        """
        Constructor for the CreateAccountFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.main_menu_frame = main_menu_frame  

        # return to main menu button
        main_menu_button = tk.Button(self,text="Return to main menu",
                                     activebackground="#ffc6c4",
                                     command=self.main_menu,font=("Arial Bold", 12))
        main_menu_button.grid(row=1, column=1, padx=10, pady=40, sticky=tk.E)

        # create account label 
        acc_label = tk.Label(self,text="Create your account",font=("Arial Bold", 20))
        acc_label.grid(row=1, column=0, padx=10, pady=40, sticky=tk.E)

        # email label
        email_label = tk.Label(self,text="Email address:")
        email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        
        # email entry
        self.email = tk.StringVar() 
        email_entry = tk.Entry(self, width=self.entry_width,textvariable=self.email)
        email_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # email confirmation label
        email_confirm_label = tk.Label(self,text="Confirm email address:")
        email_confirm_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        
        # email confirmation entry 
        self.confirm_email = tk.StringVar() 
        email_confirm_entry = tk.Entry(self, width=self.entry_width,textvariable=self.confirm_email)
        email_confirm_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # phone number label
        phone_num_label = tk.Label(self,text="Phone number:")
        phone_num_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)
        
        # phone number entry
        self.phone_number = tk.StringVar() 
        phone_num_entry = tk.Entry(self, width=self.entry_width,textvariable=self.phone_number)
        phone_num_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W,)

        # username label
        username_label = tk.Label(self,text="Username:")
        username_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)
        
        # username entry 
        self.username = tk.StringVar() 
        username_entry = tk.Entry(self, width=self.entry_width,textvariable=self.username)
        username_entry.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

        # password label
        password_label = tk.Label(self,text="Password:")
        password_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)
        
        # password entry 
        self.password = tk.StringVar()
        password_entry = tk.Entry(self, width=self.entry_width,textvariable=self.password,show="●")
        password_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

        # password confirmation label
        password_confirm_label = tk.Label(self,text="Confirm password:")
        password_confirm_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)
        
        # password confirmation entry 
        self.confirm_password = tk.StringVar()
        password_confirm_entry = tk.Entry(self, width=self.entry_width,textvariable=self.confirm_password,show="●")
        password_confirm_entry.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)
        
        # loop through security_question and create label with each element 
        for i in range(len(self.security_question)):
            # all question label
            question_label = tk.Label(self,text=self.security_question[i])
            question_label.grid(row=8+i, column=0, padx=10, pady=10, sticky=tk.E)
            
        # first question entry 
        self.first_answer = tk.StringVar()
        first_question_entry = tk.Entry(self,textvariable=self.first_answer, width=self.entry_width)
        first_question_entry.grid(row=8, column=1, padx=10, pady=10, sticky=tk.W)

        # second question entry 
        self.second_answer = tk.StringVar()
        second_question_entry = tk.Entry(self,textvariable=self.second_answer, width=self.entry_width)
        second_question_entry.grid(row=9, column=1, padx=10, pady=10, sticky=tk.W)

        # third question entry 
        self.third_answer = tk.StringVar()
        third_question_entry = tk.Entry(self,textvariable=self.third_answer, width=self.entry_width)
        third_question_entry.grid(row=10, column=1, padx=10, pady=10, sticky=tk.W)

        #create account button
        acc_button = tk.Button(self,text="Next",
                                width=self.entry_width,
                                activebackground='#78d6ff',
                                font=("Arial Bold", 12),
                                command=self.verify_entry)
        acc_button.grid(row=8+len(self.security_question)+1,columnspan=2, column=0, padx=10, pady=10, sticky=tk.E)

        # message Label
        self.message = tk.StringVar()
        message_label = tk.Label(self,textvariable=self.message,font=("Arial Bold", 10), fg='#ff0000')
        message_label.grid(row=8+len(self.security_question)+2, column=0, columnspan=2, padx=10, pady=10)
    
    def verify_email(self,email):
        #https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        """
        check if email entry follows the email format 
        """
        # Make a regular expression for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False
        
    def verify_phone_number(self,phone_number):
        # https://stackoverflow.com/questions/14894899/what-is-the-minimum-length-of-a-valid-international-phone-number
        # the minimum phone number length is 5 and max is 15
        """
        check if the length of phone number is between 5 and 15 
        """
        length = len(phone_number)
        if length >= 5 and length <=15:
            return True
        else:
            return False
    
    def verify_password(self,password):
        """
        check if the length of phone number is greater 8  
        """
        length = len(password)
        if length >= 8:
            return True
        else:
            return False

    def verify_entry(self):
        """
        This function is used verify confirmation entry and saved user entry data
        """
        email = self.email.get()
        confirm_email = self.confirm_email.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        username = self.username.get()
        phone_number = self.phone_number.get()
        security_answer = [self.first_answer.get(),self.second_answer.get(),self.third_answer.get()]
        self.current_user_data = [username,email,password,security_answer,phone_number]
        # all the entry is filled
        if (email and confirm_email and password and username and phone_number and security_answer):
            if (email == confirm_email 
                and password == confirm_password 
                and not(self.userdata_base.check_if_user_exists(username))
                and self.verify_email(email)
                and self.verify_phone_number(phone_number)
                and self.verify_password(password)):
                display_str = ""
                self.show_select_user_type()
            elif not(email == confirm_email and password == confirm_password):
                display_str = "Email or/and password does not match!"
            elif self.userdata_base.check_if_user_exists(username):
                display_str = "Username already exist, please try another username!"
            elif not(self.verify_email(email)):
                display_str = "Invalid email address"
            elif not(self.verify_phone_number(phone_number)):
                display_str = "Invalid phone number"
            elif not(self.verify_password(password)):
                display_str = "Password must be have at least 8 characters"
        # there is a empty entry
        else:
            display_str = "Please fill all of the details"
        self.message.set(display_str)
    
    def main_menu(self):
        """
        This function is used to return to main menu
        """
        self.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_select_user_type(self):
        """
        This function is used to display user type selection page frame
        """
        self.place_forget()
        user_type_frame = UserTypeFrame(self.master,self)
        user_type_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    

