import App


app = App.App(platform="macos")
app.set_name("Pu")
print(app.get_swift_file_str()[0])
# app.platform.set_active()
print(app.platform.get_build_file())
