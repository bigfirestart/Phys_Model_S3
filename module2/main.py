from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
from scipy.interpolate import interp1d
import pandas as pd

img = Image.open("rings.png")

rgb_img = img.convert('RGB')

res = []
for i in range(0, rgb_img.width):
    res.append(255-rgb_img.getpixel((i, 300))[1])


res = res[0:550]

# find min and max
maxs = argrelextrema(np.array(res), np.greater)[0]
mins = argrelextrema(np.array(res), np.less)[0]

# visibility function
min_len = min(len(maxs), len(mins))
maxs = maxs[:min_len]
mins = mins[:min_len]
vis_list = []
i=1
while i < len(maxs)-1:
    prev_max_v = (maxs[i] - mins[i-1]) / (maxs[i] + mins[i-1])
    vis_list.append(prev_max_v)
    next_max_v = (maxs[i] - mins[i]) / (maxs[i] + mins[i])
    vis_list.append(next_max_v)
    i += 1

# interpolation

y = list(filter(lambda a: a > 0, vis_list))
x = range(0, len(y))
t = np.polyfit(x, y, 4)
f = np.poly1d(t)
plt.grid()
plt.plot(x, y, 'o', x, f(x), 'b')
plt.show()



