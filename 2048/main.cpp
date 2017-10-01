#include <GL/glut.h>
#include <cmath>
#include <cstdio>

#include "vertices.h"
#include "colors.h"

const int dim = 4;

typedef struct rgbColor
{
  GLfloat r,g,b;
} rgbColor;

class Board
{
  // The background color of a filled square
  static const rgbColor squareBackgroundColor;

public:
  void setSquare(int x, int y) { for(int i = 0; i < 4; colors[y][x][i++] = squareBackgroundColor); }

  // controls
  void up();
  void down();
  void right();
  void left();

  rgbColor colors[dim][dim][4];
};

const rgbColor Board::squareBackgroundColor = {.r=1.0, .g=0.8, .b=0.3};

void Board::up()
{
  // for all active squares

    // go in the direction indicated until an active square is found or edge of board

    // merge the squareas if their values are equal

  setSquare(0,0);
}

Board board;

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
  glClear(GL_COLOR_BUFFER_BIT);   // Clear the color buffer with current clearing color

  // enable vertex arrays
  glEnableClientState(GL_COLOR_ARRAY);
  glEnableClientState(GL_VERTEX_ARRAY);

  // before draw, specify vertex arrays
  glColorPointer(3, GL_FLOAT, 0, board.colors);
  glVertexPointer(2, GL_FLOAT, 0, vertices);

  glDrawArrays(GL_QUADS, 0, 4*dim*dim);

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

void keyboardCB(int key, int x, int y)
{

  switch(key)
  {
    case GLUT_KEY_UP:
      board.up();
      break;
    case GLUT_KEY_DOWN:
      break;
    case GLUT_KEY_LEFT:
      break;
    case GLUT_KEY_RIGHT:
      break;
  }

  glutPostRedisplay();
}

//Main program
int main(int argc, char **argv)
{
  // set a first two squares
  board.setSquare(0,1);
  board.setSquare(dim-1,1);

  glutInit(&argc, argv);
  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(50,50);
  glutInitWindowSize(325,325);
  glutCreateWindow(argv[0]);
  //glutTimerFunc(10, timerCB, 10);                 // redraw only every given millisec
  glutSpecialFunc(keyboardCB);
  //Call to the drawing function
  glutDisplayFunc(draw);
  //Background color
  glClearColor(0,0,0,1); // opaque
  glutMainLoop();
  return 0;
}
