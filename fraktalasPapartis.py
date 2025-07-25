import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

ITER_COUNT = 800000 # adjust for more detail or more speed
# 800000 is a good balance for a 9:16 image
x, y = [], []

def piesimas():
    xn, yn = 0, 0
    for i in tqdm(range(ITER_COUNT)):
        rng = random.random()
        if rng < 0.01:
            xn, yn = 0, 0.16 * yn
        elif rng < 0.86:  
            xn, yn = 0.85 * xn + 0.04 * yn, -0.04 * xn + 0.85 * yn + 1.6
        elif rng < 0.93:
            xn, yn = 0.2 * xn - 0.26 * yn, 0.23 * xn + 0.22 * yn + 1.6
        else:
            xn, yn = -0.15 * xn + 0.28 * yn, 0.26 * xn + 0.24 * yn + 0.44
        x.append(xn)
        y.append(yn)

# gen points
piesimas()

# numpy supremac
x = np.array(x)
y = np.array(y)

y_norm = (y - y.min()) / (y.max() - y.min())

#vertical gradient from orange to yellow
from matplotlib.colors import LinearSegmentedColormap
gradient_cmap = LinearSegmentedColormap.from_list("fern_gradient", ["orange", "yellow"]) # create a gradient colormap

# 9:16 vertical
dpi_value =  100  # dots per inch
vertical_size = 3840  # height in pixels
horizontal_size = int(vertical_size * 9 / 16)  # width in pixels
fig = plt.figure(figsize=(horizontal_size / dpi_value, vertical_size / dpi_value),
                 dpi=dpi_value, facecolor="black")

ax = plt.gca()
ax.set_facecolor("black")


plt.scatter(x, y, c=y_norm, cmap=gradient_cmap, s=0.8) 

# trinu lauk nesamones
plt.axis('off')
plt.margins(0)
plt.gca().set_aspect('auto')

# savingzz
plt.savefig("barnsley_fern_9x16_gradient.png", dpi=dpi_value, 
            bbox_inches='tight', pad_inches=0, facecolor="black")
plt.show()


