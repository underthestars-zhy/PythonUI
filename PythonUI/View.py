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
