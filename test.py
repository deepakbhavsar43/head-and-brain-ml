# from scipy import stats
# import matplotlib.pyplot as plt
#
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# print(slope, intercept, r, p, std_err, "\n\n")
#
#
# def myfunc(x):
#     print("x : ", x)
#     return slope * x + intercept
#
#
# mymodel = list(map(myfunc, x))
# print(mymodel)
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10)

# Plot the data
plt.plot(x, x, label='linear')
plt.scatter([2,5,4,7,8,9,6,3,1,5],[4,5,8,6,3,2,7,8,4,5])
# Add a legend
plt.legend()

# Show the plot
plt.show()