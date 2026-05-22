number=[10,20,30,40,50]
total=sum(number)
count=len(number)
mean=total/count
print("number:", number)
print("mean:", mean)
import numpy as np
import matplotlib.pyplot as plt
std=np.std(number)
print("Standard Deviation:", std)
plt.plot(number)
plt.title("My Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()