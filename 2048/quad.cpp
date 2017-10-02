/*
 * Quad.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "quad.h"

static const quadVertice activeBackground =
    {
	.topLeft     = {.r=1.0, .g=0.8, .b=0.3},
	.topRight    = {.r=1.0, .g=0.8, .b=0.3},
	.bottomRight = {.r=1.0, .g=0.8, .b=0.3},
	.bottomLeft  = {.r=1.0, .g=0.8, .b=0.3}
    };

static const quadVertice emptyBackground =
    {
	.topLeft     = {.r=0, .g=0, .b=0},
	.topRight    = {.r=0, .g=0, .b=0},
	.bottomRight = {.r=0, .g=0, .b=0},
	.bottomLeft  = {.r=0, .g=0, .b=0}
    };

Quad::Quad()
{
  //value  = 0;
  vertex = emptyBackground;
}

Quad::Quad(int val)
{
  if(val > 0)
    vertex = activeBackground;
  else
    vertex = emptyBackground;
}

