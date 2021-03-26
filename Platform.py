"""
Platform related documents
"""


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
