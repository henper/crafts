/*
 * Quad.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "square.h"
#include "quad.h"
#include "colors.h"

Square::Square(int val)
{
  if(val > 0)
    {
      quadVertice* quadColors = reinterpret_cast<quadVertice*>(colors[__builtin_ctz(val)*4]);  // count trailing zeroes, i.e. log2()
      vertexColor = *quadColors;
    }
  else
    setEmpty();
}

