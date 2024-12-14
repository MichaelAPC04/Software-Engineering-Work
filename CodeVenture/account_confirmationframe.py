import tkinter as tk
from Databases.UserDataBase import UserDataBase
from datetime import datetime
from Databases.LinkedAccountDatabase import LinkedAccountDatabase

"""
The AccountConfirmationFrame Class is used to display the confirmation of account detail and 
stores it in the userdata base 

Date: 21/10/23
Last Modified: 25/10/23
"""

class AccountConfirmationFrame(tk.Frame):
    """
    The class definition for the AccountConfirmationFrame class.
    """ 
    #initialise the UserDataBase class
    userdata_base = UserDataBase()

    #initialise the LinkedAccountDatabase class
    linking_database = LinkedAccountDatabase()

    answer_column = 1
    button_width = 20
    button_font = ("Arial Bold", 12)
    button_fg = "#f1f1ee"
    # list of account detail question 
    question = ["Username: ",
                "Email: ",
                "Password: ",
                "What was your first pet's name? ",
                "Where did you go the first time you flew on a plane? ",
                "What was your childhood nickname? ",
                "Phone number:",
                "User type:"]
    
    def __init__(self, master, user_type_frame,main_menu_frame):
       
        """
        Constructor for the AccountConfirmationFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.user_type_frame = user_type_frame
        self.main_menu_frame = main_menu_frame
        # getting user inputted details
        self.data = self.user_type_frame.get_user_info()

        # page/frame title
        confirm_label = tk.Label(self,
                                 text="Please confirm your detail:",
                                 font=("Arial Bold", 20))
        confirm_label.grid(row=0, column=0,columnspan=2, padx=10, pady=10)

        # create a label that display the account detail question 
        for i in range(len(self.question)):
            tk.Label(self,
                     text=self.question[i]).grid(row=i+1, column=0, padx=10, pady=10,sticky=tk.E)
        
        # create a label that display user inputted details
        for i in range(len(self.data)):
            if i<2:
                tk.Label(self,
                         text=self.data[i]).grid(row=i+1, column=self.answer_column, padx=10, pady=10,sticky=tk.W)
            # Display password 
            elif i ==2:
                self.password = tk.StringVar()
                self.password.set(len(self.data[i])*"●")
                tk.Label(self,
                         textvariable=self.password).grid(row=i+1, column=self.answer_column, padx=10, pady=10,sticky=tk.W)
            # Display security question 
            elif i == 3:
                # since security question is another list we need another for loop
                for a in range(len(self.data[i])):
                    tk.Label(self,
                             text=self.data[i][a]).grid(row=i+a+1, column=self.answer_column, padx=10, pady=10,sticky=tk.W)
            elif i >3:
                tk.Label(self,
                         text=self.data[i]).grid(row=i+2+1, column=self.answer_column, padx=10, pady=10,sticky=tk.W)
        
        # confirm button 
        yes_button = tk.Button(self,text="Confirm",
                               width=self.button_width,
                               font=self.button_font,
                               bg="#234f1e",
                               fg=self.button_fg,
                               command=self.store_user_data)
        yes_button.grid(row=10, column=1, padx=10, pady=10,sticky=tk.W)

        # unconfirm button 
        no_button = tk.Button(self,text="Change details",
                              width=self.button_width,
                              font=self.button_font,
                              bg="#f94449",
                              fg=self.button_fg,
                              command=self.return_to_user_type_selection)
        no_button.grid(row=10, column=0, padx=10, pady=10,sticky=tk.E)

        # button for user to display their password
        reveal_pasword_button = tk.Button(self,text="👁")
        reveal_pasword_button.grid(row=3, column=2, padx=10, pady=10,sticky=tk.W)

        # diplay passsword if and only if the button is pressed
        reveal_pasword_button.bind('<Button-1>',self.show_password)
        # hide password if the button is not pressed
        reveal_pasword_button.bind('<ButtonRelease-1>',self.hide_password)

    def show_password(self,event):
        """
        The function set "password entry" to display users password when the "reveal" button is pressed
        """
        self.password.set(self.data[2])
    
    def hide_password(self,event):
        """
        The function hide password when the "reveal" button is not pressed
        """
        self.password.set(len(self.data[2])*"●")
    
    def return_to_user_type_selection(self):
        """
        The function return user to the user type selection frame/page
        """
        self.place_forget()
        self.user_type_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def store_user_data(self):
        """
        The function store user data and return to the main menu frame/page
        """
        # get the current time
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        # append data in the userdatabase 
        self.userdata_base.create_user(self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.data[5],current_datetime)
        
        user_type = self.data[5]
        username = self.data[0]
        # add a new row of their username in the linked_account.csv if user is 
        # either educator or parents
        if user_type == "EDUCATOR" or user_type == "PARENTS":
            self.linking_database.add_new_row(username)
        self.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        
