__author__ = 'richmash'

class Alert(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password


    def __repr__(self):
        return "<User {} >".format(self.email)