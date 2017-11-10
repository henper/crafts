/*
 * Square.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef SQUARE_H_
#define SQUARE_H_

typedef struct rgbColor
{
  float r,g,b;
} rgbColor;

typedef struct quadVertice
{
  // Note order is defined by OpenGL
  rgbColor bottomLeft;
  rgbColor topLeft;
  rgbColor topRight;
  rgbColor bottomRight;
} quadVertice;

class QuadColor {

public:
  QuadColor();
  QuadColor(int val);

  quadVertice vertex;
  //int value;
};

#endif /* SQUARE_H_ */
