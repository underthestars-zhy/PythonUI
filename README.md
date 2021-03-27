# PythonUI
A complete framework for **developing Swift App using Python**

## Start

### Creat App

```python
from PythonUI import App

app = App.App(platform=str('macos'))
app.set_name(str("PuApp")) # Your App Name
```

### Build

```python
from PythonUI import App

app = App.App(platform=str('macos'))
app.build().save('')
```

## View

### Creat View

```python
from PythonUI import App

app = App.App(platform=str('macos'))
um = app.get_ui_manager()[0]
view = um.view('ContentView')
# um.set_main_view(view)
```

### Creat && Add VStack

```python
from PythonUI import App
import PythonUI

app = App.App(platform=str('macos'))
um = app.get_ui_manager()[0]
view = um.view('ContentView')
vstack = um.get_vstack()
vstack.set_alignment(PythonUI.Alignment.top) # Set Alignment
vstack.set_spacing(1) # Set Spacing
view.add_view(vstack)
```