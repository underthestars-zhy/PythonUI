# PythonUI
A complete framework for **developing Swift App using Python**

## Start

### Creat App

```python
from PythonUI import App

app = App.App(platform=str('macos'))
app.set_name(str("PuApp")) # Your App Name
```

### Creat View

```python
from PythonUI import App

app = App.App(platform=str('macos'))
um = app.get_ui_manager()[0]
view = um.view('ContentView')
# um.set_main_view(view)
```

### Build

```python
from PythonUI import App

app = App.App(platform=str('macos'))
app.build().save('')
```