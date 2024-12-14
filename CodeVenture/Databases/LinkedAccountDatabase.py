import pandas as pd
import ast

"""
Created: 25/10/2023
Last Modified: 25/10/2023
Description: This is a pseudo database that is created
from a pandas dataframe that allows for
CRUD actions
"""


class LinkedAccountDatabase():
    """
    The class definition for the LinkedAccountDatabase class.
    """

    def __init__(self) -> None:
        """
        Constructor for UserDatabase class
        :output: Returns a pandas dataframe that
        is initialised from the csv
        """
        self.string_location = "db_files/linked_account.csv"
        self.db_user = pd.read_csv(self.string_location)

    def get_user(self, username: str):
        """
        This function queries the dataframe searching

        :param: String username - A string containing
        :return: list of items if found, or empty list if username is not found

        :sample input: get_user("michael123")
        :sameple return: [1, "cal","[phil123,joe]"]
        """

        # cycle through the dataframe for username
        for x in self.db_user.itertuples():
            if x[1] == username:
                res_lst = list(x)
                return res_lst[1:]
        else:
            return []

    def update_user_on_username(self, username, child):
        """
        Add the child into the linked_account.csv

        :param: username - username of the user
        :param: child - children to be linked

        :return: boolean - True if update is sucessful
        """
        try:
            # Find the row with the specified username, THIS QUERIES BASED ON USERNAME
            getmatchedRow = self.db_user['username'] == username
            children_list = ast.literal_eval(self.db_user.loc[getmatchedRow, 'children'].values[0])
            if (children_list == "[]"):
                children_list = []
            print(children_list)
            # Append the child to the list
            children_list.append(child)
            print(children_list)
            self.db_user.loc[getmatchedRow, 'children'] = [children_list]
            # Save the updated DataFrame back to the CSV file
            self.db_user.to_csv(self.string_location, index=False)
            self.db_user = pd.read_csv(self.string_location)
            print("Records updated!\n")
            return True
        except:
            print("the username is not found")
            return False

    def remove_child(self, username, child):
        """
        Removes a child from the username array
        :param: username - Username of the user
        :param: child - Child that needs to be removed
        :return: Boolean true or false if action is successful
        """
        try:
            getmatchedRow = self.db_user['username'] == username
            children_list = ast.literal_eval(self.db_user.loc[getmatchedRow, 'children'].values[0])
            if (children_list == "[]"):
                children_list = []
            print(children_list)
            # Append the child to the list
            if (len(children_list) > 0):
                children_list.remove(child)
                print(children_list)
                self.db_user.loc[getmatchedRow, 'children'] = [children_list]
                # Save the updated DataFrame back to the CSV file
                self.db_user.to_csv(self.string_location, index=False)
                self.db_user = pd.read_csv(self.string_location)
                print("Records updated!\n")
                return True
            else:
                print("there are no records to remove")
                return False
        except:
            print("the username is not found")
            return False

    def get_db(self):
        """
        getter method to return user database
        :return: Pandas dataframe of the db
        """
        return self.db_user

    def add_new_row(self, username):
        """
        When parent/educator creates an account make a new row in the linked_account.csv
        with their username
        :param: username = New user to add
        """
        new_row = [username, []]
        self.db_user.loc[len(self.db_user)] = new_row
        self.db_user.to_csv(self.string_location, index=False)
        # update database
        self.db_user = pd.read_csv(self.string_location)
