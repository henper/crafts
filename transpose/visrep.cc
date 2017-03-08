#include <GL/glut.h>
#include <cmath>
#include <cstdio>
#include "matrix.h"

#include "vertices.h"
#include "colors.h"

Matrix* A;
int dim;

void type(char* str)
{
  glPushMatrix();
  glTranslatef(-1.0, -1.0, 0.0);
  float scale = 1/(6*152.38);
  glScalef(scale, scale, scale);
  for( char* p = str; *p; p++)
  {
      glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, *p);
  }
  glPopMatrix();
}

//Drawing funciton
void draw(void)
{
  // iterative transpose
  int swaps = A->sqrTranspose();

  // prep swap counter string
  char str[20];
  std::sprintf(str, "SWAPS: %10d", swaps);

  glClear(GL_COLOR_BUFFER_BIT);   // Clear the color buffer with current clearing color

  // enable vertex arrays
  glEnableClientState(GL_COLOR_ARRAY);
  glEnableClientState(GL_VERTEX_ARRAY);

  // before draw, specify vertex arrays
  glColorPointer(3, GL_FLOAT, 0, colors);
  glVertexPointer(2, GL_FLOAT, 0, vertices);

  glDrawArrays(GL_QUADS, 0, 4*dim*dim);

  glDisableClientState(GL_VERTEX_ARRAY);  // disable vertex arrays
  glDisableClientState(GL_COLOR_ARRAY);

  type(str);
 
  //Draw order
  glFlush();
}

void timerCB(int millisec)
{
    glutTimerFunc(millisec, timerCB, millisec);
    glutPostRedisplay();
}

//Main program
int main(int argc, char **argv)
{
  dim = sqrt(sizeof(colors)/sizeof(colors[0])/4);
  A = new Matrix((quadRgb*)&colors, dim, dim);

  glutInit(&argc, argv);
  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(50,50);
  glutInitWindowSize(325,325);
  glutCreateWindow(argv[0]);
  glutTimerFunc(10, timerCB, 10);                 // redraw only every given millisec
  //Call to the drawing function
  glutDisplayFunc(draw);
  //Background color
  glClearColor(0,0,0,1); // opaque
  glutMainLoop();
  return 0;
}
