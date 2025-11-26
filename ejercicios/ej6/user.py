class User:
    def __init__(self,username,email,age,active=True):
        self.__username=self.validarUsername(username)
        self.__email=self.validarEmail(email)
        self.__age=self.validarAge(age)
        self.__active=active

    def __str__(self):
        return f"Usuario: {self.__username}({self.__age}) Active--{self.__active}"

    @property
    def email(self):
        return self.__email
    @property
    def age(self):
        return  self.__age

    @property
    def active(self):
        return self.__active
    ############################################################################
    def deactive(self):
        self.__active=False
    def activ(self):
        self.__active=True


    ############################################################################
    @staticmethod
    def validarUsername(username):
        if username != "" and not username.endswith(" ") and not username.startswith(" "):
            return username
        else:raise ValueError("Username no valido")

    @staticmethod
    def validarEmail(email):
        if "@" in email and "." in email:
            return email
        else:raise ValueError("Email no valido")
    @staticmethod
    def validarAge(age):
        if 14<=age<=120:
            return age
        else: raise ValueError("Edad no permitida")