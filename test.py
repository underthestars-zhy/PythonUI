import App


app = App.App(platform="macos")
app.set_name("Pu")
print(app.get_swift_file_str()[0])
