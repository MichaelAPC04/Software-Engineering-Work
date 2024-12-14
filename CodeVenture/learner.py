import pandas as pd
import tkinter as tk
from tkinter import messagebox

"""
The LernerFrame is the page for learner type user, It includes view module, attempt quiz,
attempt challenge, track progress, view points and logout.

Date: 25/10/23
Last Modified: 30/10/23
"""


class LearnerFrame(tk.Frame):
    """
    Frame for the learner user type with specific options.
    """
    button_height = 3
    button_width = 20
    button_font = ("Arial Bold", 12)
    button_background = "#f1f1ee"
    
    def __init__(self, master,main_menu_frame,username,login_time):
        """
        Constructor for the LearnerFrame class.
        """
        super().__init__(master=master)
        self.master = master
        self.main_menu_frame = main_menu_frame
        self.username = username

        # welcome label
        welcome_label = tk.Label(self,text=f"Welcome LEARNER {username}!",
                                 font=("Arial Bold", 25))
        welcome_label.grid(row=0,column=0,padx=10,pady=10)

        # login time label 
        login_time_label = tk.Label(self,text=f"Last login: {login_time}",
                                 font=("Arial", 15))
        login_time_label.grid(row=1,column=0,padx=10,pady=10)

        # Button to view module
        self.view_module_button = tk.Button(self, text="View Module",
                                       height=self.button_height,
                                       width=self.button_width,
                                       activebackground=self.button_background,
                                       font=self.button_font,
                                       command=self.view_module)
        self.view_module_button.grid(row=2,column=0,padx=10,pady=10)

        # Button to attempt quiz
        self.attempt_quiz_button = tk.Button(self, text="Attempt Quiz",
                                        height=self.button_height,
                                        width=self.button_width,
                                        activebackground=self.button_background,
                                        font=self.button_font,
                                        command=self.attempt_quiz)
        self.attempt_quiz_button.grid(row=3,column=0,padx=10,pady=10)

        # Button to attempt challenge
        self.attempt_challenge_button = tk.Button(self, text="Attempt Challenge",
                                             height=self.button_height,
                                             width=self.button_width,
                                             activebackground=self.button_background,
                                             font=self.button_font,
                                             command=self.attempt_challenge)
        self.attempt_challenge_button.grid(row=4,column=0,padx=10,pady=10)

        # Button to track progress
        self.track_progress_button = tk.Button(self, text="Track Progress",
                                          height=self.button_height,
                                          width=self.button_width,
                                          activebackground=self.button_background,
                                          font=self.button_font,
                                          command=self.track_progress)
        self.track_progress_button.grid(row=5,column=0,padx=10,pady=10)

        # Button to view points
        self.view_points_button = tk.Button(self, text="View Points",
                                       height=self.button_height,
                                       width=self.button_width,
                                       activebackground=self.button_background,
                                       font=self.button_font,
                                       command=self.view_points)
        self.view_points_button.grid(row=6,column=0,padx=10,pady=10)

        self.logout_button = tk.Button(self, text="Logout",
                                  height=self.button_height,
                                  width=self.button_width,
                                  activebackground=self.button_background,
                                  font=self.button_font,
                                  command=self.logout_user)
        self.logout_button.grid(row=7,column=0,padx=10,pady=10)

    def close_view_module(self):
        """
        Close the view module window and enable all buttons.
        """
        self.enable_all_buttons()
        self.view_module.destroy()
    
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

    def view_module(self):
        """
        This function handles the view module action.
        """
        self.disable_all_buttons()
        # Create a new top-level window for the view module page
        self.view_module = tk.Toplevel(self.master)
        self.view_module.title("View Module")
        
        # move toplevel to the middle 
        self.popup_midpoint(self.view_module)
        
        # Load the module data from the CSV
        self.modules_df = pd.read_csv("db_files/module_data.csv", sep="|")
        self.selected_module = tk.StringVar(value=self.modules_df['module_name'][0]) 

        # Create and pack the radio buttons
        for index, row in self.modules_df.iterrows():
            radio = tk.Radiobutton(self.view_module, text=row['module_name'], 
                                   variable=self.selected_module, value=row['module_name'])
            radio.pack(pady=5, anchor=tk.W)

        # Create and pack the "View Module" button
        view_button = tk.Button(self.view_module, text="View Module", command=self.show_module_content)
        view_button.pack(pady=10)

        # Button to close the window
        close_button = tk.Button(self.view_module, text="Close", command=self.close_view_module)
        close_button.pack(pady=10)

        #if popup is closed by control button on the top right corner enable exit button
        self.view_module.protocol("WM_DELETE_WINDOW",self.close_view_module)

    def show_module_content(self):
        """
        This function displays the content of the selected module in a message box.
        """
        self.disable_all_buttons()
        module_name = self.selected_module.get()
        content = self.modules_df[self.modules_df['module_name'] == module_name]['content'].iloc[0]
        
        # Create a new top-level window for the module content
        content_window = tk.Toplevel(self.master)
        content_window.title(module_name)

        # move toplevel to the middle 
        self.popup_midpoint(content_window)

        # Display the content in a label
        content_label = tk.Label(content_window, text=content, wraplength=400, font=("Arial", 12), padx=10, pady=10)
        content_label.pack(pady=20)

        # Button to close the window
        close_button = tk.Button(content_window, text="Close", command=content_window.destroy)
        close_button.pack(pady=20)
    
    def close_attempt_quiz(self):
        """
        Close the view module window and enable all buttons.
        """
        self.enable_all_buttons()
        self.quiz_window.destroy()
    
    def attempt_quiz(self):
        """
        Display the quiz selection page.
        """
        self.disable_all_buttons()
        self.is_challenge = False
        # Create a new top-level window for the quiz selection page
        self.quiz_window = tk.Toplevel(self.master)
        self.quiz_window.title("Attempt Quiz")
        
        # move toplevel to the middle 
        self.popup_midpoint(self.quiz_window)

        # Load the quiz data from the CSV
        self.quiz_df = pd.read_csv("db_files/quiz_data.csv", sep="|")
        self.selected_quiz = tk.StringVar(value=self.quiz_df['quiz_id'][0])  # Default to the first quiz ID

        # Create and pack the radio buttons for quiz IDs
        for index, row in self.quiz_df.iterrows():
            radio = tk.Radiobutton(self.quiz_window, text="Quiz "+str(row['quiz_id']), 
                                variable=self.selected_quiz, value=row['quiz_id'])
            radio.pack(pady=5, anchor=tk.W)

        # Button to attempt the selected quiz
        attempt_button = tk.Button(self.quiz_window, text="Attempt Quiz", command=self.display_quiz)
        attempt_button.pack(pady=10)

        # Button to close the quiz selection window
        close_button = tk.Button(self.quiz_window, text="Close", command=self.close_attempt_quiz)
        close_button.pack(pady=10)

        #if popup is closed by control button on the top right corner enable exit button
        self.quiz_window.protocol("WM_DELETE_WINDOW",self.close_attempt_quiz)

    def display_quiz(self):
        """
        Display the quiz for the selected quiz ID.
        """
        # Destroy the quiz selection window
        self.quiz_window.destroy()

        # Create a new top-level window for the quiz
        self.quiz_attempt_window = tk.Toplevel(self.master)

        # move toplevel to the middle 
        self.popup_midpoint(self.quiz_attempt_window)

        quiz_id = int(self.selected_quiz.get())
        question = self.quiz_df[self.quiz_df['quiz_id'] == quiz_id]['questions'].iloc[0]

        # Display the question
        question_label = tk.Label(self.quiz_attempt_window, text=question)
        question_label.pack(pady=10, anchor=tk.W)

        # Entry field for the answer
        self.answer_entry = tk.Entry(self.quiz_attempt_window)
        self.answer_entry.pack(pady=10)

        # Button to submit the answer
        submit_button = tk.Button(self.quiz_attempt_window, text="Submit Answer", command=lambda: self.check_answer(quiz_id, challenge=self.is_challenge))
        submit_button.pack(pady=10)

        # Button to close the quiz attempt window
        close_button = tk.Button(self.quiz_attempt_window, text="Close", command=lambda:[self.enable_all_buttons(),self.quiz_attempt_window.destroy()])
        close_button.pack(pady=10, anchor=tk.W)
        
        #if popup is closed by control button on the top right corner enable exit button
        self.quiz_attempt_window.protocol("WM_DELETE_WINDOW",lambda:[self.enable_all_buttons(),self.quiz_attempt_window.destroy()])

    def check_answer(self, quiz_id, challenge = False):
        """
        Check the submitted answer against the correct answer.
        """
        submitted_answer = self.answer_entry.get()
        correct_answer = self.quiz_df[self.quiz_df['quiz_id'] == quiz_id]['answers'].iloc[0]
        
        if str(submitted_answer) == str(correct_answer):
            self.update_progress(quiz_id, challenge=challenge)
            messagebox.showinfo(title="Result", message="Correct Answer!")
        else:
            explanation = self.quiz_df[self.quiz_df['quiz_id'] == quiz_id]['explanation'].iloc[0]
            messagebox.showerror(title="Result", message=f"Wrong answer!\n\nExplanation: {explanation}")

        # Destroy the quiz attempt window after displaying the message box
        self.quiz_attempt_window.destroy()
        self.enable_all_buttons()

    def close_attempt_challenge(self):
        """
        Close the view module window and enable all buttons.
        """
        self.enable_all_buttons()
        self.quiz_window.destroy()

    def attempt_challenge(self):
        """
        This function handles the attempt challenge action.
        """
        self.disable_all_buttons()
        self.is_challenge = True
        # Create a new top-level window for the quiz selection page
        self.quiz_window = tk.Toplevel(self.master)
        self.quiz_window.title("Challenge question list")
        
        # move toplevel to the middle 
        self.popup_midpoint(self.quiz_window)

        # Load the quiz data from the CSV
        self.quiz_df = pd.read_csv("db_files/challenge_quiz.csv", sep="|")
        self.selected_quiz = tk.StringVar(value=self.quiz_df['quiz_id'][0])  # Default to the first quiz ID

        # Create and pack the radio buttons for quiz IDs
        for index, row in self.quiz_df.iterrows():
            radio = tk.Radiobutton(self.quiz_window, text="Challenge "+str(row['quiz_id']), 
                                variable=self.selected_quiz, value=row['quiz_id'])
            radio.pack(pady=5, anchor=tk.W)

        # Button to attempt the selected quiz
        attempt_button = tk.Button(self.quiz_window, text="Attempt Quiz", command=self.display_quiz)
        attempt_button.pack(pady=10)

        # Button to close the quiz selection window
        close_button = tk.Button(self.quiz_window, text="Close", command=self.close_attempt_challenge)
        close_button.pack(pady=10)

        #if popup is closed by control button on the top right corner enable exit button
        self.quiz_window.protocol("WM_DELETE_WINDOW",self.close_attempt_challenge)

    def update_progress(self, quiz_id, challenge=False):
        """
        Update the progress of the current user after passing a quiz.
        """
        df = pd.read_csv("db_files/user_data.csv")

        # Determine which columns to update based on the quiz type
        if challenge:
            column_name = "challenge"
            point_increment = 20
        else:
            column_name = "progress"
            point_increment = 10

        # Find the progress and points of the current user
        current_progress = df.loc[df["username"] == self.username, column_name].values[0]
        current_points = df.loc[df["username"] == self.username, "points"].values[0]

        # Convert the string representation of the list to an actual list
        progress_list = eval(current_progress)

        # Update progress if the quiz hasn't been attempted yet
        if quiz_id not in progress_list:
            progress_list.append(quiz_id)
            updated_progress_str = str(progress_list)
            df.loc[df["username"] == self.username, column_name] = updated_progress_str

            # Update points
            updated_points = current_points + point_increment
            df.loc[df["username"] == self.username, "points"] = updated_points

            df.to_csv("db_files/user_data.csv", index=False)

    def track_progress(self):
        """
        Display the progress of the current user.
        """
        # Load the user data CSV
        df = pd.read_csv("db_files/user_data.csv")
        
        # Find the progress of the current user
        current_progress = df.loc[df["username"] == self.username, "progress"].values[0]
        challenge_progress = df.loc[df["username"] == self.username, "challenge"].values[0]
        
        # Convert the string representation of the list to an actual list
        progress_list = eval(current_progress)
        challenge_list = eval(challenge_progress)
        
        # Create a message based on the progress list
        progress_message = "Normal Quiz Progress:\nYou finished question(s): " + ", ".join(map(str, progress_list))
        challenge_message = "\n\nChallenge Quiz Progress:\nYou finished question(s): " + ", ".join(map(str, challenge_list))
        
        # Display the combined message
        messagebox.showinfo(title="Your Progress", message=progress_message + challenge_message)

    def view_points(self):
        """
        Displays the points of the current user in a message box.
        """
        df = pd.read_csv("db_files/user_data.csv")
        
        # Fetch the points of the current user
        current_points = df.loc[df["username"] == self.username, "points"].values[0]
        
        # Display the points in a message box
        messagebox.showinfo(title="Your Points", message=f"You have {current_points} points!")
    
    def logout_user(self):
        """
        Logout the current user and return to the login frame.
        """
        from loginframe import LoginFrame
        self.place_forget()  # Hide the current frame (LearnerFrame)
        login_frame = LoginFrame(self.master, self.main_menu_frame)  # Initialize the login frame
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def disable_all_buttons(self):
        """
        Disable all buttons in the frame.
        """
        self.view_module_button.config(state=tk.DISABLED)
        self.attempt_quiz_button.config(state=tk.DISABLED)
        self.attempt_challenge_button.config(state=tk.DISABLED)
        self.track_progress_button.config(state=tk.DISABLED)
        self.view_points_button.config(state=tk.DISABLED)
        self.logout_button.config(state=tk.DISABLED)

    def enable_all_buttons(self):
        """
        Enable all buttons in the frame.
        """
        self.view_module_button.config(state=tk.NORMAL)
        self.attempt_quiz_button.config(state=tk.NORMAL)
        self.attempt_challenge_button.config(state=tk.NORMAL)
        self.track_progress_button.config(state=tk.NORMAL)
        self.view_points_button.config(state=tk.NORMAL)
        self.logout_button.config(state=tk.NORMAL)

        


if __name__ == '__main__':
    # root = tk.Tk()
    pass
