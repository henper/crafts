/*
 * ai.cpp
 *
 *  Created on: Oct 6, 2017
 *      Author: henper
 */

#include "ai.h"
#include <vector>
#include <algorithm>

struct square
{
  int value;
  Coord pos;

  bool operator < (const square& sqr) const
  {
    return (value < sqr.value);
  }
};

void addAllSquares(std::vector<square>& listRef, Board* board)
{
  listRef.reserve(16);
  Coord pos;
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

std::vector<Coord> addNeighbourSquares(Coord origin)
{
  std::vector<Coord> neighbours;

  // Handle the cases in columns from left to right
  switch(origin.x) //left edge
  {
  case 0:
    {
      switch(origin.y)
      {
      case 3: // handle top left square
        neighbours = {             {.x=1, .y=3},
                     {.x=0, .y=2}};
        break;
      case 2:
      case 1: // handle the two middle squares
        neighbours = {{.x=0, .y=origin.y+1},
                                             {.x=1, .y=origin.y},
                      {.x=1, .y=origin.y-1}};
        break;
      case 0: // handle bottom left square
        neighbours = {{.x=0, .y=1},
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
                                             {.x=origin.x, .y=2}};
        break;
      break;
      case 2:
      case 1: // handle the four middle squares
        neighbours = {                                {.x=origin.x, .y=origin.y+1},
                      {.x=origin.x-1, .y=origin.y  },                               {.x=origin.x+1, .y=origin.y  },
                                                      {.x=origin.x, .y=origin.y-1}};
        break;
      case 0: // handle the two bottom middle squares
        neighbours = {                       {.x=origin.x, .y=1},
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
                                    {.x=3, .y=2}};
        break;
      case 2:
      case 1: // handle the two middle squares
        neighbours = {                       {.x=3, .y=origin.y+1},
                      {.x=2, .y=origin.y},
                                             {.x=3, .y=origin.y-1}};
        break;
      case 0: // handle bottom left square
        neighbours = {              {.x=3, .y=1},
                      {.x=2, .y=0}};
        break;
      }
      break;
    }
  }

  return neighbours;
}

std::vector<square> coordsVec2squaresVec(std::vector<Coord> CoordsVec, Board* board)
{
  std::vector<square> squaresVec;
  squaresVec.reserve(CoordsVec.size());

  for(int i = 0; i < CoordsVec.size(); ++i)
    {
      if(board->squareVal[CoordsVec.at(i).x][CoordsVec.at(i).y] != 0)
        {
          square newSquare = {board->squareVal[CoordsVec.at(i).x][CoordsVec.at(i).y], CoordsVec.at(i)};
          squaresVec.push_back(newSquare);
        }
    }
  return squaresVec;
}

int findHighestValueIn(std::vector<square>* searchSpace, int maxVal=262144) // default value is impossible to reach
{
  int highestValue = 0;
  int highestIndex = -1;
  for(int i = 0; i < searchSpace->size(); ++i)
    {
      if(searchSpace->at(i).value > highestValue && //how to handle equal squares?
         searchSpace->at(i).value <= maxVal)
        {
          highestValue = searchSpace->at(i).value;
          highestIndex = i;
        }
    }

  return highestIndex;
}

void swipe(direction move, Board* board)
{
  switch(move)
  {
  case Up:
    board->up();
    break;
  case Down:
    board->down();
    break;
  case Left:
    board->left();
    break;
  case Right:
    board->right();
    break;
  }
}

void mergeAdjacentSquaresWithEqualValues(Coord from, Coord to, Board* board)
{
  if(from.y == to.y)
    {
      //move horizontally
      if(from.x < to.x)
        board->right();
      else
        board->left();
      return;
    }
  else
    {
      // move vertically
      if(from.y < to.y)
        board->up();
      else
        board->down();
      return;
    }
}

void findSequenceTail(std::vector<square>* squares, Board* board)
{
  std::vector<square> squaresToSearch = coordsVec2squaresVec(addNeighbourSquares(squares->back().pos), board);

  if(squaresToSearch.size() == 0)
    return; // all alone

  int idx = findHighestValueIn(&squaresToSearch, squares->back().value);
  if(idx < 0)
    return;

  square next = squaresToSearch.at(idx);

  if(next.value == squares->back().value) // equal values should be merged
    {
      squares->push_back(next);
      return;
    }

  squares->push_back(next);
  findSequenceTail(squares, board);
}

bool placeInCorner(Coord pos, Board* board)
{
  // Place at right edge if possible
  bool moveRight = false;
  for(int x = pos.x+1; x < 3; ++x)
    {
      moveRight = true;
      if(board->squareVal[x][pos.y])
        {
          moveRight = false;
          break; // a square is in the way
        }
    }

  if(moveRight)
    {
      board->right();
      return true;
    }

  // Place at left edge if possible
  bool moveLeft = false;
  for(int x = pos.x-1; x >= 0; --x)
    {
      moveRight = true;
      if(board->squareVal[x][pos.y])
        {
          moveLeft = false;
          break; // a square is in the way
        }
    }

  if(moveLeft)
    {
      board->left();
      return true;
    }

  // Place at top edge if possible
  bool moveUp = false;
  for(int y = pos.y+1; y < 3; ++y)
    {
      moveUp = true;
      if(board->squareVal[pos.x][y])
        {
          moveUp = false;
          break; // a square is in the way
        }
    }

  if(moveUp)
    {
      board->up();
      return true;
    }

  // Place at top edge if possible
  bool moveDown = false;
  for(int y = pos.y-1; y <= 0; --y)
    {
      moveDown = true;
      if(board->squareVal[pos.x][y])
        {
          moveDown = false;
          break; // a square is in the way
        }
    }

  if(moveDown)
    {
      board->down();
      return true;
    }

  return false;
}

compass disqualifyDirections(Coord pos, Board* board)
{
  compass swipe;
  if(pos.isInBottomLeftCorner())
    {
      swipe.horizontal = Left;
      swipe.vertical   = Down;
    }

  if(pos.isInBottomRightCorner())
    {
      swipe.horizontal = Right;
      swipe.vertical   = Down;
    }

  if(pos.isInTopLeftCorner())
    {
      swipe.horizontal = Left;
      swipe.vertical   = Up;
    }

  if(pos.isInTopRightCorner())
    {
      swipe.horizontal = Right;
      swipe.vertical   = Up;
    }

  return swipe;
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
  std::vector<square> squares;
  squares.reserve(16);

  addAllSquares(squares, board);

  std::sort(squares.begin(), squares.end());
  squares.erase(std::remove_if(squares.begin(), squares.end(),
                               [](square sqr) { return sqr.value == 0; }));

  square highValueSquare = squares.at(findHighestValueIn(&squares));

  if(highValueSquare.pos.isInCorner() == false)
    {
      if(placeInCorner(highValueSquare.pos, board) == false)
        return; // not possible to place highest value square in corner
    }

  compass noGo = disqualifyDirections(highValueSquare.pos, board);

  squares.clear();
  squares.push_back(highValueSquare);

  findSequenceTail(&squares, board);

  square last = squares.back();
  squares.pop_back();

  // Merge equal squares
  if(squares.back().value == last.value)
    {
      mergeAdjacentSquaresWithEqualValues(last.pos, squares.back().pos, board);
      return;
    }
}
