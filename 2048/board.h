/*
 * board.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef BOARD_H_
#define BOARD_H_

#include "square.h"

class Board
{
public:
  Board();
  void setSquare(int x, int y, int val) { square[x][y] = Square(val); }

  // controls
  void up();
  void down();
  void right();
  void left();

  Square square[4][4];
};


#endif /* BOARD_H_ */
