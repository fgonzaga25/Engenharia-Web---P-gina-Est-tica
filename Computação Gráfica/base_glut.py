from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import os  # Adicionando a importação do módulo 'os'
import numpy as np

janela = 0

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)  # Corrigindo para GL_PROJECTION
    glLoadIdentity()

def show_info():
    print('Empresa: ' + str(glGetString(GL_VENDOR).decode()))
    print('Modelo: ' + str(glGetString(GL_RENDERER).decode()))
    print('OpenGL: ' + str(glGetString(GL_VERSION).decode()))

def show_extensions():
    exts = glGetString(GL_EXTENSIONS).decode().split(' ')
    print('Extensoes ativas: ')
    for ext in exts:
        print(ext)

def desenha_tri():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5,-0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5,-0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0,0.5)
    glEnd()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    desenha_tri()
    glutSwapBuffers()

def keyboard(key, x, y):
    k = key.decode()
    if k == 'q':
        os._exit(0)

def main():
    print('Funcao principal')
    global janela

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitContextVersion(3, 2)
    glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)
    janela = glutCreateWindow('Janela inicial')
    glutDisplayFunc(render)
    glutKeyboardFunc(keyboard)
    InitGL()
    show_info()
    glutMainLoop()

if __name__ == '__main__':
    print("Aperte q para sair")
    main()
    