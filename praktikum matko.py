#Membuat grafik sinus atau trigonometri
import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100) #-pi<= x <= pi

# the function, which is y = sin(x) here
y = np.sin(x) + np.cos(x) #persamaan 1
y1 = np.cos(x) + np.tan(x) #persamaan 2
y2 = np.arctan(x) - np.tan(x) #persamaan 3
y3 = np.arcsin(x) * np.cos(x) + np.tan(x)/np.sin(x) #persamaan 4
y4 = np.sin(x) / np.tan(x) #persamaan 5

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'b-',) #garis warna biru
plt.plot(x,y1, 'g-') #garis warna hijau
plt.plot(x,y2, 'r-') #garis warna merah
plt.plot(x,y3, 'c-') #garis warna cyan
plt.plot(x,y4, 'y-') #garis warna kuning

# show the plot
plt.show()