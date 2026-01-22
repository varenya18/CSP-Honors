import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv

def hue_to_rgb(hue):
    """Convert hue (0-360) to RGB color"""
    return mcolors.hsv_to_rgb([hue / 360.0, 1.0, 1.0])

# read the CSV file
lines = []
with open('lines.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        lines.append({
            'x1': int(row['x1']),
            'y1': int(row['y1']),
            'x2': int(row['x2']),
            'y2': int(row['y2']),
            'hue': int(row['hue'])
        })

# make the plot
fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
ax.set_facecolor('black')

# draw each line
for line in lines:
    color = hue_to_rgb(line['hue'])
    ax.plot([line['x1'], line['x2']], [line['y1'], line['y2']],
            color=color, linewidth=1.5)

ax.set_aspect('equal')
ax.set_xlim(-180, 180)
ax.set_ylim(-180, 180)

ax.axis('off')

plt.tight_layout()
plt.savefig('string_art.png', facecolor='black', dpi=150)
plt.show()

print("Saved to string_art.png")