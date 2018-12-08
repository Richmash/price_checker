from passlib.hash import pbkdf2_sha512
_author__ = 'richmash'


class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password usinf pbkdf2_sha512
        :param password:the sha512 password from the logoin/register form
        :return: A sha512 -> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)


    @staticmethod
    def heck_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The datbase passwords is encrypted more that the user's password at this stage.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if passwords match, False otherwise
        """

        return pbkdf2_sha512.verify(password, hashed_password)