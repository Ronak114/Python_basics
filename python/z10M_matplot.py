import matplotlib.pyplot as plt
import numpy as np
import random

# Step 1: Generate Student IDs and Marks
students = list(range(1, 11))
marks = [random.randint(20, 100) for _ in students]

# Step 2: Study Matplotlib Basics
# Let's create various types of plots

# Step 3: Line Plot
plt.figure(figsize=(10, 4))
plt.subplot(2, 3, 1)
plt.plot(students, marks, linestyle='-', marker='o', color='b')
plt.title('Line Plot')
plt.xlabel('Student')
plt.ylabel('Marks')

# Step 4: Bar Graph
plt.subplot(2, 3, 2)
plt.bar(students, marks, color='g')
plt.title('Bar Graph')
plt.xlabel('Student')
plt.ylabel('Marks')

# Step 5: Scatter Plot
plt.subplot(2, 3, 3)
plt.scatter(students, marks, marker='*', color='r')
plt.title('Scatter Plot')
plt.xlabel('Student')
plt.ylabel('Marks')

# Step 6: Histogram
plt.subplot(2, 3, 4)
plt.hist(marks, bins=10, color='m')
plt.title('Histogram')
plt.xlabel('Marks')
plt.ylabel('Frequency')

# Step 7: Pie Chart
plt.subplot(2, 3, 5)
labels = [f"Student {s}" for s in students]
plt.pie(marks, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')

# Step 8: Display the Plots
plt.tight_layout()
plt.show()