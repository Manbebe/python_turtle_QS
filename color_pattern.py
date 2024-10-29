import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.shape(name="turtle")


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'teal', 'purple', 'black']


for i in range(5000):
  t.forward(i)
  t.color(colors[i % len(colors)])
  t.left(500)
