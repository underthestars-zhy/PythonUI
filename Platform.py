"""
Platform related documents
"""
import UIManager


class PlatformMac:
    swift: str = (
        "import SwiftUI\n"
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

    ui_managers = []
    used_scenePhase = False

    def get_ui_manager(self, name):
        ui_manager = UIManager.MacUIManager(name=name)
        self.ui_managers.append(ui_manager)
        return ui_manager

    def set_active(self):
        if not self.used_scenePhase:
            self.used_scenePhase = True
            self.swift = self.swift.replace('{scenePhase}', '@Environment(\\.scenePhase) private var scenePhase')

    def get_build_file(self):
        file = self.swift
        file = file.replace('    {scenePhase}\n', '')
        return file
