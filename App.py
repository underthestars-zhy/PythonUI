"""
Create App, get manager, compile App to Swift
"""
import sys

import Platform


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

    def get_ui_manager(self, name):
        return self.platform.get_ui_manager(name), self
