/*
 * quad.h
 *
 *  Created on: Jan 11, 2019
 *      Author: eponhik
 */

#ifndef QUAD_H_
#define QUAD_H_

typedef struct coord2dS
{
  float x,y;

  void scale(int factor) { x *= factor; y *= factor; };
} coord2dS;

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
} quadVerticeColor;

class QuadColor {

public:
  QuadColor();
  void setEmpty();

  quadVerticeColor vertexColor;
};

class QuadVertex {

public:
  QuadVertex();
  QuadVertex(int xIdx, int yIdx, int xMax, int yMax); // set the coord2ds for an indexed square

  coord2dS bottomLeft;
  coord2dS topLeft;
  coord2dS topRight;
  coord2dS bottomRight;
};

QuadVertex* generateGrid(int xsquares, int ysquares);

#endif /* QUAD_H_ */
