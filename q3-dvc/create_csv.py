import os
import csv

files = []

for root, dirs, filenames in os.walk("data"):
    for filename in filenames:
        files.append(os.path.join(root, filename))

files.sort()

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename"])

    for file in files:
        writer.writerow([file])

print(f"Created data.csv with {len(files)} rows.")