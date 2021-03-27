"""
Provide contextual support for the UI interface
"""
from PythonUI import View


class MacUIManager:
    def __init__(self, platform):
        self.views = []
        self.platform = platform
        self.main_view = None
        self.main_view_str = '{view}'

    def view(self, name: str):
        view = View.View(name=name)
        self.views.append(view)
        return view

    def set_main_view(self, view: View.View):
        self.main_view = view
        self.platform.swift = str(self.platform.swift).replace(self.main_view_str, self.main_view.name + '()')
        self.main_view_str = view.name
