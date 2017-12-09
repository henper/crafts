/*
 * board.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef BOARD_H_
#define BOARD_H_

#include "coord.h"
#include "square.h"

class Board
{
private:
  void moveSquare(Coord origin, Coord dest);
  bool mergeIfEqual(Coord origin, Coord dest);

public:
  Board();
  void setSquare(Coord pos, int val) { quad[pos.x][pos.y] = QuadColor(val); squareVal[pos.x][pos.y] = val; }
  void genSquare();

  // controls
  void up();
  void down();
  void right();
  void left();

  // holds the colors for all vertices
  QuadColor quad[4][4];

  // holds the coordinates for all vertices
  QuadVertex vertex[4][4];

  // holds the numerical value in each square
  int squareVal[4][4];
};


#endif /* BOARD_H_ */
