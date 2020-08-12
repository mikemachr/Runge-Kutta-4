import matplotlib.pyplot as plt
import math
import numpy as np
y=[]
def f(x,y):
    #enter function here, solve in terms dy/dx=....
    return float((20+7*math.sin(2*x)-y)/10)
h=float(input("Enter step\n"))
y.append(float(input("Enter initial condition y0\n")))
limit=int(input("Enter superior limit\n"))
x=np.linspace(0,limit,limit*limit)
for i in range (0,(len(x)-1)):
    k_1 = float(f(x[i],y[i]))
    k_2 = float(f(x[i]+0.5*h,y[i]+0.5*h*k_1))
    k_3 = float(f((x[i]+0.5*h),(y[i]+0.5*h*k_2)))
    k_4 = float(f((x[i]+h),(y[i]+k_3*h)))
    y.append(y[i] + (1/6)*(k_1+2*k_2+2*k_3+k_4)*h) 
plt.plot(x,y)
plt.ylabel("y")
plt.xlabel("time")
plt.title("Runge Kutta 4")
plt.xlim(left=0)
plt.show()

      