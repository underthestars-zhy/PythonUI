"""
Create various views
"""

import random


class View:
    """
    View is the basis of all views
    """

    swift: str = (
        'struct {name}: View {\n'
        '\n'
        '    {var}\n'
        '    var body: some View {\n'
        '    {code}\n'
        '    }\n'
        '}\n'
    )

    code = '{code}'
    view = None
    variables = []

    def __init__(self, name: str):
        self.name = name
        self.swift = self.swift.replace('{name}', self.name)

    def build(self):
        file = self.swift
        file = '//\n//  Created By PythonUI\n//\n\n' + file
        file = file.replace('{code}', self.code)
        if len(self.variables) != 0:
            for item in self.variables:
                file = file.replace('{var}', item + '\n' + '    {var}\n')
        file = file.replace('    {var}\n', '', 1)
        if self.code == '{code}' or self.code == ' ' or self.code == '':
            print(f'Wrong - {self.name} code is not set')
        return file

    def add_view(self, view):
        self.code = view.build()
        self.view = view
        if len(view.variable_build()) != 0:
            self.variables = view.variable_build()
        return self


class VStack:
    """
    Vertically arranged view
    """

    swift: list = [
        'VStack(alignment: .center, spacing: nil) {\n',
        '}\n'
    ]

    parameter = '{parameter}'
    alignment = '.center'
    spacing = 'nil'
    codes: list = []
    variables = []
    views = []

    def set_alignment(self, alignment: str):
        self.swift[0] = str(self.swift[0]).replace(self.alignment, f'.{alignment}', 1)
        self.alignment = f'.{alignment}'

    def set_spacing(self, spacing):
        self.swift[0] = str(self.swift[0]).replace(self.spacing, f'{spacing}', 1)
        self.spacing = f'{spacing}'

    def build(self):
        if len(self.codes) == 0:
            print('Wrong - VStack code is not set')

        code_list = [self.swift[0]]
        for code in self.codes:
            code_list.append(code)
        code_list.append(self.swift[1])

        code_str: str = ''
        for code_ in code_list:
            code_str += ('\t' + code_)

        return code_str

    def variable_build(self):
        return self.variables

    def add_view(self, view):
        self.views.append(view)
        self.codes.append(view.build())
        if len(view.variable_build()) != 0:
            self.variables += view.variable_build()


class Text:
    """
    Create text view
    """

    def __init__(self, text):
        if type(text) == str:
            self.text = text
            v_str = random.choice('abcdefghijklmnopqrstuvwxyz')
            for _ in range(0, 11):
                v_str += random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
            self.variable = f'var {v_str} = "{text}"'
            self.var = v_str
            print(f"$ Add variable: {v_str} = {text}, String")

    def variable_build(self):
        return [self.variable]

    def build(self):
        b_str = f'Text({self.var})\n'
        return b_str
