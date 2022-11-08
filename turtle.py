from turtle import *

#draw a Turtlestar
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


#draw a Skycraper
x=input()
for i in range(0,x):
    for i in range(0,x-i-1):
        print' ',
         for i in range(0,i+1):
         print'*',
    print
