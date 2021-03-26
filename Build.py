"""
Compile file
"""

import os.path


class MacBuild:
    def __init__(self, file_dict: dict):
        self.file_dict = file_dict

    def save(self, path: str):
        abs_path = os.path.abspath(path)
        # print(abs_path)
        # print(self.file_dict)
        for file_path, content in self.file_dict.items():
            print('* Write content to ' + abs_path + f'/{file_path}')
            with open(abs_path + f'/{file_path}', 'w') as f:
                f.write(content)
        print('+ Build success')
