
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
        float scale = 1/(MONOSPACE_CHAR_WIDTH*4*2); // should then supposedly fill one quarter of the screen (1/2 for -1 to +1 width)

        // Add consideration for number of digits
        int numDigits = strlen(str);
        scale /= numDigits; // will make any number of digits fit into the square

        // Having one giant digit fill the entire square looks odd, decreases readability, scale a lone digit down further
        if(numDigits == 1)
        {
          scale /= 2;
        }

        float height = MONOSPACE_CHAR_HEIGHT*scale;

        // convert from square index (0 to 3) to GL window position (-1 to +1)
        coord2dS coord = {.x = pos.x/2.0f - 0.95f,                // -1 would be the leftmost edge
                          .y = pos.y/2.0f - 0.75f - height/2.0f}; // half the text height down from the center of the square

        // b/c of the abnormal scale for one digit it has to be placed further right than the others to be in the middle
        if(numDigits == 1)
        {
          coord.x += 0.1;
        }

        glwStrokeMonospace(str, coord, scale);
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
  glwRedraw();
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

  glwRedraw();
}

void idleCB()
{
  ai_main(&board);
  glwRedraw();
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
