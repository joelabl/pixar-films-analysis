"""This script analyzes the Pixar People dataset separately for insights into team composition or
specific individuals' contributions."""

import matplotlib.pyplot as plt
from pixarfilms.datasets import load_people


pixar_people = load_people()
print("Pixar People Dataset Header")
print(pixar_people.head())

# Analyze team composition: Count roles and contributors
role_counts = pixar_people["role_type"].value_counts()
top_contributors = pixar_people["name"].value_counts().head(10)

# Plot the distribution of roles
plt.figure(figsize=(10, 6))
role_counts.plot(kind="bar")
plt.title("Distribution of Roles in Pixar Films")
plt.xlabel("Role Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot the top contributors
plt.figure(figsize=(10, 6))
top_contributors.plot(kind="bar")
plt.title("Top 10 Contributors to Pixar Films")
plt.xlabel("Name")
plt.ylabel("Number of Films Contributed")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Summary of unique contributors and their roles
unique_contributors = (
    pixar_people.groupby(["name", "role_type"]).size().reset_index(name="count")
)
print("Unique Contributors and Their Roles:")
print(unique_contributors.head(10))
