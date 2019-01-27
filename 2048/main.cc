
#include <cstdio>
#include <cstring>

#include <GL/glut.h>
#include "glutWrapper.h"

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
  // glutWrapper will take care of displaying the squares, we just need to add the numbers
  type();
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

  coord2dS size = {325, 325};
  windowParamsS win = {.title = "2048",
                       .position = {0},
                       .size = size,
                       .vertices = board.vertex[0],
                       .colors = board.quad[0],
                       .length = dim*dim};

  callbacksS cb = {.draw = draw,
                   .alphaKey = NULL,
                   .specialKey = keyboardCB,
                   .idle = NULL,
                   .timer = NULL,
                   .period = 0};

  glwInit(&argc, argv, win, cb);

  glwMainLoop();
  return 0;
}
