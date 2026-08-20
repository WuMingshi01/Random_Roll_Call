from random import choice




class random_person:
    def __init__(self,person_list: list):
        self.persons=person_list


    def random(self):
        choice(self.persons)