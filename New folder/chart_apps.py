import matplotlib.pyplot as plt

def plot_all_charts():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 5, 8, 12, 7]

    # 1. Line Chart
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("Line Chart")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    # 2. Bar Chart
    plt.subplot(2, 2, 2)
    plt.bar(x, y, color='orange')
    plt.title("Bar Chart")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # 3. Pie Chart
    plt.subplot(2, 2, 3)
    labels = ['A', 'B', 'C', 'D', 'E']
    plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Pie Chart")

    # 4. Scatter Plot
    plt.subplot(2, 2, 4)
    plt.scatter(x, y, color='green')
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_histogram():
    # Sample data for histogram
    data = [12, 15, 13, 16, 18, 15, 14, 13, 14, 16, 17, 19, 15, 14, 13]

    plt.figure(figsize=(6, 4))
    plt.hist(data, bins=5, color='purple', edgecolor='black')
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_all_charts()
    plot_histogram()
