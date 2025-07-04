import matplotlib.pyplot as plt

def line_chart_app():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y, marker='o', color='blue')
    plt.title("Line Chart App")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def bar_chart_app():
    categories = ['A', 'B', 'C', 'D']
    values1 = [10, 20, 15, 25]
    values2 = [12, 18, 14, 22]

    x = range(len(categories))
    plt.bar(x, values1, width=0.4, label='2024', align='center')
    plt.bar([i + 0.4 for i in x], values2, width=0.4, label='2025', align='center')

    plt.xticks([i + 0.2 for i in x], categories)
    plt.title("Bar Chart Comparison")
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.legend()
    plt.show()

def pie_chart_app():
    sizes = [40, 30, 20, 10]
    labels = ['Python', 'JavaScript', 'C++', 'Java']
    explode = [0.1, 0, 0, 0]

    plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Pie Chart App")
    plt.axis('equal')
    plt.show()

def histogram_app():
    data = [12, 15, 13, 16, 18, 15, 14, 13, 14, 16, 17, 19, 15, 14, 13]

    plt.hist(data, bins=4, color='skyblue', edgecolor='black')
    plt.title("Histogram App")
    plt.xlabel("Value Range")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def scatter_plot_app():
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 6, 8, 7]
    colors = ['red', 'green', 'blue', 'purple', 'orange']

    plt.scatter(x, y, c=colors, s=100)
    plt.title("Scatter Plot App")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# === Main Menu ===
def main():
    while True:
        print("\nChoose a chart to display:")
        print("1. Line Chart")
        print("2. Bar Chart")
        print("3. Pie Chart")
        print("4. Histogram")
        print("5. Scatter Plot")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            line_chart_app()
        elif choice == '2':
            bar_chart_app()
        elif choice == '3':
            pie_chart_app()
        elif choice == '4':
            histogram_app()
        elif choice == '5':
            scatter_plot_app()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code provides a simple interactive menu to display various types of charts using Matplotlib.
# Each function creates a specific type of chart, and the main function allows users to choose which