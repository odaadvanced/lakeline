# 07_05_drawing.py

from guizero import *

app = App(width=400, height=200)
drawing = Drawing(app, width="fill", height="fill")
drawing.rectangle(20, 20, 300, 100, color="purple")
drawing.oval(30, 50, 290, 190, color="orange")
drawing.line(0, 0, 400, 200, color="black", width=5)
drawing.text(20, 100, "Hello World", color="black", font="Comic", size=48)
app.display()
