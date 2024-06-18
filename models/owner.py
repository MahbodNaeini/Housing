class Owner:
    def __init__(self, name, surname, national_code):
        self.name = name
        self.surname = surname
        self.national_code = national_code

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_national_code(self):
        return self.national_code

    def set_national_code(self, national_code):
        self.national_code = national_code
