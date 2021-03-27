"""
Create various views
"""


class View:
    """
    View is the basis of all views
    """

    swift: str = (
        'struct {name}: View {\n'
        '\n'
        '    var body: some View {\n'
        '        {code}\n'
        '    }\n'
        '}\n'
    )

    code = '{code}'

    def __init__(self, name: str):
        self.name = name
        self.swift = self.swift.replace('{name}', self.name)

    def build(self):
        file = self.swift
        file = '//\n//  Created By PythonUI\n//\n\n' + file
        if self.code == '{code}' or self.code == ' ' or self.code == '':
            print(f'Wrong - {self.name} code is not set')
        return file


class VStack:
    """
    Vertically arranged view
    """

    swift: list = [
        'VStack(alignment: .center, spacing: nil) {\n',
        '}'
    ]

    parameter = '{parameter}'
    alignment = '.center'
    spacing = 'nil'
    codes: list = []

    def build(self):
        code_list = self.swift.copy()
        code_list.insert(1, self.codes)
        code_str = ''
        for code in code_list:
            code_str += code
        return code_str
