import sys
import array
from PIL import Image
import numpy as np
import random

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import cv2

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

class Texture( object ):
    """Texture either loaded from a file or initialised with random colors."""
    def __init__( self ):
        self.xSize, self.ySize = 0, 0
        self.rawRefence = None

class FileTexture( Texture ):
    """Texture loaded from a file."""
    def __init__( self, fileName ):
        im = Image.open('globe.png')
        self.xSize = im.size[0]
        self.ySize = im.size[1]
        self.imdata = np.fromstring(im.tobytes(), np.uint8)            

class VideoFileTexture( Texture ):
    """Texture loaded from a mp4 file."""
    def __init__( self, fileName ):
        self.filename = fileName
        self.video_capture = cv2.VideoCapture()

    def _get_video_frame(self):
        # get latest frame from video
        success, frame = self.video_capture.read()
        if success: return frame
     
        if not self.video_capture.isOpened():
            self.video_capture.open(self.filename)
        else:
            self.video_capture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)      
     
        return self.video_capture.read()[1]      

def cylinder():
    PI = 3.14159    
    resolution  = 0.5
    height = 2.0
    radius = 1.0

    glPushMatrix()
    glTranslatef(0, -1.1, 0)

    # glBegin(GL_TRIANGLE_FAN)
    # glTexCoord2f( 0.5, 0.5 )
    # glVertex3f(0, height, 0)    
    # for i in frange(2*PI, 0, -resolution):    
    #     glTexCoord2f( 0.5 * math.cos(i) + 0.5, 0.5 * math.sin(i) + 0.5 )
    #     glVertex3f(radius * math.cos(i), height, radius * math.sin(i))
    # #/* close the loop back to 0 degrees */
    # glTexCoord2f( 0.5, 0.5 )
    # glVertex3f(radius, height, 0)
    # glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in frange(0, 2*PI, resolution):        
        tc = ( i / (float)( 2*PI ) )
        glTexCoord2f( tc, 0.0 )
        glVertex3f(radius * math.cos(i), 0, radius * math.sin(i))
        glTexCoord2f( tc, 1.0 )
        glVertex3f(radius * math.cos(i), height, radius * math.sin(i))
        
    glTexCoord2f( 0.0, 0.0 )
    glVertex3f(radius, 0, 0)
    glTexCoord2f( 0.0, 1.0 )
    glVertex3f(radius, height, 0)
    glEnd()

    glPopMatrix()

def display():
    glClearColor( 0, 0, 0, 1 )
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    gluPerspective( 10, 1.0, 1.2, 50.0 )
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    glTranslatef( 0, tilt, zoom)
    glEnable( GL_CULL_FACE )
    glCullFace(GL_FRONT)
    glEnable( GL_DEPTH_TEST )
    
    glRotatef( pan, 0.0, 0.1, 0.0 )
    
    cylinder()
    glutSwapBuffers()

def timer( value ):
    global pan
    pan += 1;
    glutPostRedisplay()
    #glutTimerFunc( 16, timer, 0 )

pan = 0
tilt = 0
zoom = -8.1

def init():    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)    
    glutKeyboardFunc(keyboard)
    glutTimerFunc( 0, timer, 0 );
    glutIdleFunc(idle)  

def idle():
    tx_image = cv2.flip(frame._get_video_frame(), 1)
    tx_image = Image.fromarray(tx_image)
    ix = tx_image.size[0]
    iy = tx_image.size[1]    
    tx_image = tx_image.tobytes('raw', 'BGRX', 0, -1)    

    #print('[Frame size] Width '+str(ix)+ ' Height: '+str(iy))

    glClearColor ( 0, 0, 0, 0 )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, tx_image )        
    glEnable( GL_TEXTURE_2D )
    glutPostRedisplay()

def keyboard(key, x, y):    
    # Allow to quit by pressing 'Esc' or 'q'
    ch = key.decode("utf-8")    
    
    global pan
    global tilt
    global zoom
    
    if ch == chr(27):
        sys.exit()
    if ch == 'q':
        sys.exit()
    if ch == 'a':  
        pan -= 2     
        glutPostRedisplay()
    if ch == 'd':        
        pan += 2
        glutPostRedisplay()
    if ch == 'w':  
        tilt -= 0.1
        glutPostRedisplay()
    if ch == 's':        
        tilt += 0.1
        glutPostRedisplay()
    if ch == 'z':        
        zoom += 0.1        
        glutPostRedisplay()
    if ch == 'x':        
        zoom -= 0.1
        glutPostRedisplay()

def main():
    glutInit( sys.argv )
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB)

    glutInitWindowSize( 4096, 1264 )
    glutInitWindowPosition( 100, 100 )
    glutCreateWindow( sys.argv[0] )
    
    init()
    glutMainLoop(  )

frame = VideoFileTexture(sys.argv[1])
if __name__ == '__main__':
    main()