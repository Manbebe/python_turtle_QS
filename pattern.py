import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.shape(name="turtle")

for i in range(850):
  t.forward(i)
  t.left(850)
