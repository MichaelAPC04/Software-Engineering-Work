"""
Created: 25/10/2023
Last Modified: 30/10/2023
Description: Abstract User class for inheriting by child user classes
"""

class User:
    """
    This is the class definition for the User class.
    """

    def __init__(self, username, email, password, securityAnswer, phoneNumber, userType=None):
        """
        Constructor for the User class.
        :param: username - username of the User
        :param: email - email of the User
        :param: password - Password of the User
        :param: security answer - security questions of the User
        :param: phoneNumber - Phone number of the User
        """
        self.username = username
        self.email = email
        self.password = password
        self.securityAnswer = securityAnswer
        self.phoneNumber = phoneNumber
        self.userType = userType


