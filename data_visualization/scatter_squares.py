import matplotlib.pyplot as plt 

x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]
# plt.scatter(x_values, y_values, c=(0, 0, 0), edgecolor='none', s=10)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, edgecolor='none', s=10)
# replace 'viridis' with any name from https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py

# set chart title and lebel axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5000, 0, 120000000000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
