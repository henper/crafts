/*
 * glutWrapper.c
 *
 *  Created on: Dec 26, 2018
 *      Author: eponhik
 */
#include <GL/glut.h>
#include "glutWrapper.h"

// define and declare private context
typedef struct contextS
{
  windowParamsS window;
  callbacksS    callbacks;
} contextS;
static contextS context;

static void glwDraw()
{
  glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer with current clearing color

  // enable vertex arrays
  glEnableClientState(GL_COLOR_ARRAY);
  glEnableClientState(GL_VERTEX_ARRAY);

  // before draw, specify vertex arrays
  glColorPointer(3, GL_FLOAT, 0, &context.window.colors->vertexColor.bottomLeft.r);
  glVertexPointer(2, GL_FLOAT, 0, &context.window.vertices->bottomLeft);

  glDrawArrays(GL_QUADS, 0, 4*context.window.length); //we're drawing QUADS hence the 4 indices per square

  glDisableClientState(GL_VERTEX_ARRAY);  // disable vertex arrays
  glDisableClientState(GL_COLOR_ARRAY);

  // call user defined draw function
  if(context.callbacks.draw)
    context.callbacks.draw();

  //Draw order
  glFlush();
}

void glwInit(int* argc, char** argv, windowParamsS winp, callbacksS cb)
{
  // save params in context
  context.window = winp;
  context.callbacks = cb;

  glutInit(argc, argv); // what commannd line args are available in freeglut?

  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(winp.position.x,winp.position.y);
  glutInitWindowSize(winp.size.x,winp.size.y);
  glutCreateWindow(winp.title);

  // install user defined callbacks
  glutIdleFunc(cb.idle);
  glutKeyboardUpFunc(cb.alphaKey);
  glutSpecialUpFunc(cb.specialKey);

  // install our own draw function (wich will call user defined draw callback)
  glutDisplayFunc(glwDraw);

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

void glwStrokeMonospace(char* str, coord2dS pos, float scale)
{
  glPushMatrix();
  glTranslatef(pos.x, pos.y, 0.0);
  glScalef(scale, scale, scale);
  
  for(char* p = str; *p; p++)
  {
    glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, *p);
  }
  glPopMatrix();
}

void glwMainLoop(void) { glutMainLoop(); }
void glwRedraw(void) { glutPostRedisplay(); }
