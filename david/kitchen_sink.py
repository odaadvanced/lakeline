# 07_04_kitchen_sink.py

from guizero import *
def get_select(selected_value):
    print(selected_value)
app = App(title="Kitchen Sink", layout="grid", width=400, height=400)

# Row 0
Text(app, text="David Was Here!", grid=[0, 0])
TextBox(app, grid=[1, 0])
PushButton(app, text="Baguette", grid=[2, 0])

# Row 1
CheckBox(app, text="boxcheck", grid=[0, 1])
ListBox(app, items=["Taco", "Burger", "Pizza"], grid=[1, 1])
Combo(app, options=["I", "Am", "Watching", "You"], grid=[2, 1], command=get_select)

# Row 2
ButtonGroup(app, options=["portrait", "landscape"], selected="portrait", grid=[0, 2])
Slider(app, start=0, end=10, grid=[1, 2])
Picture(app, image="test.png", width=100, height=100, grid=[2, 2])

app.display()
