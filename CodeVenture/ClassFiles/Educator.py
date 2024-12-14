from ClassFiles.User import User
import string
import random

"""
Created: 25/10/2023
Last Modified: 30/10/2023
Description: Educator class for Codeventure
"""

class Educator(User):
    """
    This is the class definition for the Educator class.
    """
    def __init__(self, username, email, password, securityAnswer, phoneNumber):
        """
        Constructor for the Educator class.
        :param: username - username of the educator
        :param: email - email of the educator
        :param: password - Password of the educator
        :param: security answer - security questions of the eduvator
        :param: phoneNumber - Phone number of the eduvator
        """
        super().__init__(username, email, password, securityAnswer, phoneNumber)
        self.userType = 'EDUCATOR'
        self.unique_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    def get_username(self):
        """
        This function is used to get the username
        :return: returns a string of the educator username
        """
        return self.username

    def get_email(self):
        """
        This function is used to get the email
        :return: returns the email of the educator
        """
        return self.email