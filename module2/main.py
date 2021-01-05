from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

img = Image.open("rings.png")
rgb_img = img.convert('RGB')

# getting pixels
res = []
for i in range(0, rgb_img.width):
    res.append(255-rgb_img.getpixel((i, 300))[1])
res = res[100:550]

# find min and max
maxs = argrelextrema(np.array(res), np.greater)[0]
mins = argrelextrema(np.array(res), np.less)[0]

# visibility function
min_len = min(len(maxs), len(mins))
maxs = maxs[:min_len]
mins = mins[:min_len]
vis_list = []
i=0
while i < len(mins)-1:
    if maxs[i] > mins[i]:
        prev_max_v = (maxs[i] - mins[i]) / (maxs[i] + mins[i])
        vis_list.append(prev_max_v)
    if maxs[i+1] > mins[i]:
        next_max_v = (maxs[i+1] - mins[i]) / (maxs[i+1] + mins[i])
        vis_list.append(next_max_v)
    i += 1

# approximation
y = vis_list
x = range(0, len(y))
t = np.polyfit(x, y, 4)
f = np.poly1d(t)

# saving results
res_coof = open("results/res_aprox_coof.txt", 'w')
res_coof.write(str(f))

plt.grid()
plt.title("V(r)")
plt.xlabel("r")
plt.ylabel("V")
plt.plot(x, y, 'o', x, f(x), 'b')
plt.savefig("results/res_plot.png")



