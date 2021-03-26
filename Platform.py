"""
Platform related documents
"""
import UIManager


class PlatformMac:
    swift: str = (
        "import SwiftUI\n"
        '@main\n'
        'struct {name}App: SwiftUI.App {\n'
        '    var body: some Scene {\n'
        '        WindowGroup {\n'
        '            {view}\n'
        '        }\n'
        '    }\n'
        '}'
    )

    ui_managers = []

    def get_ui_manager(self, name):
        ui_manager = UIManager.MacUIManager(name=name)
        self.ui_managers.append(ui_manager)
        return ui_manager
