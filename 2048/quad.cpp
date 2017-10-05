/*
 * Quad.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "quad.h"
#include "colors.h"

static const quadVertice emptyBackground =
    {
	.topLeft     = {.r=0.5, .g=0.5, .b=0.5},
	.topRight    = {.r=0.5, .g=0.5, .b=0.5},
	.bottomLeft  = {.r=0.5, .g=0.5, .b=0.5},
	.bottomRight = {.r=0.5, .g=0.5, .b=0.5}
    };

Quad::Quad()
{
  //value  = 0;
  vertex = emptyBackground;
}

Quad::Quad(int val)
{
  if(val > 0)
    {
      /*rgbColor* col1 = reinterpret_cast<rgbColor*>(colors[__builtin_ctz(val)*4]);
      quadVertice quadColors = {*col1, *col1, *col1, *col1};*/

      quadVertice* quadColors = reinterpret_cast<quadVertice*>(colors[__builtin_ctz(val)*4]);
      vertex = *quadColors;
    }
  else
    vertex = emptyBackground;
}

