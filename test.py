import PythonUI
from PythonUI import App

app = App.App(platform="macos")
app.set_name("Pu")
um = app.get_ui_manager()[0]
view = um.view('ContentView')
um.set_main_view(view)
vstack = um.get_vstack()
vstack.set_alignment(PythonUI.Alignment.top)
vstack.set_spacing(1)
text = um.get_text(text="hi")
text.padding([PythonUI.EdgeSet.top], 2)
vstack.padding(PythonUI.EdgeSet.all, 3)
vstack.add_view(text)
text_2 = um.get_text(text="c")
vstack.add_view(text_2)
view.add_view(vstack)
app.build().save('/Users/zhuhaoyumbp15/Downloads/PythonUI')
