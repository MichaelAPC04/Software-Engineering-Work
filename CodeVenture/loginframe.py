import tkinter as tk
from Databases.UserDataBase import UserDataBase
from learner import LearnerFrame
from admin import AdminFrame
from datetime import datetime
from EducatorFrame import EducatorFrame

"""
The LoginFrame Class is used to display the login page for user to 
login into CodeVenture 

Date: 21/10/23
Last Modified: 25/10/23
"""

class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """
    # initialise the UserDataBase class
    userdata_base = UserDataBase()
    def __init__(self, master, main_menu_frame):
        """
        Constructor for the LoginFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.main_menu_frame = main_menu_frame  
        
        # return to main menu button
        main_menu_button = tk.Button(self,text="Return to main menu", command=self.main_menu,font=("Arial Bold", 12))
        main_menu_button.grid(row=0, column=1, padx=10, pady=30, sticky=tk.E)

        #picture of the logo
        codeventure_logo = tk.Canvas(self,width=128, height=128)
        codeventure_logo.grid(row=1,columnspan=2,padx=10,pady=10)

        img_path = "image/Python_logo.png"
        self.login_logo = tk.PhotoImage(file = img_path)
        codeventure_logo.create_image(0, 0, image=self.login_logo)

        # welcome label
        welcome_label = tk.Label(self,
                               text="Welcome back to Codeventure! ",
                               font=("Arial Bold", 25))
        welcome_label.grid(row=2, columnspan=2, padx=10, pady=10)

        # Username label
        username_label = tk.Label(self, text="Username:")
        username_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Username entry 
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        # Password label
        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        # Password entry 
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password,
                                  show="●")
        self.password_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        # Login button
        login_button = tk.Button(self, text="Login",font=("Arial Bold", 12),command=self.verify_login)
        login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # message Label
        self.message = tk.StringVar()
        message_label = tk.Label(self,textvariable=self.message,font=("Arial Bold", 10), fg='#ff0000')
        message_label.grid(row=6, columnspan=2, padx=10, pady=10)

    def main_menu(self):
        """
        This function is used to return to main menu
        """
        self.place_forget()
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def show_educator_parent_menu(self,username,login_time):
        """
        The function display the educator/parent menu
        """
        self.place_forget()

        educator_menu = EducatorFrame(self.master,username, login_time, self.main_menu_frame)
        educator_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def verify_login(self):
        """
        The function verify user login details
        """
        # update user database
        self.userdata_base.update_user_database()
        #get username and password from the entries
        username = self.username.get()
        password = self.password.get()

        # check if username exist 
        if self.userdata_base.check_if_user_exists(username):
            # get user data 
            data = self.userdata_base.get_user(username)
            last_login_time = self.userdata_base.get_user_login_time(username)
            # get the current time
            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
            # update the last login
            self.userdata_base.update_last_login(username, current_datetime)

            # check if password matches 
            if password == data[2]:
                user_type = self.userdata_base.get_user_type(username)
                if user_type == "LEARNER":
                    display_str = "Logged in as a Learner!"
                    self.destroy() 
                    learner_frame = LearnerFrame(self.master, self.main_menu_frame, username,last_login_time)
                    learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                #
                elif user_type == "PARENTS" or user_type == "EDUCATOR":
                    display_str = "Logged in"
                    self.show_educator_parent_menu(username,last_login_time)

                elif user_type == "ADMIN":
                    display_str = "Logged in as an Admin!"
                    self.destroy() 
                    learner_frame = AdminFrame(self.master, self.main_menu_frame,username)
                    learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                
            else:
                display_str = "Password is incorect."
        else:
            display_str = "User does not exist, please register an account."
        self.message.set(display_str)


