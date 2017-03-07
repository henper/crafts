#include <GL/glut.h>
#include "matrix.h"

#include "vertices.h"
#include "colors.h"

Matrix* A;

//Drawing funciton
void draw(void)
{
  A->transpose();

  glClear(GL_COLOR_BUFFER_BIT);   // Clear the color buffer with current clearing color

  // enable vertex arrays
  glEnableClientState(GL_COLOR_ARRAY);
  glEnableClientState(GL_VERTEX_ARRAY);

  // before draw, specify vertex arrays
  glColorPointer(3, GL_FLOAT, 0, colors);
  glVertexPointer(2, GL_FLOAT, 0, vertices);

  glDrawArrays(GL_QUADS, 0, 4*16); //FIXME: hardcoded matrix size

  glDisableClientState(GL_VERTEX_ARRAY);  // disable vertex arrays
  glDisableClientState(GL_COLOR_ARRAY);
 
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
  A = new Matrix((quadRgb*)&colors, 4, 4); //FIXME: hardcoded matrix size

  glutInit(&argc, argv);
  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(50,50);
  glutInitWindowSize(325,325);
  glutCreateWindow(argv[0]);
  glutTimerFunc(33, timerCB, 33);                 // redraw only every given millisec
  //Call to the drawing function
  glutDisplayFunc(draw);
  //Background color
  glClearColor(0,0,0,1); // opaque
  glutMainLoop();
  return 0;
}
