
#include <cstdio>
#include <cstring>

#include <GL/glut.h>

#include "board.h"
#include "ai.h"

const int dim = 4;

Board board;

void type()
{
  char str[100];
  Coord pos;
  for(pos.x = 0; pos.x < 4; pos.x++)
    {
      for(pos.y = 0; pos.y < 4; pos.y++)
        {
          int num = board.squareVal[pos.x][pos.y];
          if(num)
            {
              sprintf(str, "%d", num);

              // Scale the numbers to fit nicely into a square, start width making sure that the width will fit
              // a mono font character is 119.05 units high and 33.33 units wide
              float scale = 1/(33.33*4*2); // should then supposedly fill one quarter of the screen (1/2 for -1 to +1 width)

              // Add consideration for number of digits
              int numDigits = strlen(str);
              scale /= numDigits; // will make any number of digits fit into the square

              // Having one giant digit fill the entire square looks odd, decreases readability, scale a lone digit down further
              if(numDigits == 1)
                {
                  scale /= 2;
                }

              float height = 119.05*scale;

              // convert from square index (0 to 3) to GL window position (-1 to +1)
              float x = pos.x/2.0 - 0.95; // -1 would be the leftmost edge
              float y = pos.y/2.0 - 0.75 - height/2.0; // half the text height down from the center of the square

              // b/c of the abnormal scale for one digit it has to be placed further right than the others to be in the middle
              if(numDigits == 1)
                {
                  x += 0.1;
                }

              glPushMatrix();
              glTranslatef(x, y, 0.0);
              //float scale = 1/(6*152.38);
              glScalef(scale, scale, scale);
              
              for( char* p = str; *p; p++)
              {
                  glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, *p);
              }
              glPopMatrix();

            }
        }
    }
}

//Drawing funciton
void draw(void)
{
  glClear(GL_COLOR_BUFFER_BIT);   // Clear the color buffer with current clearing color

  // enable vertex arrays
  glEnableClientState(GL_COLOR_ARRAY);
  glEnableClientState(GL_VERTEX_ARRAY);

  // before draw, specify vertex arrays
  glColorPointer(3, GL_FLOAT, 0, &board.quad[0][0].vertexColor.bottomLeft.r);
  glVertexPointer(2, GL_FLOAT, 0, &board.vertex[0][0].bottomLeft);

  glDrawArrays(GL_QUADS, 0, 4*dim*dim); //we're drawing QUADS hence the 4 indices per square

  glDisableClientState(GL_VERTEX_ARRAY);  // disable vertex arrays
  glDisableClientState(GL_COLOR_ARRAY);

  // After the quad vertices and colors have been drawn add the number on each square
  type();

  //Draw order
  glFlush();
}

void timerCB(int millisec)
{
    ai_main(&board);
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
      board.down();
      break;
    case GLUT_KEY_LEFT:
      board.left();
      break;
    case GLUT_KEY_RIGHT:
      board.right();
      break;
  }

  glutPostRedisplay();
}

void idleCB()
{
  ai_main(&board);
  glutPostRedisplay();
}

//Main program
int main(int argc, char **argv)
{
  // set first two squares
  board.genSquare();
  board.genSquare();

  /*
  Coord pos;
  pos.x=0; pos.y=0;
  board.setSquare(pos, 2);
  pos.x=1; pos.y=0;
  board.setSquare(pos, 2);
  pos.x=2; pos.y=0;
  board.setSquare(pos, 4);
  pos.x=3; pos.y=0;
  board.setSquare(pos, 8);
  */

  glutInit(&argc, argv);
  //Simple buffer
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition(1000,50);
  glutInitWindowSize(325,325);
  glutCreateWindow(argv[0]);

  // Register callback for AI function (only one!)
  glutTimerFunc(500, timerCB, 500);                 // redraw only every given millisec
  //glutIdleFunc(idleCB);

  // Register callback for player (keyboard) interaction (only one!)
  //glutSpecialFunc(keyboardCB);
  glutSpecialUpFunc(keyboardCB);

  //Make a first call to the drawing function
  glutDisplayFunc(draw);
  //Background color
  glClearColor(0,0,0,1); // opaque

  //Text properties
  glEnable(GL_LINE_SMOOTH);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  glLineWidth(3.0);
  glColor3f(0.2, 0.2, 0.2);

  glutMainLoop();
  return 0;
}
