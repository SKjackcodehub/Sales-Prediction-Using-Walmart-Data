import matplotlib.pyplot as plt

# Example data (replace with your actual data)
accuracy_matlab = [80, 70, 80, 75,90 ]
existing_systems = [70, 60, 70, 65, 80]
time_points = [1, 2, 3, 4, 5]

# Create a line graph
plt.figure()
plt.plot(time_points, accuracy_matlab, 'r-d', linewidth=2, markersize=8)
plt.plot(time_points, existing_systems, 'b-o', linewidth=2, markersize=8)

# Add labels and a legend
plt.xlabel('Output Differences')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison: Exist Output vs Our Output')
plt.legend(['New Output', 'Existing Output'], loc='best')

# Customize the plot
plt.grid(True)
plt.tight_layout()

# You can save the plot as an image file if needed
# plt.savefig('accuracy_comparison_plot.png')

# Display the plot
plt.show()
