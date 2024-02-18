#!/usr/bin/python3

""" This module provides Base class
"""

import json
import turtle


class Base:
    """
    This class representing base class
    """
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        """
        Initializes an instance of the Base class.

        Parameters:
        - id (int): The identifier for the instance. If not
        provided, it is auto-generated.

        Returns:
        None
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Parameters:
        - list_dictionaries (list): List of dictionaries to be converted.

        Returns:
        str: JSON-formatted string representing
        the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Parameters:
        - json_string (str): JSON-formatted string
        to be converted.

        Returns:
        list: List of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        """
        Saves a list of instances to a JSON file.

        Parameters:
        - list_objs (list): List of instances to be saved.

        Returns:
        None
        """

        if not list_objs:
            list_objs = []
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            temp_list = [obj.to_dictionary() for obj in list_objs]
            json_string = Base.to_json_string(temp_list)
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary) -> object:
        """
        Create a new obj from dictionary

        Parameters:
        - cls: class where this method call.
        - dictionary (dict): the dictionary to be obj

        Returns:
        cls instance
        """

        classname = cls.__name__
        dummy = {}
        if classname == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls) -> list:
        """
        Load objects from a JSON file and create instances of the class.

        Returns:
            list: A list of created instances.
        """
        filename = cls.__name__ + ".json"
        list_objs = []
        try:
            with open(filename, "r") as file:
                file_content = file.read()
                loaded_data = cls.from_json_string(file_content)
                list_objs = [cls.create(**obj) for obj in loaded_data]
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw squares and rectangles using turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.
        """
        turtle.color("red")
        turtle.bgcolor("cyan")
        turtle.width(5)
        turtle.speed(1)
        turtle.penup()
        turtle.goto(-300, 0)
        turtle.pendown()
        Base.draw_square(list_squares)
        Base.draw_rectangle(list_rectangles)
        turtle.done()

    @staticmethod
    def draw_rectangle(list_rectangles):
        """
        Draw rectangles using turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects.
        """
        counter = 0
        for obj in list_rectangles:
            for i in range(4):
                turtle.forward(obj.width if i % 2 == 0 else obj.height)
                turtle.left(90)
            counter += 1
            if counter != len(list_rectangles):
                turtle.penup()
                turtle.forward(50 + obj.width)
                turtle.pendown()

    @staticmethod
    def draw_square(list_squares):
        """
        Draw squares using turtle graphics.

        Args:
            list_squares (list): List of Square objects.
        """
        for obj in list_squares:
            for _ in range(4):
                turtle.forward(obj.size)
                turtle.left(90)
            turtle.penup()
            turtle.forward(50 + obj.size)
            turtle.pendown()
