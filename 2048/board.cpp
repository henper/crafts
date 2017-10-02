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

void Board::up()
{
  // for all active squares
  for(int x = 0; x < 4; ++x)
    {
      for(int y = 0; y < 4; ++y)
        {
          if(squareVal[x][y])
            {
              // move in the direction indicated until an active square is found or edge of board
              int dy = y;
              while(dy<4)
                {
                  if(squareVal[x][dy] )
                    {

                    }
                  ++dy;
                }

              // merge the squares if their values are equal
            }

        }

    }
  setSquare(0,0,0);
}

