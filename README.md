# Intro.
This repository contains implementation of rendering stiched video sequence onto cylinder-like (180 degrees) surface.

# Prerequisites.
Assignment was implemented in Python using PyOpenGL API. Majority of the code contains OpenGL calls, hence the code can be easily rewritten in another programming language. I'm using iOS but code is platform-independent. 
In order to run the code you need to take several easy installation steps:

###### 1. Python
I'm using Anaconda's Python 3.5 distribution. To install Anaconda go to: https://www.anaconda.com/download/#macos for iOS installation, https://www.anaconda.com/download/#linux for Linux machine and https://www.anaconda.com/download/#windows for Windows.
###### 2. Numpy
Anaconda already contains numpy, however if you're using different distribution go to https://scipy.org/install.html for installation details.
###### 3. PIL (pillow)
Library needed for opening video file. I've used pip for installation: **pip install pillow**
###### 4. OpenCV
Library needed for video preprocessing. You can install it with: **pip install opencv-python**
###### 5. PyOpenGL
PyOpenGL can be easily installed with pip: **pip install PyOpenGL PyOpenGL_accelerate**. Otherwise, refer to http://pyopengl.sourceforge.net/documentation/installation.html for installation guidelines. 

**You can now run the code!**

# I DIDN'T INCLUDE VIDEO FILE TO REPOSITORY.
You can download a video and change the name accordingly. **After that, place the file in the same folder with python source file (source folder) and pass the file name as program parameter. Example: python texturedCylinder_video.py video.mp4**

# Running the program: 
From terminal in source folder: **python texturedCylinder_video.py filename**

# Snapshots
![alt text](https://github.com/dimahwang88/bepro_pjt/blob/master/snapshots/Screenshot%20at%20Aug%2028%2023-19-06.png)
**You can rotate the surface to left by pressing 'a' on the keyboard:**
![alt text](https://github.com/dimahwang88/bepro_pjt/blob/master/snapshots/Screenshot%20at%20Aug%2028%2023-19-40.png)
**or to right by pressing 'd':**
![alt text](https://github.com/dimahwang88/bepro_pjt/blob/master/snapshots/Screenshot%20at%20Aug%2028%2023-20-03.png)

**You can exit the program by pressing 'Esc' button.**
