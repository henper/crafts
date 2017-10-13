/*
 * ai.cpp
 *
 *  Created on: Oct 6, 2017
 *      Author: henper
 */

#include "ai.h"
#include <vector>

struct square
{
 int value;
 coord pos;
};

void addAllSquares(std::vector<square>& listRef, Board* board)
{
  listRef.reserve(16);
  coord pos;
  square elem;
  for(pos.x = 0; pos.x < 4; pos.x++)
    {
      for(pos.y = 0; pos.y < 4; pos.y++)
        {
          elem.pos = pos;
          elem.value = board->squareVal[pos.x][pos.y];
          listRef.push_back(elem);
        }
    }
}

std::vector<coord> addNeighbourSquares(coord origin, Board* board)
{
  std::vector<coord> neighbours;

  // Handle the cases in columns from left to right
  switch(origin.x) //left edge
  {
  case 0:
    {
      switch(origin.y)
      {
      case 3: // handle top left square
        neighbours = {             {.x=1, .y=3},
                     {.x=0, .y=2}, {.x=1, .y=2}};
        break;
      case 2:
      case 1: // handle the two middle squares
        neighbours = {{.x=0, .y=origin.y+1}, {.x=1, .y=origin.y+1},
                                             {.x=1, .y=origin.y},
                      {.x=1, .y=origin.y-1}, {.x=1, .y=origin.y-1}};
        break;
      case 0: // handle bottom left square
        neighbours = {{.x=0, .y=1}, {.x=1, .y=1},
                                    {.x=1, .y=0}};
        break;
      }
      break;
    }
  case 1:
  case 2: // handle the two middle columns
    {
      switch(origin.y)
      {
      case 3: // handle the two top middle squares
        neighbours = {{.x=origin.x-1, .y=3},                      {.x=origin.x+1, .y=3},
                      {.x=origin.x-1, .y=2}, {.x=origin.x, .y=2}, {.x=origin.x+1, .y=2}};
        break;
      break;
      case 2:
      case 1: // handle the four middle squares
        neighbours = {{.x=origin.x-1, .y=origin.y+1}, {.x=origin.x, .y=origin.y+1}, {.x=origin.x+1, .y=origin.y+1},
                      {.x=origin.x-1, .y=origin.y  },                               {.x=origin.x+1, .y=origin.y  },
                      {.x=origin.x-1, .y=origin.y-1}, {.x=origin.x, .y=origin.y-1}, {.x=origin.x+1, .y=origin.y-1}};
        break;
      case 0: // handle the two bottom middle squares
        neighbours = {{.x=origin.x-1, .y=1}, {.x=origin.x, .y=1}, {.x=origin.x+1, .y=1},
                      {.x=origin.x-1, .y=0},                      {.x=origin.x+1, .y=0}};
        break;
      }
      break;
    }
  case 3: // right edge
    {
      switch(origin.y)
      {
      case 3: // handle top right square
        neighbours = {{.x=2, .y=3},
                      {.x=2, .y=2}, {.x=3, .y=2}};
        break;
      case 2:
      case 1: // handle the two middle squares
        neighbours = {{.x=2, .y=origin.y+1}, {.x=3, .y=origin.y+1},
                      {.x=2, .y=origin.y},
                      {.x=2, .y=origin.y-1}, {.x=3, .y=origin.y-1}};
        break;
      case 0: // handle bottom left square
        neighbours = {{.x=2, .y=1}, {.x=3, .y=1},
                      {.x=2, .y=0}};
        break;
      }
      break;
    }
  }


  return neighbours;
}


square findHighestValueIn(std::vector<square>& searchSpace, int maxVal=0)
{
  int highestValue = 0;
  int highestIndex = 0;
  for(int i = 0; i < searchSpace.size(); ++i)
    {
      if(searchSpace.at(i).value > highestValue) //how to handle equal squares?
        {
          highestValue = searchSpace.at(i).value;
          highestIndex = i;
        }
    }

  return (searchSpace.at(highestIndex));
}

void ai_main(Board* board)
{
  // TODO:Place super smart AI here
  //
  // Get information on the board state from the reference passed in.
  // When this function returns the board state will be redrawn.
  // You can make multiple moves on the board but if you want all of them shown
  // make only one move and then exit.

  // Find the position of the highest valued square NOT already in sequence, i.e 256 > 128 > 64 > _8_
  std::vector<square> squaresToSearch;
  addAllSquares(squaresToSearch, board);

  square highestValueSquare = findHighestValueIn(squaresToSearch);

  // Find the highest value in sequence of the highest square

}


