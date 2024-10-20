import matplotlib.pyplot as plt

nums = range(1,5001)
cubic_nums = [x**3 for x in nums]

print(plt.style.available) #styles availables
plt.style.use('seaborn-v0_8') #use a plot style
fig,ax = plt.subplots()
ax.scatter(nums,cubic_nums,c=cubic_nums,cmap=plt.cm.Greens,s=10)

#set chat title and label axes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of value", fontsize=14)

#set size of tick labels.
ax.tick_params(labelsize=8)

#set the range for each axis.
ax.axis([0,5100,0,140_000_000_000])
ax.ticklabel_format(style="sci")

#showing the plot
plt.show()