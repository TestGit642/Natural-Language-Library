"""
ଏବେ ଆପଣଙ୍କ  କମ୍ପୁଟରରେ  Natural Language Library ଉପଲବ୍ଧ ହେଇଯାଇଥିବ |

N:B-ଆମ   Library ସବୁ  Editor,Python IDE ରେ ଚାଲିବ |

ଏବେ ଆମେ କେମିତି ବ୍ୟବହାର କରିବା ଆସନ୍ତୁ ଜାଣିବା

୧.ପ୍ରଥମେ ଆମେ ଯେକୌଣସି Editor କିମ୍ବା Python  Library ର ନାମ କୁ ଆମ ପ୍ରୋଗମ ରେ ଅବସ୍ତିତ କରିବା
ଉଦାହରଣ :
ପ୍ରଥମ  ଉପାୟ-from nllall import *
ଦ୍ୱିତୀୟ ଉପାୟ-import nllall
( ପ୍ରଥମ  ଉପାୟ ଓ ଦ୍ୱିତୀୟ ଉପାୟ ଭିତରୁ ଗୋଟିଏ  ଉପାୟ ବ୍ୟବହାର କରିପାରିବେ )

୨.ତା ପରେ ଆମେ  ଯଦି କିଛି ଆମେ ଆମ ମୁଦ୍ରଣ କରିବାକୁ ଚାଁହୁଥିବା  ବା  ଆଉଟପୁଟ୍ ରେ ଦେଖିବାକୁ ଚାଁହୁଥିବା
ସେଥିପାଇଁ ଆମେ ମୁଦ୍ରଣ ନାମକ କାର୍ଯ୍ୟ କୁ କଲ କରିବା  |
ଉଦାହରଣ :
from nllall import * #ପ୍ରଥମ  ଉପାୟ
ମୁଦ୍ରଣ("ନମସ୍କାର ବିଶ୍ୱବାସି")

ତା ପରେ ଏହି Programme କୁ Run button କୁ click  କରିବେ ତା ପରେ ଏହା ର ଆସିଯିବ  ଆଉଟପୁଟ୍  କିଛି ଏଭଳି

 ନମସ୍କାର ବିଶ୍ୱବାସି

୩.ତା ପରେ ଆମେ ଯଦି କିଛି ଉପଯୋଗକର୍ତ୍ତା ଇନପୁଟ୍ ନବାକୁ ଚାଁହୁଥିବା ବା କୀବୋର୍ଡ୍ ରେ ଇନପୁଟ୍ ନବାକୁ ଚାଁହୁଥିବା
ସେଥିପାଇଁ ଆମେ ନିବେଶ ନାମକ କାର୍ଯ୍ୟ କୁ କଲ କରିବା  |
from nllall import *
ବ=ନିବେଶ("କୀବୋର୍ଡ୍ କୁ କିଛି ଇନପୁଟ୍ ଦିଅ : ")
ମୁଦ୍ରଣ(ବ)

ତା ପରେ ଏହି Programme କୁ Run button କୁ click  କରିବେ ତା ପରେ ଏହା ର ଆସିଯିବ  ଆଉଟପୁଟ୍  କିଛି ଏଭଳି

କୀବୋର୍ଡ୍ କୁ କିଛି ଇନପୁଟ୍ ଦିଅ : କେନ୍ଦୁଝର
କେନ୍ଦୁଝର

4.ଏଭଳି ଆମ Library ରେ ବହୁତ ଗୁଡିଏ function ବା କାର୍ଯ୍ୟ ଅଛି ସେଗୁଡିକ ହେଲେ

୧.ନେଟୱର୍କ କାର୍ଯ୍ୟ
୨.ଗଣିତ କାର୍ଯ୍ୟ
୩.ଅକ୍ଷର ର ଖେଳ(string) କାର୍ଯ୍ୟ
୪.ଗ୍ରାଫିକ୍ସ କାର୍ଯ୍ୟ
୫.କ୍ରମ କାର୍ଯ୍ୟ
୬.ଖୋଜିବା କାର୍ଯ୍ୟ
୭.operating ସ୍ଵଷ୍ଟଏମ କାର୍ଯ୍ୟ
୮.platform କାର୍ଯ୍ୟ
୯.ତାରିଖ କାର୍ଯ୍ୟ
୧୦.ସମୟ କାର୍ଯ୍ୟ

ତ ଏଭଳି  ବହୁତ ଗୁଡିଏ କାର୍ଯ୍ୟ ଅଛି |

5.ଯଦି ଆପଣଙ୍କୁ କିଛି ଆସୁନି ତ ଆପଣ ଆମ ଲିବରେରୀ କୁ ସାହାଯ୍ୟ ମାଗିପାରିବେ ,ତ ସାହାଯ୍ୟ ମାଗିବାକୁ ହେଲେ ସାହାଯ୍ୟ କାର୍ଯ୍ୟ କୁ କଲ କରିବାକୁ ପଡିବ |
ଉଦାହରଣ :
ସାହାଯ୍ୟ("nllall")


"""

#socket module start

import socket  # ଏଠାରେ ଆମେ ଦୁଇଟି ମଡ୍ୟୁଲ୍, ସକେଟ୍ ଏବଂ ସମୟ ଆମଦାନୀ କରୁ
import time

def ହୋଷ୍ଟନାମ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ଏଠାରେ ଆମେ ଦୁଇଟି ମଡ୍ୟୁଲ୍, ସକେଟ୍ ଏବଂ ସମୟ ଆମଦାନୀ କରୁ
    # କିମ୍ବା ହୋଷ୍ଟ

    #ଲକ୍ଷ୍ୟ = input('ଆପଣ କ’ଣ ସ୍କାନ୍ କରିବାକୁ ଚାହୁଁଛନ୍ତି?: ')
    ଲକ୍ଷ୍ୟ = input('-->')
    # ପରବର୍ତ୍ତୀ ରେଖା ଆମକୁ ip ଠିକଣା ଦେଇଥାଏ |
    # ଲକ୍ଷ୍ୟସ୍ଥଳର
    ଲକ୍ଷ୍ୟ_ip = socket.gethostbyname(ଲକ୍ଷ୍ୟ)
    print('ହୋଷ୍ଟରେ ସ୍କାନ୍ ଆରମ୍ଭ କରିବା:', ଲକ୍ଷ୍ୟ_ip)


    # ପୋର୍ଟଗୁଡିକ ସ୍କାନ କରିବା ପାଇଁ କାର୍ଯ୍ୟ
    def port_scan(port):
        try:
            s.connect((ଲକ୍ଷ୍ୟ_ip, port))
            return True
        except:
            return False

    start = time.time()
    # ଏଠାରେ ଆମେ ପୋର୍ଟ 0 ରୁ 4 ସ୍କାନ୍ କରୁଛୁ |

    for port in range(5):   #ସେଠାରେ 65,535 ଟି Port ଅଛି |
        if port_scan(port):
            print(f'ପୋର୍ଟ {port} ଖୋଲା ଅଛି')
        else:
            print(f'ପୋର୍ଟ {port} ବନ୍ଦ ଅଛି')

    end = time.time()
    print(f' ସମୟ ନିଆଯାଇଛି {end - start:.2f} ସେକେଣ୍ଡ୍')

    #


#import module
import subprocess
#from englisttohindi.englisttohindi import EngtoHindi
# Traverse the ipconfig information
def ନେଟୱର୍କତଥ୍ୟ():
	ନେଟୱର୍କ_ତଥ୍ୟ = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')

	# Arrange the bytes data
	for item in ନେଟୱର୍କ_ତଥ୍ୟ:
		print(item.split('\r')[:-1])




#socket module end


#Math Module start
import math
ପାଇ=math.pi
ବର୍ଗମୂଳ=math.sqrt
ଘାତ=math.pow
ଗସାଗୁ=math.gcd
ଲସାଗୁ=math.lcm
ଫ୍ୟାକ୍ଟୋରିଆଲ୍=math.factorial
ରାଉଣ୍ଡଅପ୍=math.ceil
ରାଉଣ୍ଡକମ୍=math.floor
ଦଶମିକଭାଙ୍ଗ=math.modf
ଦଶମିକଭାଗକାଟ=math.trunc


def ଯୁକ୍ତ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def ଯୋଗ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def ମିଶାଣ(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def ବିୟୋଗ(x, y):
    result = x - y
    return result


#print(ବିୟୋଗ(1, 2))


# print(ମିଶାଣ(1,2,3,4,8,90,100))



def ବିଯୁକ୍ତ(x,y):
    result = x - y
    return result


#print(ବିଯୁକ୍ତ(126624654.2,2444646))


def ଗୁଣନ(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul
def ଭାଗ(x,y):
    result = x / y
    return result

def ହରଣ(x,y):
    result = x/y
    return result



#math module complete


#string module complete

ପ୍ରଥମବଡଅକ୍ଷରକର=str.capitalize
ବଡଅକ୍ଷରକୁସାନ=str.casefold
ସମସ୍ତଶବ୍ଦଓସଂଖ୍ୟା=str.isalnum
ବଡଛୋଟବଡ=str.swapcase
ଇଏଖାଲିଶବ୍ଦତ=str.isalpha
ଇଏଖାଲିସଂଖ୍ୟାତ=str.isdigit
ଇଏଠିକରୂପତ=str.isidentifier
ଇଏସାନଅକ୍ଷରତ=str.islower
ଇଏଲୋକାଲସଂଖ୍ୟାତ=str.isnumeric
ଇଏଫାଙ୍କାତ=str.isspace
ଇଏବଡତ=str.isupper
ସବୁକୁସାନ=str.lower
ସବୁକୁବଡ=str.upper
ବାମଫାଙ୍କାକୁକାଟ=str.lstrip
ଡାହାଣଫାଙ୍କାକୁକାଟ=str.rstrip
କେତେଟାଶବ୍ଦଅଛି=len
def ଅକ୍ଷରକୁଓଲଟାକର(a):
    return a[::-1]
# function which return reverse of a string

def ଓଲଟାସିଧାଓଲଟା(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


def ପ୍ରଥମବଡଶବ୍ଦ(str):
    for i in range(0, len(str)):

        if (str[i].istitle()):
            return str[i]

    return 0


def ଅଧିକଥିବାଶବ୍ଦ(a):
    max_frequency = {}
    for i in a:
       if i in max_frequency:
          max_frequency[i] += 1
       else:
          max_frequency[i] = 1
    my_result = max(max_frequency, key = max_frequency.get)
    return my_result

#string module Complete



#turtle module start





#ghanta function
import turtle
import datetime
def ଘଡ଼ି():
    currentDT = datetime.datetime.now()
    screen=turtle.Screen()
    trtl=turtle.Turtle()
    screen.setup(620,620)
    screen.bgcolor('black')
    clr=['red','green','blue','yellow','purple']
    trtl.pensize(4)
    trtl.shape('turtle')
    trtl.penup()
    trtl.pencolor('red')
    m=0
    for i in range(12):
          m=m+1
          trtl.penup()
          trtl.setheading(-30*i+60)
          trtl.forward(150)
          trtl.pendown()
          trtl.forward(25)
          trtl.penup()
          trtl.forward(20)
          trtl.write(str(m),align="center",font=("Arial", 12, "normal"))
          if m==12:
            m=0
          trtl.home()
    trtl.home()
    trtl.setpos(0,-250)
    trtl.pendown()
    trtl.pensize(10)
    trtl.pencolor('blue')
    trtl.circle(250)
    trtl.penup()
    trtl.setpos(150,-270)
    trtl.pendown()
    trtl.pencolor('olive')
    trtl.write((str(currentDT)),font=("Arial", 22, "normal"))
    trtl.ht()
    turtle.done()
#ଘଡ଼ି()
#animal function

import turtle as t
def କୁକୁର():
    t.screensize(500, 500)
    # 【 head outline 】
    t.pensize(5)
    t.home()
    t.seth(0)
    t.pd()  #pendown
    t.color('black')
    t.circle(20, 80)  # 0
    t.circle(200, 30)  # 1
    t.circle(30, 60)  # 2
    t.circle(200, 29.5)  # 3
    t.color('black')
    t.circle(20, 60)  # 4
    t.circle(-150, 22)  # 5
    t.circle(-50, 10)  # 6
    t.circle(50, 70)  # 7
    #  determine the approximate position of the nose t.xcor and t. ycor the position of the tortoise at the beginning
    x_nose = t.xcor()
    y_nose = t.ycor()
    t.circle(30, 62)  # 8
    t.circle(200, 15)  # 9
    # 【 nose 】
    t.pu() #penup
    t.goto(x_nose, y_nose + 25)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 eye 】
    t.pu()
    t.goto(x_nose + 48, y_nose + 55)
    t.seth(90)
    t.pd()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    # 【 ear 】
    t.pu()
    t.color('#444444')
    t.goto(x_nose + 100, y_nose + 110)
    t.seth(182)
    t.pd()
    t.circle(15, 45)
    t.color('black')
    t.circle(10, 15)
    t.circle(90, 70)
    t.circle(25, 110)
    t.rt(4)
    t.circle(90, 70)
    t.circle(10, 15)
    t.color('#444444')
    t.circle(15, 45)
    # 【 body 】
    t.pu()
    t.color('black')
    t.goto(x_nose + 90, y_nose - 30)
    t.seth(-130)
    t.pd()
    t.circle(250, 28)
    t.circle(10, 140)
    t.circle(-250, 25)
    t.circle(-200, 25)
    t.circle(-50, 85)
    t.circle(8, 145)
    t.circle(90, 45)
    t.circle(550, 5)
    # 【 tail 】
    t.seth(0)
    t.circle(60, 85)
    t.circle(40, 65)
    t.circle(40, 60)
    t.lt(150)  #left
    t.circle(-40, 90)
    t.circle(-25, 100)
    t.lt(5)
    t.fd(20)
    t.circle(10, 60)
    # 【 back 】
    t.rt(80)  #right
    t.circle(200, 35)
    # 【 collar 】
    t.pensize(20)
    t.color('#F03C3F')
    t.lt(10)
    t.circle(-200, 25)
    # 【 love bell 】
    t.pu()
    t.fd(18)
    t.lt(90)
    t.fd(18)
    t.pensize(6)
    t.seth(35)  #setheading
    t.color('#FDAF17')
    t.begin_fill()
    t.lt(135)
    t.fd(6)
    t.right(180)  #  brush turn around
    t.circle(6, -180)
    t.backward(8)
    t.right(90)
    t.forward(6)
    t.circle(-6, 180)
    t.fd(15)
    t.end_fill()
    # 【 front calf 】
    t.pensize(5)
    t.pu()
    t.color('black')
    t.goto(x_nose + 100, y_nose - 125)
    t.pd()
    t.seth(-50)
    t.fd(25)
    t.circle(10, 150)
    t.fd(25)
    # 【 posterior calf 】
    t.pensize(4)
    t.pu()
    t.goto(x_nose + 314, y_nose - 125)
    t.pd()
    t.seth(-95)
    t.fd(25)
    t.circle(-5, 150)
    t.fd(2)
    t.hideturtle()
    t.done()

#କୁକୁର()


def ପାଣ୍ଡା():
	pen = turtle.Turtle()

	# Defining method to draw a colored circle
	# with a dynamic radius
	def ring(col, rad):

		# Set the fill
		pen.fillcolor(col)

		# Start filling the color
		pen.begin_fill()

		# Draw a circle
		pen.circle(rad)

		# Ending the filling of the color
		pen.end_fill()

	##########################Main Section#############################

	# pen.up			 --> move turtle to air
	# pen.down		 --> move turtle to ground
	# pen.setpos		 --> move turtle to given position
	# ring(color, radius) --> draw a ring of specified color and radius
	###################################################################

	##### Draw ears #####
	# Draw first ear
	pen.up()
	pen.setpos(-35, 95)
	pen.down
	ring('black', 15)

	# Draw second ear
	pen.up()
	pen.setpos(35, 95)
	pen.down()
	ring('black', 15)

	##### Draw face #####
	pen.up()
	pen.setpos(0, 35)
	pen.down()
	ring('white', 40)

	##### Draw eyes black #####

	# Draw first eye
	pen.up()
	pen.setpos(-18, 75)
	pen.down
	ring('black', 8)

	# Draw second eye
	pen.up()
	pen.setpos(18, 75)
	pen.down()
	ring('black', 8)

	##### Draw eyes white #####

	# Draw first eye
	pen.up()
	pen.setpos(-18, 77)
	pen.down()
	ring('white', 4)

	# Draw second eye
	pen.up()
	pen.setpos(18, 77)
	pen.down()
	ring('white', 4)

	##### Draw nose #####
	pen.up()
	pen.setpos(0, 55)
	pen.down
	ring('black', 5)

	##### Draw mouth #####
	pen.up()
	pen.setpos(0, 55)
	pen.down()
	pen.right(90)
	pen.circle(5, 180)
	pen.up()
	pen.setpos(0, 55)
	pen.down()
	pen.left(360)
	pen.circle(5, -180)
	pen.hideturtle()
	turtle.done()
#ପାଣ୍ଡା()

#rainbow
def ଇନ୍ଦ୍ରଧନୁ():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
    turtle.done()


# Python program to draw square
# using Turtle Programming
#ଆୟତାକାର

def ଆୟତାକାର():
    skk = turtle.Turtle()

    for i in range(4):
        skk.forward(50)
        skk.right(90)

    turtle.done()


# Python program to draw star
# using Turtle Programming
def ତାରା():

    star = turtle.Turtle()

    star.right(75)
    star.forward(100)

    for i in range(4):
        star.right(144)
        star.forward(100)

    turtle.done()


# Python program to draw hexagon
# using Turtle Programming
def ଷଡ଼ଭୁଜ():

    polygon = turtle.Turtle()

    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)

    turtle.done()


#
# import for turtle module
def ଅଷ୍ଟାଭୁଜ():

# making a workScreen
    ws = turtle.Screen()

    # defining a turtle instance
    geekyTurtle = turtle.Turtle()

    # iterating the loop 8 times
    for i in range(8):
        # moving turtle 100 units forward
        geekyTurtle.forward(100)

        # turning turtle 45 degrees so
        # as to make perfect angle for an octagon
        geekyTurtle.left(45)
    turtle.done()





# draw any polygon in turtle

def ବହୁଭୁଜ():
# creating turtle pen
    t = turtle.Turtle()

    # taking input for the no of the sides of the polygon
    n = int(input("Enter the no of the sides of the polygon : "))

    # taking input for the length of the sides of the polygon
    l = int(input("Enter the length of the sides of the polygon : "))


    for _ in range(n):
        turtle.forward(l)
        turtle.right(360 / n)
    turtle.done()


# turtle library
#This to make turtle object
#tess=turtle.Turtle()

# self defined function to print coordinate
def ସଂଯୋଜନା():
    def buttonclick(x,y):
        print("ଆପଣ ଏହି ସ୍ଥାନରେ କ୍ଲିକ୍ କରିଛନ୍ତି ({0},{1})".format(x,y))

    #onscreen function to send coordinate
    turtle.onscreenclick(buttonclick,1)
    turtle.listen() # listen to incoming connections
    turtle.speed(10) # set the speed
    turtle.done() # hold the screen



#turtle complete





#sorting start


#bubble sort
def କ୍ରମ(list):

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
   return list
#bubble sort


#merge sort
def ଭାଗମିଶାଅକ୍ରମ(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = ଭାଗମିଶାଅକ୍ରମ(left_list)
   right_list = ଭାଗମିଶାଅକ୍ରମ(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

#merge sort
#insertion sort
def ବଡକ୍ରମ(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
# Compare the current element with next one
   while (InputList[j] > nxt_element) and (j >= 0):
      InputList[j+1] = InputList[j]
      j=j-1
   InputList[j+1] = nxt_element
   return InputList
#insertion_sort

#selection sort
def ଚୟନକ୍ରମ(inp):
   for idx in range(len(inp)):
      min_idx = idx
      for j in range( idx +1, len(inp)):
         if inp[min_idx] > inp[j]:
            min_idx = j
# Swap the minimum value with the compared value
   inp[idx], inp[min_idx] = inp[min_idx], inp[idx]
   return inp






#selection  sort


#linear search
def  ଖୋଜିବା(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
#binary search
def ଶୀଘ୍ରଖୋଜିବା(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

#jump search
import math
def ଅତିକ୍ରମକରିଖୋଜିବା(lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

#FibonacciSearch
def fs(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1
#InterpolationSearch
def ପ୍ରକ୍ଷେପ(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1



#sorting complete



#platform and os start
from os import *
from platform import *


def ଓଜନ(a):
    return path.getsize(a)  # file size in byte


def କଣଅଛି(a):
    return listdir(a)


def ଜାଣିନି(a):
    return help(a)


କେଉଁଜାଗା = getcwd()  # current directory o
ସଞ୍ଚାଳକ = processor()  # computer processor name p
ସଞ୍ଚାଳକସଂସ୍କରଣ = architecture()  # computer bit 32/64 p
ସଞ୍ଚାଳକନାମ = machine()  # amd64 p
କମ୍ପ୍ୟୁଟରନାମ = node()  # computer name p
ପରିଚାଳନାନାମସଂସ୍କରଣ = platform()  # osname p
ପରିଚାଳନାନାମ = system()  # which os

#platform and os complete



#other start

def ମିଥ୍ୟା():
    return False
def ସତ୍ୟ():
    return True

def ମୁଦ୍ରଣ(data):
    print(data)

# Input Function

def ନିବେଶ(data):  # input
    a = input(data)
    return a

#other complete

#datetime start


from datetime import datetime
now=datetime.now()
def ପୂର୍ଣ୍ଣତାରିଖସମୟ():
    return datetime.isoformat(now)

ତାରିଖ=datetime.today()
ପୂର୍ଣ୍ଣବାରତାରିଖବର୍ଷ=now.strftime("%A %m %Y")
ବାରତାରିଖବର୍ଷ=now.strftime("%a %m %y")
ସମୟ୧୨=now.strftime("%I %p %S")
ସମୟ୨୪=now.strftime("%H:%M:%S")



#date time complete

#help module
def ସାହାଯ୍ୟ(a):
    return help(a);