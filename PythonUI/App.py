"""
Create App, get manager, compile App to Swift
"""
import sys
from PythonUI import Build, Platform


class App:
    name = '{name}'
    view = '{view}'

    def __init__(self, platform: str):
        if platform.lower() == "macos":
            self.platform = Platform.PlatformMac()
        else:
            print(f"Not supported on this platform: {platform}")
            sys.exit()

    def set_name(self, name: str):
        self.platform.swift = self.platform.swift.replace(self.name, name)
        self.name = name
        return self

    def get_swift_file_str(self):
        return self.platform.swift, self

    def get_ui_manager(self):
        return self.platform.get_ui_manager(), self

    def when_active(self):
        self.platform.set_active()

    def build(self):
        if self.name == '{name}' or self.name == '' or self.name == ' ':
            print('Wrong - App name is not set')

        file_dict = {
            f"{self.name}App.swift": self.platform.build(),
        }

        for view in self.platform.ui_manager.views:
            file_dict[view.name + '.swift'] = view.build()

        if type(self.platform) == Platform.PlatformMac:
            return Build.MacBuild(file_dict=file_dict)
