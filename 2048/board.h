/*
 * board.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef BOARD_H_
#define BOARD_H_

#include "quad.h"

class Board
{
public:
  Board();
  void setSquare(int x, int y, int val) { quad[x][y] = Quad(val); squareVal[x][y] = val; }

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
