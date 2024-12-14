import pandas as pd
import tkinter as tk
from tkinter import messagebox

"""
The AdminFrame is used for admin type user where it allows view and edit the user's details
It contains several functions called 'view username', 'edit profile', delete profile', and 'logout'.

Date: 26/10/23
Last Modified: 30/10/23
"""
class AdminFrame(tk.Frame):
    """
    Frame for the admin user type with specific options.
    """
    button_height = 3
    button_width = 20
    button_font = ("Arial Bold", 12)
    button_background = "#f1f1ee"

    def __init__(self, master, main_menu_frame, username):
        """
        Constructor for the AdminFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.main_menu_frame = main_menu_frame
        self.username = username

        # Welcome label
        welcome_label = tk.Label(self, text=f"Welcome ADMIN {username}!", font=("Arial Bold", 25))
        welcome_label.grid(row=1, column=0, padx=10, pady=10)

        # Button to view all usernames
        self.view_username_button = tk.Button(self, text="View All Usernames", height=self.button_height,
                                        width=self.button_width, activebackground=self.button_background,
                                        font=self.button_font, command=self.view_username)
        self.view_username_button.grid(row=2, column=0, padx=10, pady=10)

        # Button to edit profile
        self.edit_profile_button = tk.Button(self, text="Edit Profile", height=self.button_height,
                                       width=self.button_width, activebackground=self.button_background,
                                       font=self.button_font, command=self.edit_profile)
        self.edit_profile_button.grid(row=3, column=0, padx=10, pady=10)

        # Button to delete profile
        self.delete_profile_button = tk.Button(self, text="Delete Profile", height=self.button_height,
                                         width=self.button_width, activebackground=self.button_background,
                                         font=self.button_font, command=self.delete_profile)
        self.delete_profile_button.grid(row=4, column=0, padx=10, pady=10)

        # Button to log out
        self.logout_button = tk.Button(self, text="Logout", height=self.button_height,
                                  width=self.button_width, activebackground=self.button_background,
                                  font=self.button_font, command=self.logout_user)
        self.logout_button.grid(row=5, column=0, padx=10, pady=10)

    def view_username(self):
        """
        Display all usernames in the system.
        """
        self.disable_all_buttons()
        self.view_username_window = tk.Toplevel(self.master)
        self.view_username_window.title("Usernames List")

        # move toplevel to the middle 
        self.popup_midpoint(self.view_username_window)

        # Load the user data from CSV
        df = pd.read_csv("db_files/user_data.csv")
        self.selected_username = tk.StringVar(value=df['username'].iloc[0])

        # Create and pack radio buttons for each username
        for username in df['username']:
            radio = tk.Radiobutton(self.view_username_window, text=username, 
                                   variable=self.selected_username, value=username)
            radio.pack(pady=5, anchor=tk.W)

        # Button to view details of selected username
        view_button = tk.Button(self.view_username_window, text="View Details", command=self.show_user_details)
        view_button.pack(pady=10)

        # Button to close the view usernames window
        close_button = tk.Button(self.view_username_window, text="Close", command=self.close_view_username)
        close_button.pack(pady=10)
        
        # Bind the close action to the "X" button
        self.view_username_window.protocol("WM_DELETE_WINDOW", self.close_view_username)

    def show_user_details(self):
        """
        Display details of the selected username.
        """
        username = self.selected_username.get()
        df = pd.read_csv("db_files/user_data.csv")
        user_info = df[df['username'] == username].iloc[0]

        # Create a new top-level window for displaying user details
        details_window = tk.Toplevel(self.master)
        details_window.title(f"Details of {username}")
        
        # move toplevel to the middle 
        self.popup_midpoint(details_window)

        # Display each detail as a label
        for column, value in user_info.items():
            label = tk.Label(details_window, text=f"{column.capitalize()}: {value}")
            label.pack(pady=5, anchor=tk.W)

        # Button to close the details window
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10, anchor=tk.W)

    def close_view_username(self):
        """
        Close the view username window and enable all buttons.
        """
        self.enable_all_buttons()
        self.view_username_window.destroy()

    def edit_profile(self):
        """
        Allow the admin to edit the profile of a user.
        """
        self.disable_all_buttons()
        self.edit_profile_window = tk.Toplevel(self.master)
        self.edit_profile_window.title("Edit User Profile")

        # move toplevel to the middle 
        self.popup_midpoint(self.edit_profile_window)

        # Load the user data from CSV
        df = pd.read_csv("db_files/user_data.csv")
        self.selected_user_to_edit = tk.StringVar(value=df['username'].iloc[0])

        # Create and pack radio buttons for each username
        for username in df['username']:
            radio = tk.Radiobutton(self.edit_profile_window, text=username, 
                                   variable=self.selected_user_to_edit, value=username)
            radio.pack(pady=5, anchor=tk.W)

        # Button to begin editing the selected user profile
        edit_button = tk.Button(self.edit_profile_window, text="Edit User", command=self.show_edit_fields)
        edit_button.pack(pady=10)

        # Button to close the edit profile window
        close_button = tk.Button(self.edit_profile_window, text="Close", command=self.close_edit_profile)
        close_button.pack(pady=10)

        # Bind the close action to the "X" button
        self.edit_profile_window.protocol("WM_DELETE_WINDOW", self.close_edit_profile)

    def show_edit_fields(self):
        """
        Display editable fields for the selected user profile.
        """
        username = self.selected_user_to_edit.get()
        df = pd.read_csv("db_files/user_data.csv")
        user_info = df[df['username'] == username].iloc[0]

        self.edit_fields_window = tk.Toplevel(self.master)
        self.edit_fields_window.title(f"Editing {username}")

        # move toplevel to the middle 
        self.popup_midpoint(self.edit_fields_window)

        self.updated_values = {}  # dictionary to store updated values

        # Loop to create labels and entry fields for each editable detail
        for index, column in enumerate(['username', 'email', 'password', 'phoneNumber']):
            label = tk.Label(self.edit_fields_window, text=f"{column.capitalize()}:")
            label.grid(row=index, column=0, pady=5, padx=5, sticky=tk.W)

            entry = tk.Entry(self.edit_fields_window)
            entry.grid(row=index, column=1, pady=5, padx=5)
            entry.insert(0, user_info[column])
            self.updated_values[column] = entry

        # Button to save the edited details
        save_button = tk.Button(self.edit_fields_window, text="Commit", command=self.commit_changes)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)
    
    def commit_changes(self):
        """
        Save the edited details after confirmation.
        """
        confirm = messagebox.askyesno(title="Confirmation", message="Are you sure you want to change these details?")
        if confirm:
            df = pd.read_csv("db_files/user_data.csv")
            row_idx = df.index[df['username'] == self.selected_user_to_edit.get()].tolist()[0]
            
            for column, entry_widget in self.updated_values.items():
                new_value = entry_widget.get().strip()  # Get the updated value from the entry widget
                if new_value:  # If the entry widget is not empty
                    df.at[row_idx, column] = new_value  # Update the corresponding value in the dataframe

            df.to_csv("db_files/user_data.csv", index=False)
            messagebox.showinfo(title="Success", message="User details have been updated.")
            self.edit_fields_window.destroy()
            self.close_edit_profile()

    def close_edit_profile(self):
        """
        Close the edit profile window and enable all buttons.
        """
        self.enable_all_buttons()
        self.edit_profile_window.destroy()

    def delete_profile(self):
        """
        Allow the admin to delete a user's profile.
        """
        self.disable_all_buttons()
        self.delete_profile_window = tk.Toplevel(self.master)
        self.delete_profile_window.title("Delete User Profile")

        # move toplevel to the middle 
        self.popup_midpoint(self.delete_profile_window)

        # Load the user data from CSV
        df = pd.read_csv("db_files/user_data.csv")
        self.selected_user_to_delete = tk.StringVar(value=df['username'].iloc[0])

        # Create and pack radio buttons for each username
        for username in df['username']:
            radio = tk.Radiobutton(self.delete_profile_window, text=username, 
                                   variable=self.selected_user_to_delete, value=username)
            radio.pack(pady=5, anchor=tk.W)

        # Button to initiate the delete process for the selected user profile
        delete_button = tk.Button(self.delete_profile_window, text="Remove User", command=self.confirm_delete)
        delete_button.pack(pady=10)

        # Button to close the delete profile window
        close_button = tk.Button(self.delete_profile_window, text="Close", command=self.close_delete_profile)
        close_button.pack(pady=10)

        # Bind the close action to the "X" button
        self.delete_profile_window.protocol("WM_DELETE_WINDOW", self.close_delete_profile)

    def confirm_delete(self):
        """
        Confirm the delete action with the admin.
        """
        confirm = messagebox.askyesno(title="Confirmation", message="Are you sure you want to delete this user?")
        if confirm:
            df = pd.read_csv("db_files/user_data.csv")
            df = df[df['username'] != self.selected_user_to_delete.get()]
            df.to_csv("db_files/user_data.csv", index=False)
            messagebox.showinfo(title="Success", message="User has been deleted.")
            self.delete_profile_window.destroy()
            self.enable_all_buttons()

    def close_delete_profile(self):
        """
        Close the delete profile window and enable all buttons.
        """
        self.enable_all_buttons()
        self.delete_profile_window.destroy()


    def logout_user(self):
        """
        Logout the admin and return to the login frame.
        """
        from loginframe import LoginFrame
        self.place_forget()
        login_frame = LoginFrame(self.master, self.main_menu_frame)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def disable_all_buttons(self):
        """
        Disable all buttons in the frame.
        """
        self.view_username_button.config(state=tk.DISABLED)
        self.edit_profile_button.config(state=tk.DISABLED)
        self.delete_profile_button.config(state=tk.DISABLED)
        self.logout_button.config(state=tk.DISABLED)

    def enable_all_buttons(self):
        """
        Enable all buttons in the frame.
        """
        self.view_username_button.config(state=tk.NORMAL)
        self.edit_profile_button.config(state=tk.NORMAL)
        self.delete_profile_button.config(state=tk.NORMAL)
        self.logout_button.config(state=tk.NORMAL)

    def popup_midpoint(self,toplevel):
        """
        This function is used to center the toplevel to the middle of the program
        """
        #get upper left corner coordinate of the main window
        x = self.master.winfo_x()
        y = self.master.winfo_y()

        # update idletask so view_module.winfo_width() and view_module.winfo_height() will return
        # the correct value
        # https://stackoverflow.com/questions/34373533/winfo-width-returns-1-even-after-using-pack
        self.master.update_idletasks() 

        # get the midpoint of the main window and the popup
        mid_width = int((self.master.width -toplevel.winfo_width())/2)
        mid_height = int((self.master.height - toplevel.winfo_height())/2)
        
        #popup is display on the middle of the main window
        toplevel.geometry(f"+{x+mid_width}+{y+mid_height}")


if __name__ == '__main__':
    pass

