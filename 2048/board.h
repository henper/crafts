/*
 * board.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef BOARD_H_
#define BOARD_H_

#include "quad.h"
#include "coord.h"

class Board
{
private:
  void moveSquare(Coord origin, Coord dest);
  bool mergeIfEqual(Coord origin, Coord dest);

public:
  Board();
  void setSquare(Coord pos, int val) { quad[pos.x][pos.y] = Quad(val); squareVal[pos.x][pos.y] = val; }
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
