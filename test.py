import numpy as np
import matplotlib.pyplot as plt

# Example data (with some obvious outliers)
x = np.array([10, 11, 11, 12, 12, 12, 13, 13, 14, 15, 40, 45])

plt.figure(figsize=(6, 3))
plt.boxplot(
    x,
    vert=False,
    showfliers=True,   # show outlier points
    whis=1.5           # whiskers at 1.5 * IQR (default)
)
plt.title("Box Plot (Outliers shown as points)")
plt.xlabel("Value")
plt.tight_layout()
plt.show()