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

    def to_json(self):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
