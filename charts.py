import matplotlib.pyplot as plt

def category_chart():
    categories = ["life", "love", "truth", "humor", "inspirational"]
    values = [15, 12, 10, 8, 9]

    plt.figure(figsize=(8,5))
    plt.bar(categories, values)
    plt.title("Quote Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig("chart.png")
    return "chart.png"