import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. Load the dataset
# ==========================================

df = pd.read_csv("students.csv")


# ==========================================
# 2. Calculate student averages
# ==========================================

df["Average"] = df[
    ["Math", "Physics", "Computer_Science"]
].mean(axis=1)


# ==========================================
# 3. Find the best student
# ==========================================

best_student = df.loc[df["Average"].idxmax()]

print("\nBest student:")
print(best_student[["Student", "Average"]])


# ==========================================
# 4. Analyze study hours
# ==========================================

correlation = df["Study_Hours"].corr(df["Average"])

print("\nCorrelation between study hours and average:")
print(round(correlation, 2))


# ==========================================
# 5. Find the Top 5 students
# ==========================================

top_5 = df.nlargest(5, "Average")

print("\nTop 5 students:")
print(top_5[["Student", "Average"]])


# ==========================================
# 6. Visualize study hours vs average
# ==========================================

plt.scatter(df["Study_Hours"], df["Average"])

plt.xlabel("Study Hours")
plt.ylabel("Average")
plt.title("Study Hours vs Student Average")

plt.show()


# ==========================================
# 7. Visualize Top 5 students
# ==========================================

plt.bar(top_5["Student"], top_5["Average"])

plt.xlabel("Student")
plt.ylabel("Average")
plt.title("Top 5 Students by Average")

plt.show()
