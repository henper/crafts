/*
 * quad.cc
 *
 *  Created on: Jan 11, 2019
 *      Author: eponhik
 */

#include "quad.h"

QuadColor::QuadColor()
{
  setEmpty();
}

void QuadColor::setEmpty()
{
  quadVertice emptyBackground =
  {
    .bottomLeft  = {.r=0.5, .g=0.5, .b=0.5},
    .topLeft     = {.r=0.5, .g=0.5, .b=0.5},
    .topRight    = {.r=0.5, .g=0.5, .b=0.5},
    .bottomRight = {.r=0.5, .g=0.5, .b=0.5}
  };
  this->vertexColor = emptyBackground;
}
