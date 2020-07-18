#630510606
#อนาวิล อาทะวงศ์
#003-000
#Lab02_2
h = float(input("Input height (m): ")) #get height and weight
if (h < 0) :
    h *= -1
if (h > 10000) :
    h /= 10000
elif (h > 1000) :
    h /= 1000
elif (h > 100) :
    h /= 100


w = float(input("Input weight (kg): "))
bmi = w/(h**2) #complie BMI
print("BMI is %.4f" % (bmi))