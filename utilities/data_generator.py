from mimesis import Generic


class DataGenerator:

    @staticmethod
    def generate_name():
        return Generic().person.name()

    @staticmethod
    def generate_email():
        return Generic().person.email()

    @staticmethod
    def generate_password():
        return Generic().person.password(length=8, hashed=False)
