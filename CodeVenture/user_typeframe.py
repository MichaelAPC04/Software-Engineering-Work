import tkinter as tk 
from account_confirmationframe import AccountConfirmationFrame

"""
The UserTypeFrame Class is used to display the selection for the 
different user types.

Date: 21/10/23
Last Modified: 25/10/23
"""

class UserTypeFrame(tk.Frame):
    """
    The class definition for the UserTypeFrame class.
    """
    img_size = 200 
    img_path = [
            "image/learner_img_resize.png",
            "image/parent_img_resize.png",
            "image/educator_img_resize.png"
        ]
    img = []
    button_row = 2
    button_background = '#78d6ff'
    user_type_list = ["LEARNER","PARENTS","EDUCATOR"]
    user_type = None

    def __init__(self, master, create_account_frame):
        """
        Constructor for the UserTypeFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.create_account_frame = create_account_frame 
        
        for path in self.img_path:
            tk_img = tk.PhotoImage(file = path)
            self.img.append(tk_img)

        # page title
        user_type_label = tk.Label(self,text="User Type",font=("Arial Bold", 20))
        user_type_label.grid(row=1,column=0, padx=10, pady=40)

        # Return to account details
        acc_button = tk.Button(self,text="Change account details",
                               font=("Arial Bold", 12),
                               activebackground="#ffc6c4",
                               command=self.return_to_account_info)
        acc_button.grid(row=1, column=2, padx=10, pady=40)
        
        # learner button
        learner_button = tk.Button(self,image=self.img[0],
                                   activebackground= self.button_background,
                                   command=lambda:[self.set_learner(),self.show_account_confirmation()])
        learner_button.grid(row=self.button_row, column=0, padx=10, pady=10)

        # parent button
        parent_button = tk.Button(self,image=self.img[1],
                                  activebackground= self.button_background,
                                  command=lambda:[self.set_parent(),self.show_account_confirmation()])
        parent_button.grid(row=self.button_row, column=1, padx=10, pady=10)

        # educator button
        educator_button = tk.Button(self,image=self.img[2],
                                    activebackground= self.button_background,
                                    command=lambda:[self.set_educator(),self.show_account_confirmation()])
        educator_button.grid(row=self.button_row, column=2, padx=10, pady=10)

        # user type label 
        for i in range(len(self.user_type_list)):
            tk.Label(self,
                     text=self.user_type_list[i],
                     font=("Arial Bold", 10)).grid(row=self.button_row+1,
                                                    column=i,
                                                    padx=10,
                                                    pady=10)
    
    def show_account_confirmation(self):
        """
        The function is used to displa the account confirmation frame/page
        """
        self.place_forget()
        account_confirm_frame = AccountConfirmationFrame(self.master,self,self.create_account_frame.main_menu_frame)
        account_confirm_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def return_to_account_info(self):
        """
        The function is used to return to the create account frame/page
        """
        self.place_forget()
        self.create_account_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
   
    def set_learner(self):
        """
        The function set the user_type to learner
        """
        self.user_type = self.user_type_list[0]
    
    def set_parent(self):
        """
        The function set the user_type to parent
        """
        self.user_type = self.user_type_list[1]
    
    def set_educator(self):
        """
        The function set the user_type to educator 
        """
        self.user_type = self.user_type_list[2]

    def get_user_info(self):
        """
        The function is used to return user details 
        """
        data = self.create_account_frame.current_user_data+[self.user_type]
        return data
        