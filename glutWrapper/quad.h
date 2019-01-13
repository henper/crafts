/*
 * quad.h
 *
 *  Created on: Jan 11, 2019
 *      Author: eponhik
 */

#ifndef QUAD_H_
#define QUAD_H_

#include "glutWrapper.h"

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
  void setEmpty();

  quadVerticeColor vertexColor;
};

class QuadVertex {

public:
  coord2dS bottomLeft;
  coord2dS topLeft;
  coord2dS topRight;
  coord2dS bottomRight;
};

#endif /* QUAD_H_ */
