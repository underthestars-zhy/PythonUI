from PythonUI import App

app = App.App(platform="macos")
app.set_name("Pu")
um = app.get_ui_manager()[0]
view = um.view('ContentView')
um.set_main_view(view)
app.build().save('/Users/zhuhaoyumbp15/Downloads/PythonUI')
