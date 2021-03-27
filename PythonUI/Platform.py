"""
Platform related documents
"""
from PythonUI import UIManager


class PlatformMac:
    swift: str = (
        "import SwiftUI\n\n"
        '@main\n'
        'struct {name}App: SwiftUI.App {\n'
        '    {scenePhase}\n'
        '    var body: some Scene {\n'
        '        WindowGroup {\n'
        '            {view}\n'
        '        }\n'
        '    }\n'
        '}'
    )

    used_scenePhase = False

    def __init__(self):
        self.ui_manager = UIManager.MacUIManager(platform=self)

    def get_ui_manager(self):
        return self.ui_manager

    def set_active(self):
        if not self.used_scenePhase:
            self.used_scenePhase = True
            self.swift = self.swift.replace('{scenePhase}', '@Environment(\\.scenePhase) private var scenePhase')

    def build(self):
        file = self.swift
        file = file.replace('    {scenePhase}\n', '')
        file = '//\n//  Created By PythonUI\n//\n\n' + file
        return file
