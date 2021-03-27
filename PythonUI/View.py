"""
Create various views
"""


class View:
    """
    View is the basis of all views
    """

    swift = (

    )

    def __init__(self, name: str):
        self.name = name

    def build(self):
        file = self.swift
        return file
