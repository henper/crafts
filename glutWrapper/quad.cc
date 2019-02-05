/*
 * quad.cc
 *
 *  Created on: Jan 11, 2019
 *      Author: eponhik
 */

#include "quad.h"
#include <cstdlib>

QuadColor::QuadColor()
{
  setEmpty();
}

void QuadColor::setEmpty()
{
  quadVerticeColor emptyBackground =
  {
    .bottomLeft  = {.r=0.5, .g=0.5, .b=0.5},
    .topLeft     = {.r=0.5, .g=0.5, .b=0.5},
    .topRight    = {.r=0.5, .g=0.5, .b=0.5},
    .bottomRight = {.r=0.5, .g=0.5, .b=0.5}
  };
  this->vertexColor = emptyBackground;
}

QuadVertex::QuadVertex() {}
QuadVertex::QuadVertex(int xIdx, int yIdx, int xMax, int yMax)
{
  // Step1. Get the incremantals for each dimension, knowing that both X and Y ranges from -1 to +1
  float xDelta = 2 / (float)xMax;
  float yDelta = 2 / (float)yMax;

  // Step2. given the incrementals calculate the bottom left coordinate of this indexed square 
  this->bottomLeft.x = xIdx*xDelta - 1;
  this->bottomLeft.y = yIdx*yDelta - 1;

  // Step3. derive the remaining coordinates given the bottomLeft and the incrementals
  this->topLeft.x = this->bottomLeft.x;
  this->topLeft.y = this->bottomLeft.y + yDelta;
  this->topRight.x = this->bottomLeft.x + xDelta;
  this->topRight.y = this->bottomLeft.y + yDelta;
  this->bottomRight.x = this->bottomLeft.x + xDelta;
  this->bottomRight.y = this->bottomLeft.y;
}

QuadVertex* generateGrid(int xsquares, int ysquares)
{
  QuadVertex* vertices = (QuadVertex*)malloc(sizeof(QuadVertex) * xsquares * ysquares);

  for(int yIdx = 0; yIdx < ysquares; yIdx++)
  {
    for(int xIdx = 0; xIdx < xsquares; xIdx++)
    {
      vertices[yIdx*xsquares + xIdx] = QuadVertex(xIdx, yIdx, xsquares, ysquares);
    }
  }

  return vertices;
}
