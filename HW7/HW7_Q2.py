#PYTHON contour plot

#IMPORT libraries
import matplotlib.pyplot as plt     #Matplotlib, pyplot and pylab are used for plotting graphs in Python
import numpy as np                  #Numpy is used for scientific computing in Python   

x = np.linspace(0, 2, 50)           # Return evenly spaced numbers over a specified interval (start, end(length), increments)
y = np.linspace(0, 2, 50)           # Return evenly spaced numbers over a specified interval (start, end(width), increments))
X, Y = np.meshgrid(x, y)            # Return coordinate matrices from coordinate vectors, X and Y are 2D arrays                       
Z = np.cos(Y) * np.sin(X)     # Z is the input formula. In this sample, sin(x) * cos(y) is used. Change to desired(deflection, Mx, My, etc.)


plt.figure(figsize=(10,8))          # Set the size of the figure
contourplt=plt.contourf(X, Y, Z, 10, cmap='Spectral_r')     #contourf is used for filled contour plots. 
                                                            # 10 is the number of contour lines. cmap is the color map. Spectral_r is the color map used in this sample. Change to desired color map.            
plt.clabel(contourplt,colors='g',inline=True, fontsize=10)  #configure contour plots. colors, inline, fontsize are optional

#legends and axis labels
plt.colorbar()                                               
plt.xlabel('X')
plt.ylabel('Y')