/*
 * glutWrapper.c
 *
 *  Created on: Dec 26, 2018
 *      Author: eponhik
 */
#include <GL/glut.h>
#include "glutWrapper.h"

void glwInit(int* argc, char** argv, windowParamsS winp, callbacksS cb)
{
  glutInit(argc, argv); // what commannd line args are available in freeglut?

  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(winp.position.x,winp.position.y);
  glutInitWindowSize(winp.size.x,winp.size.y);
  glutCreateWindow(winp.title);

  // install callbacks
  glutIdleFunc(cb.idle);
  glutKeyboardUpFunc(cb.alphaKey);
  glutSpecialUpFunc(cb.specialKey);
  glutDisplayFunc(cb.window);

  // only install timer if given (avoid segfault)
  if (cb.timer != NULL && cb.period != 0)
    glutTimerFunc(cb.period, cb.timer, cb.period); // use the period as both the timeout value and the ID (the argument to timer callback)


  //Background color
  glClearColor(0,0,0,1); // opaque

  //Text properties
  glEnable(GL_LINE_SMOOTH);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  glLineWidth(3.0);
  glColor3f(0.2, 0.2, 0.2);
}

void glwMainLoop(void) { glutMainLoop(); }
