#!/usr/bin/python3
""" Class that defines a student """


class Student:
    """ Student class with an instance and a public method """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of Student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        Args:
            attrs: filter. If it is a list of strings, only attribute names
            contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """

        dictionary = {}
        if type(attrs) is list and all([type(elem) is str for elem in attrs]):
            for k, v in self.__dict__.items():
                if k in attrs:
                    dictionary[k] = v
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Args:
            json: dictionary where the keys and values will be taken
            and converted into the new values of the class Student
        """

        for key, value in json.items():
            self.__dict__[key] = value
