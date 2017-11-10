/*
 * board.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "board.h"
#include "coord.h"
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>

#include "vertices.h"

Board::Board()
{
  std::memcpy(vertex, vertices, sizeof(vertex));
}

void Board::genSquare()
{
  std::vector<Coord> emptySquares;

  for(Coord i = {.x=0, .y=0}; i.y < 4; i.y++)
    {
      for(i.x = 0; i.x < 4; i.x++)
        {
          if(squareVal[i.x][i.y] == 0)
            emptySquares.push_back(i);
        }
    }

  // if there are no empty squares, you've lost
  if(emptySquares.empty())
    {
      printf("You loose!\n");
      return;
    }

  // pick a random empty square and initalize it
  int idx = rand() % emptySquares.size();
  int val = ((rand() % 2) + 1) * 2;
  setSquare(emptySquares[idx], val);

}

void Board::moveSquare(Coord origin, Coord dest)
{
  quad[dest.x][dest.y] = quad[origin.x][origin.y];
  quad[origin.x][origin.y] = QuadColor(0);

  squareVal[dest.x][dest.y] = squareVal[origin.x][origin.y];
  squareVal[origin.x][origin.y] = 0;
}

bool Board::mergeIfEqual(Coord origin, Coord dest)
{
  if(dest.x < 4 && dest.y < 4 &&
     squareVal[dest.x][dest.y] == squareVal[origin.x][origin.y])
    {
      // clear the 'from' square
      setSquare(origin, 0);

      // and update the value and color of the merging square
      squareVal[dest.x][dest.y] *= 2;
      quad[dest.x][dest.y] = QuadColor(squareVal[dest.x][dest.y]);
      return true;
    }
  return false;
}

void Board::up()
{
  Coord orig = {.x = 0, .y = 0};
  Coord dest = {.x = 0, .y = 0};

  bool movePossible, mergePossible;
  movePossible = mergePossible = false;

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
              Coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.y < 4)
                {
                  if(squareVal[dest.x][dest.y])
                    {
                      // another square was in the way (check later if equal values)
                      break;
                    }
                  movePossible = true;
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.y++;
                }

              mergePossible = mergeIfEqual(temp, dest);

            }

        }

    }

  if(movePossible || mergePossible)
    genSquare();

}

void Board::down()
{
  Coord orig = {.x = 0, .y = 0};
  Coord dest = {.x = 0, .y = 0};

  bool movePossible, mergePossible;
  movePossible = mergePossible = false;

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
              Coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.y > -1)
                {
                  if(squareVal[dest.x][dest.y])
                    {
                      // another square was in the way (check later if equal values)
                      break;
                    }
                  movePossible = true;
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.y--;
                }

              mergePossible = mergeIfEqual(temp, dest);

            }

        }

    }

  if(movePossible || mergePossible)
    genSquare();

}

void Board::right()
{
  Coord orig = {.x = 0, .y = 0};
  Coord dest = {.x = 0, .y = 0};

  bool movePossible, mergePossible;
  movePossible = mergePossible = false;

  // for all active squares
  for(orig.x = 2; orig.x > -1; orig.x--)  // begin at the second right-most row of the board (sqaures already at the rightmost edge have nowhere to go)
    {
      for(orig.y = 0; orig.y < 4; orig.y++)  // y-direction matters not
        {
          if(squareVal[orig.x][orig.y])
            {
              // move in the direction indicated until an active square is found or edge of board
              dest.x = orig.x + 1;
              dest.y = orig.y;
              Coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.x < 4)
                {
                  if(squareVal[dest.x][dest.y])
                    {
                      // another square was in the way (check later if equal values)
                      break;
                    }
                  movePossible = true;
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.x++;
                }

              mergePossible = mergeIfEqual(temp, dest);

            }

        }

    }

  if(movePossible || mergePossible)
    genSquare();

}

void Board::left()
{
  Coord orig = {.x = 0, .y = 0};
  Coord dest = {.x = 0, .y = 0};

  bool movePossible, mergePossible;
  movePossible = mergePossible = false;

  // for all active squares
  for(orig.x = 1; orig.x < 4; orig.x++)  // begin at the second left-most row of the board
    {
      for(orig.y = 0; orig.y < 4; orig.y++)  // y-direction matters not
        {
          if(squareVal[orig.x][orig.y])
            {
              // move in the direction indicated until an active square is found or edge of board
              dest.x = orig.x - 1;
              dest.y = orig.y;
              Coord temp = orig; // the square gets moved incrementally, therefore we need to keep the both the original location and a potentially temporary location (if multiple steps)

              while(dest.x > -1)
                {
                  if(squareVal[dest.x][dest.y])
                    {
                      // another square was in the way (check later if equal values)
                      break;
                    }
                  movePossible = true;
                  moveSquare(temp, dest);
                  temp = dest;
                  dest.x--;
                }

              mergePossible = mergeIfEqual(temp, dest);

            }

        }

    }

  if(movePossible || mergePossible)
    genSquare();

}

