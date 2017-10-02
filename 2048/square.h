/*
 * Square.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef SQUARE_H_
#define SQUARE_H_

#include <GL/glut.h>

typedef struct rgbColor
{
  GLfloat r,g,b;
} rgbColor;

typedef struct quadVertice
{
  // Note order is defined by OpenGL
  rgbColor topLeft;
  rgbColor topRight;
  rgbColor bottomRight;
  rgbColor bottomLeft;
} quadVertice;

class Square {

  static const quadVertice activeBackground;
  static const quadVertice emptyBackground;

public:
  Square();
  Square(int val);
  ~Square();

  quadVertice vertex;
  //int value;
};

#endif /* SQUARE_H_ */
