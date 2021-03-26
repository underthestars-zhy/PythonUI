"""
Create App, get manager, compile App to Swift
"""
import sys

import Platform


class App:
    swift: str = (
        "import SwiftUI\n"
        '@main\n'
        'struct {name}App: SwiftUI.App {\n'
        '    var body: some Scene {\n'
    )

    name = "{name}"

    def __init__(self, platform: str):
        if platform.lower() == "macos":
            self.platform = Platform.PlatformMac()
        else:
            print(f"Not supported on this platform: {platform}")
            sys.exit()

    def set_name(self, name: str):
        self.swift = self.swift.replace(self.name, name)
        self.name = name
