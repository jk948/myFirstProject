import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,8,16,32]

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("This is the title")
plt.show()

plt.savefig("plot.png")
