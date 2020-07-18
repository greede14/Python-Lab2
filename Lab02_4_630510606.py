#630510606
#อนาวิล อาทะวงศ์
#003-000
#Lab02_4

day = 86400000 #define in milisec
hour = 3600000
minute = 60000
second =  1000

m = int(input("Input number of milliseconds: "))
days = m/day #change milisec to day
hours = (m%day)/hour
minutes = (m%day%hour)/minute
seconds = (m%day%hour%minute)/second
m = (m%day%hour%minute%second)

print("Results = %i day(s), %i hour(s), %i minute(s), %i second(s), and %i millisec(s) " %(days,hours,minutes,seconds,m))