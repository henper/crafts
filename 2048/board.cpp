/*
 * board.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "board.h"
#include <cstring>

Board::Board()
{

}

void Board::moveSquare(coord origin, coord dest)
{
  quad[dest.x][dest.y] = quad[origin.x][origin.y];
  quad[origin.x][origin.y] = Quad(0);

  squareVal[dest.x][dest.y] = squareVal[origin.x][origin.y];
  squareVal[origin.x][origin.y] = 0;
}

void Board::up()
{
  coord orig = {.x = 0, .y = 0};
  coord dest = {.x = 0, .y = 0};

  // for all active squares
  for(orig.y = 2; orig.y > -1; orig.y--)  // begin at the second top-most row of the board (sqaures already at the top have nowhere to go)
    {
      for(orig.x = 0; orig.x < 4; orig.x++)  // x-direction matters not
        {
          if(squareVal[orig.x][orig.y])
            {
              // move in the direction indicated until an active square is found or edge of board
              dest.x = orig.x;
              dest.y = orig.y + 1;
              coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.y < 4)
                {
                  if(squareVal[dest.x][dest.y] )
                    {
                      break;
                    }
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.y++;
                }

              // merge the squares if their values are equal
            }

        }

    }

}

void Board::down()
{
  coord orig = {.x = 0, .y = 0};
  coord dest = {.x = 0, .y = 0};

  // for all active squares
  for(orig.y = 1; orig.y < 4; orig.y++)  // begin at the second bottom-most row of the board (sqaures already at the top have nowhere to go)
    {
      for(orig.x = 0; orig.x < 4; orig.x++)  // x-direction matters not
        {
          if(squareVal[orig.x][orig.y])
            {
              // move in the direction indicated until an active square is found or edge of board
              dest.x = orig.x;
              dest.y = orig.y - 1;
              coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.y > -1)
                {
                  if(squareVal[dest.x][dest.y] )
                    {
                      break;
                    }
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.y--;
                }

              // merge the squares if their values are equal
            }

        }

    }

}
