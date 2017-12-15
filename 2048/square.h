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

typedef struct quadVerticeColor
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

  quadVerticeColor vertexColor;
  //int value;
};

typedef struct coord2d
{
  float x, y;
} coord2d;

class QuadVertex {

public:
  coord2d bottomLeft;
  coord2d topLeft;
  coord2d topRight;
  coord2d bottomRight;
};

#endif /* SQUARE_H_ */
