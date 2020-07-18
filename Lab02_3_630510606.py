#630510606
#อนาวิล อาทะวงศ์
#003-000
#Lab02_3

print("First Equation") #get data and keep it
m1 = float(input("Input m1: "))
b1 = float(input("Input b1: "))
print("Second Equation")
m2 = float(input("Input m2: "))
b2 = float(input("Input b2: "))

x = (b1 - b2)*(-1)/(m1 - m2) #complie Linear equation
y1 = (m1*x) + b1 #find y
y2 = (m2*x) + b2
print("The point of intersection is at x = %.2f and y = %.2f" % (x,y1))

