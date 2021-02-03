class Reader:
    def __init__(self, person_id, person_name, person_surname):
        """

        :param person_id: ID читателя
        :param person_name: Имя пользователя
        :param person_surname: Фамилия пользователя
        """
        self.person_id = person_id
        self.person_name = person_name
        self.person_surname = person_surname

    def print_full_name(self):
        """

        :return: Имя и Фамилия читателя
        """
        return print(f'{self.person_name} {self.person_surname}')
