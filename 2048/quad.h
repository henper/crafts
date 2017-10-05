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
  rgbColor topLeft;
  rgbColor topRight;
  rgbColor bottomLeft;
  rgbColor bottomRight;
} quadVertice;

class Quad {

public:
  Quad();
  Quad(int val);

  quadVertice vertex;
  //int value;
};

#endif /* SQUARE_H_ */
