from turtle import *
speed(6)
width(3)
color("green") #ოთხკუთხედი
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(100) 

color("black") #კარი
begin_fill()
left(90) 
forward(150)
right(90)
forward(100)
right(90)
forward(150)
end_fill()

penup()
goto(300, 300)
pendown()

color("red") #სახურავი
begin_fill()
left(225)
forward(220)
left(92)
forward(213)
end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(137)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

penup()
goto(100, 200)
pendown()

begin_fill()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()