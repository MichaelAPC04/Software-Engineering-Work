import pandas as pd


"""
Created: 10/09/2023
Last Modified: 18/09/2023
Description: This is a pseudo database that is created
from a pandas datafram that allows for
CRUD actions 
"""

class UserDataBase():
    """
    The class definition for the UserDataBase class.
    """
    def __init__(self) -> None:
        """
        Constructor for UserDatabase class
        :output: Returns a pandas dataframe that
        is initialised from the csv
        """
        self.string_location = "db_files/user_data.csv"
        self.db_user = pd.read_csv(self.string_location)

    def get_user(self, username: str):
        """
        This function queries the dataframe searching 
        
        :param: String username - A string containing
        :return: list of items if found, or empty list if username is not found 

        :sample input: get_user("michael123")
        :sameple return: [1, 'michael123', 'michael@gmail.com', 'michaelpw', '[panda,cat,elephant]', 4213823942, ' PARENTS', "'2020-10-10 11:12'", '[]']
        """

        #cycle through the dataframe for username
        for x in self.db_user.itertuples():
            if x[1] == username:
                res_lst = list(x)
                return res_lst[1:] 
        else:
            return []

    def check_if_user_exists(self,username: str):
        """
        This function checks whether a username exists within the database csv 
        
        :param: String username - that is to be queried
        :return: Boolean - True if username is found
        """
        #cycle through the dataframe for username
        for x in self.db_user.itertuples(): 
            #if username exist on the database
            if x[1] == username:
                return True
        #if username does not exist on the database
        return False

    def create_user(self,username,email,password,securityAnswer,phoneNumber,userType,lastlogin,progress=[],points=0,challenge=[]):
        """
        This function creates a new user entry in the database 

        :param: username - username of the user
        :param: String email - email oof the user
        :param: String password - password of the user
        :param: List securityAnswer - list of the security answers
        :param: String phoneNumber - string of the phone number
        :param: String userType - type of the user 
        :param: Dattime lastlogin - last login datatime 
        :param: List progress - list of finished courses
        :param: Integer points - number of points that users has
        :param: List challenge - list of finished challenge


        :return: boolean - True if creating a user is sucecssful 
        
        """
        try:
            new_row = [username,email,password,securityAnswer,phoneNumber,userType,lastlogin,progress,points,challenge]
            self.db_user.loc[len(self.db_user)] = new_row
            self.db_user.to_csv(self.string_location, index=False)
            self.db_user = pd.read_csv(self.string_location)
            return True
        except:
            return False

    def update_password_on_username(self,username,password):
        try:
            # Find the row with the specified username, THIS QUERIES BASED ON USERNAME
            getmatchedRow = self.db_user['username'] == username

            # Update the values for the matched row
            self.db_user.loc[getmatchedRow, 'password'] = password

            # Save the updated DataFrame back to the CSV file
            self.db_user.to_csv(self.string_location, index=False)
            self.db_user = pd.read_csv(self.string_location)
            return True
        except:
            return False

    def showSample(self):
        return self.db_user.sample()
        
    def get_db(self):
        """
        getter method to return user database
        """
        return self.db_user

    def update_last_login(self, username, last_login_time):
        """
        :param username:
        :param last_login_time:
        """
        df = pd.read_csv(self.string_location)
        df.loc[df["username"] == username, "lastLogin"] = last_login_time
        df.to_csv(self.string_location, index=False)

    def get_user_type(self, username: str) -> str:
        """
        This function queries the dataframe searching for the user type based on the given username.

        :param: String username - A string containing the username
        :return: str - The user type if found, or an empty string if username is not found 
        """
        user_row = self.db_user[self.db_user['username'] == username]
        return user_row['userType'].iloc[0]
    
    def get_user_login_time(self,username):
        """
        This function is used to get user's login time

        :param: String username - user's username
        :return: str - string of login time in YYYY-MM-DD HH:MM format 
        """
        user_row = self.db_user[self.db_user['username'] == username]
        return user_row['lastLogin'].iloc[0]
    
    def update_user_database(self):
        """
        This function updates the user database

        No return value
        """
        self.db_user = pd.read_csv(self.string_location)
    
if __name__ == '__main__':
    db = UserDataBase()
    user= db.create_user(1,1,1,1,1,1,1)
    print(user)
