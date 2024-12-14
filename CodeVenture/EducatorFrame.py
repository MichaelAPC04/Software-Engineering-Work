import tkinter as tk
from Databases.UserDataBase import UserDataBase
from ClassFiles.Educator import Educator
from Databases.LinkedAccountDatabase import LinkedAccountDatabase
from Databases.ModuleDatabase import ModuleDatabase
import ast

"""
Created: 25/10/2023
Last Modified: 30/10/2023
Description: Educator frame used for tracking and adding children 
"""
class EducatorFrame(tk.Frame):
    """
    The class definition for the EducatorFrame class.
    """
    def __init__(self, master, educator_username, login_time, main_menu_frame):
        """
        Constructor for the EducatorFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.main_menu_frame = main_menu_frame

        # Creating db
        db = UserDataBase()
        data = db.get_user(educator_username)

        # Extracting user data
        username = data[0]
        email = data[1]
        password = data[2]
        securityAnswer = data[3]
        phoneNumber = data[4]

        # Instantiating educator class
        self.educator = Educator(username, email, password, securityAnswer, phoneNumber)



        # Welcome label
        welcome_label = tk.Label(self, text="Welcome " + self.educator.get_username() + "!",
                                 font=("Arial Bold", 25))
        welcome_label.grid(row=1, column=0, padx=10, pady=10)
        
        # login time label 
        login_time_label = tk.Label(self,text=f"Last login: {login_time}",
                                 font=("Arial", 15))
        login_time_label.grid(row=2,column=0,padx=10,pady=10)


        # https://www.studytonight.com/tkinter/python-tkinter-button-widget
        button_style = {
            'height': 3,
            'width': 20,
            'font': ("Arial Bold", 12)
        }

        # Button to add a new child
        view_progress_btn = tk.Button(self, text="View Students Progress", command=self.track_progress, **button_style)
        view_progress_btn.grid(row=3, column=0, padx=10, pady=10)

        # Button to view progress of children
        add_child_btn = tk.Button(self, text="Add a new student", command=self.add_child, **button_style)
        add_child_btn.grid(row=4, column=0, padx=10, pady=10)


        # back to main menu
        main_menu_button = tk.Button(self, text="Return to Main Menu", command=self.back_to_login_menu, **button_style)
        main_menu_button.grid(row=5, column=0, padx=10, pady=10)

    def track_progress(self):
        """
        Adding tracking progress frame
        """
        self.place_forget()
        add_child_frame = TrackProgressFrame(self.master, self, self.educator)
        add_child_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def add_child(self):
        """
        Adding add child frame
        """
        self.place_forget()
        add_child_frame = AddChildFrame(self.master, self, self.educator)
        add_child_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_to_login_menu(self):
        """
        Adding back to menu frame
        """
        self.grid_forget()  # Hide the child frame
        self.destroy()  # Destroy the child frame
        self.main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class TrackProgressFrame(tk.Frame):
    """
    The class definition for the TrackProgressFrame class.
    """
    
    def __init__(self, master, educator_frame, educator):
        """
        Constructor for the TrackProgressFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.educator_frame = educator_frame
        self.educator = educator


        #adding main menu button
        main_menu_button = tk.Button(self, text="Return to Educator Menu", command=self.back_to_educator_menu,
                                     font=("Arial Bold", 12))
        main_menu_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # adding welcome label for student progress
        welcome_label = tk.Label(self, text="Student Progress", font=("Arial Bold", 25))
        welcome_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        # adding text box for all children progress
        children_progress_text = tk.Text(self, wrap=tk.WORD, width=70, height=20)
        children_progress_text.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        #grabbing children progress
        linked_account_db = LinkedAccountDatabase()
        user_db = UserDataBase()
        module_db = ModuleDatabase()
        child_lst = ast.literal_eval(linked_account_db.get_user(self.educator.get_username())[1])

        # if there isnt a child, we want to instantiate an empty array
        if (child_lst == "[]"):
            child_lst = []

        # if the child list has items in it
        if(child_lst):

            # for each child in the list
            for child in child_lst:

                # get the childs name as a header
                children_progress_text.insert(tk.END, f"Student: {child}\n", "heading")

                # grab their progress nad turn it into an array
                child_progress = user_db.get_user(child)[7].strip().strip(']').strip('[').split(',')

                #if they have progress
                if(child_progress[0] != ''):
                    #print out each progress of the child
                    for progress in child_progress:
                        module_name = module_db.get_module_name(int(progress))
                        children_progress_text.insert(tk.END,f"Module {progress}: {module_name}\n", "module")

                # else show that the child has no progress
                else:
                    children_progress_text.insert(tk.END, f"No modules completed\n", "no_module")
                children_progress_text.insert(tk.END, f"\n")

        else:
            children_progress_text.insert(tk.END, f"No students added to observation list")

        children_progress_text.config(state=tk.DISABLED)

        # adding group fonts and styles through tagging
        # https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.tag_configure
        children_progress_text.tag_configure("heading", font=("Arial", 13, "bold"), spacing1=5)
        children_progress_text.tag_configure("module", font=("Arial", 10), spacing1=2)
        children_progress_text.tag_configure("no_module", font=("Arial", 10),background="red", spacing1=2)

    def back_to_educator_menu(self):
        """
        Removes the educator frame and adds the parent frame on top again
        """
        self.grid_forget()  # Hide the child frame
        self.destroy()  # Destroy the child frame
        self.educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class AddChildFrame(tk.Frame):
    """
    The class definition for the AddChildFrame class.
    """
    def __init__(self, master, educator_frame, educator):
        """
        Constructor for the AddChildFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.educator_frame = educator_frame
        self.educator = educator

        # initialising databases
        self.linked_account_db = LinkedAccountDatabase()
        self.user_db = UserDataBase()

        self.child_lst = ast.literal_eval(self.linked_account_db.get_user(self.educator.get_username())[1])
        if (self.child_lst == "[]"):
            self.child_lst = []
        # Button to return to main menu
        main_menu_button = tk.Button(self, text="Return to Educator Menu", command=self.back_to_educator_menu,
                                     font=("Arial Bold", 12))
        main_menu_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # welcome label for the site
        welcome_label = tk.Label(self, text="Add a student", font=("Arial Bold", 25))
        welcome_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)



        # Username label
        add_child_label = tk.Label(self, text="Enter the username of your student:", font=("Arial Bold", 20))
        add_child_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # adding a new child input
        self.child_username_entry = tk.StringVar()
        self.child_username_entry = tk.Entry(self, textvariable=self.child_username_entry)
        self.child_username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        # Login button
        login_button = tk.Button(self, text="Add Student",font=("Arial Bold", 12),command=self.adding_child)
        login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # message Label for adding a student
        self.message = tk.StringVar()
        message_label = tk.Label(self,textvariable=self.message,font=("Arial Bold", 10), fg='#ff0000')
        message_label.grid(row=6, columnspan=2, padx=10, pady=10)


        # Current students title
        list_of_students_label = tk.Label(self, text="Curents Students", font=("Arial Bold", 20))
        list_of_students_label.grid(row=1, column=2, sticky=tk.E, padx=10, pady=10)

        # delete button for children
        delete_student_button = tk.Button(self, text="Delete",font=("Arial Bold", 12),command=self.deleting_child)
        delete_student_button.grid(row=8, column=2, sticky=tk.W, padx=11, pady=10)

        # message to show action of delete child
        self.delete_child_message = tk.StringVar()
        message_label = tk.Label(self,textvariable=self.delete_child_message,font=("Arial Bold", 10), fg='#ff0000')
        message_label.grid(row=9, column=2, sticky=tk.W, padx=11, pady=10)


        # Listbox to display the list of students
        self.student_listbox = tk.Listbox(self, selectmode=tk.SINGLE, height=10, width=30)
        self.student_listbox.grid(row=2, column=2, rowspan=6, padx=10, pady=10, sticky=tk.W)

        # Populate the Listbox with students
        for student in self.child_lst:
            self.student_listbox.insert(tk.END, student)
    def adding_child(self):
        """
        The function verify user login details
        """
        username = self.child_username_entry.get()
        if self.user_db.check_if_user_exists(username):
            data = self.user_db.get_user(username)
            if data[5] == "LEARNER":
                if username not in self.child_lst:
                    self.child_lst.append(username)
                    display_str = "Student added"
                    self.linked_account_db.update_user_on_username(self.educator.get_username(), username)
                    self.student_listbox.insert(tk.END, username)
                else: display_str = "Student already added"
            else:
                display_str = "Current profile is not a student"
        else:
            display_str = "This student does not exist."
        self.message.set(display_str)

    def deleting_child(self):
        """
        This function attemps to delete a child from the linked_account csv using the input
        from the list box
        """
        display_str = ""
        try:
            #source code found: https://tkdocs.com/tutorial/morewidgets.html
            # get the seleected value from the list box
            selected_index = self.student_listbox.curselection()
            selected_child = self.student_listbox.get(selected_index)

            # check if that child exists
            if self.user_db.check_if_user_exists(selected_child):
                # if it does exist, remove it from the array
                if(self.linked_account_db.remove_child(self.educator.get_username(), selected_child)):
                    # clear the list box
                    self.student_listbox.delete(0,tk.END)
                    # re-load it from the database
                    self.child_lst = ast.literal_eval(self.linked_account_db.get_user(self.educator.get_username())[1])
                    if (self.child_lst == "[]"):
                        self.child_lst = []
                    # Populate the Listbox with students
                    for student in self.child_lst:
                        self.student_listbox.insert(tk.END, student)
                    display_str = "Records successfully updated"
                else:
                    display_str = "Deletion not successful"
        except:
            display_str = "Please select a child"

        self.delete_child_message.set(display_str)


    def back_to_educator_menu(self):
        """
        Removes the current frame and adds the educator frame on top
        """
        self.grid_forget()  # Hide the child frame
        self.destroy()  # Destroy the child frame
        self.educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)




if __name__ == '__main__':
    pass
    # root = Interface("Codeventure")
    # educator_frame = EducatorFrame(root, "cal")
    # educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # educator_frame.lift()
    # root.mainloop()
