class User:

    def __init__(self, name, nic, mobile, email, address):
        self.__name = name #encapsulation
        self.__nic = nic
        self.__phone_no = mobile
        self.__email = email
        self.__address = address

    def get_nic(self):
        return self.__nic

    def set_nic(self, nic):
        self.__nic = nic

    def get_name(self): #boilerplate code
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_mobile(self):
        return self.__nic

    def set_mobile(self, mobile):
        self.__phone_no = mobile

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address


    def __str__(self):
        return

    def __hash__(self): #overring the parent class object __str__ method
        return f"User name - {self.__name} User email - {self.__email}"