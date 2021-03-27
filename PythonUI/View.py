"""
Create various views
"""
import PythonUI


class View:
    """
    View is the basis of all views
    """

    swift: str = (
        'struct {name}: View {\n'
        '\n'
        '    var body: some View {\n'
        '    {code}\n'
        '    }\n'
        '}\n'
    )

    code = '{code}'
    view = None

    def __init__(self, name: str):
        self.name = name
        self.swift = self.swift.replace('{name}', self.name)

    def build(self):
        file = self.swift
        file = '//\n//  Created By PythonUI\n//\n\n' + file
        file = file.replace('{code}', self.code)
        if self.code == '{code}' or self.code == ' ' or self.code == '':
            print(f'Wrong - {self.name} code is not set')
        return file

    def add_view(self, view):
        self.code = view.build()
        self.view = view
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

    def set_alignment(self, alignment: str):
        self.swift[0] = str(self.swift[0]).replace(self.alignment, f'.{alignment}', 1)
        self.alignment = f'.{alignment}'


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
