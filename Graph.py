# Load data
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("results.csv")

# 1. Nodes Expanded by Status per Heuristic
plt.figure(figsize=(10, 6))
for status in data['Status'].unique():
    subset = data[data['Status'] == status].groupby(
        'Heuristic')['NodesExpanded'].mean()
    plt.bar(subset.index + f"-{status}", subset.values, label=status)
plt.xticks(rotation=90)
plt.title('Nodes Expanded by Status per Heuristic')
plt.xlabel('Heuristic')
plt.ylabel('Average Nodes Expanded')
plt.legend(title='Status')
plt.tight_layout()
plt.savefig("graphs/Nodes_Expanded_by_Status_per_Heuristic.png")

# 2. Time Taken by Status per Heuristic
plt.figure(figsize=(10, 6))
for status in data['Status'].unique():
    subset = data[data['Status'] == status].groupby('Heuristic')['Time'].mean()
    plt.plot(subset.index, subset.values, label=status, marker='o')
plt.xticks(rotation=90)
plt.title('Time Taken by Status per Heuristic')
plt.xlabel('Heuristic')
plt.ylabel('Average Time (seconds)')
plt.legend(title='Status')
plt.tight_layout()
plt.savefig("graphs/Time_Taken_by_Status_per_Heuristic.png")

# 3. Nodes Expanded by Status and Algorithm
plt.figure(figsize=(10, 6))
for status in data['Status'].unique():
    subset = data[data['Status'] == status].groupby(
        'Algorithm')['NodesExpanded'].mean()
    plt.bar(subset.index + f"-{status}", subset.values, label=status)
plt.xticks(rotation=45)
plt.title('Nodes Expanded by Status and Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Average Nodes Expanded')
plt.legend(title='Status')
plt.tight_layout()
plt.savefig("graphs/Nodes_Expanded_by_Status_and_Algorithm.png")

# 4. Time Comparison by Status and Algorithm
plt.figure(figsize=(10, 6))
for status in data['Status'].unique():
    subset = data[data['Status'] == status].groupby('Algorithm')['Time'].mean()
    plt.plot(subset.index, subset.values, label=status, marker='o')
plt.xticks(rotation=45)
plt.title('Time Comparison by Status and Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Average Time (seconds)')
plt.legend(title='Status')
plt.tight_layout()
plt.savefig("graphs/Time_Comparison_by_Status_and_Algorithm.png")

# 5. Efficiency Comparison (Nodes Expanded vs. Time) by Status
plt.figure(figsize=(10, 6))
for status in data['Status'].unique():
    subset = data[data['Status'] == status]
    plt.scatter(subset['NodesExpanded'], subset['Time'], label=status)
plt.title('Efficiency Comparison: Nodes Expanded vs. Time by Status')
plt.xlabel('Nodes Expanded')
plt.ylabel('Time (seconds)')
plt.legend(title='Status')
plt.tight_layout()
plt.savefig("graphs/Efficiency_Comparison_Nodes_vs_Time_by_Status.png")
