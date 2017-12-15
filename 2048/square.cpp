/*
 * Quad.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "square.h"

#include "colors.h"

static const quadVertice emptyBackground =
{
  .bottomLeft  = {.r=0.5, .g=0.5, .b=0.5},
  .topLeft     = {.r=0.5, .g=0.5, .b=0.5},
  .topRight    = {.r=0.5, .g=0.5, .b=0.5},
  .bottomRight = {.r=0.5, .g=0.5, .b=0.5}
};

QuadColor::QuadColor()
{
  //value  = 0;
  vertexColor = emptyBackground;
}

QuadColor::QuadColor(int val)
{
  if(val > 0)
    {
      quadVertice* quadColors = reinterpret_cast<quadVertice*>(colors[__builtin_ctz(val)*4]);  // count trailing zeroes, i.e. log2()
      vertexColor = *quadColors;
    }
  else
    vertexColor = emptyBackground;
}

