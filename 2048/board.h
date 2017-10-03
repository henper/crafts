/*
 * board.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef BOARD_H_
#define BOARD_H_

#include "quad.h"

// Square coordinate in grid: 4x4
typedef struct coord
{
  int x, y;
} coord;

class Board
{
private:
  void moveSquare(coord origin, coord dest);
  void mergeIfEqual(coord origin, coord dest);

public:
  Board();
  void setSquare(coord pos, int val) { quad[pos.x][pos.y] = Quad(val); squareVal[pos.x][pos.y] = val; }
  void genSquare();

  // controls
  void up();
  void down();
  void right();
  void left();

  // holds the colors for all vertices
  Quad quad[4][4];

  // holds the numerical value in each square
  int squareVal[4][4];
};


#endif /* BOARD_H_ */
