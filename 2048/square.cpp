/*
 * Square.cpp
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#include "square.h"

Square::Square()
{
  vertex = emptyBackground;
}

Square::Square(int val)
{
  //value  = val;
  vertex = activeBackground;
}

Square::~Square() {

}

const quadVertice Square::activeBackground =
    {
	.topLeft     = {.r=1.0, .g=0.8, .b=0.3},
	.topRight    = {.r=1.0, .g=0.8, .b=0.3},
	.bottomRight = {.r=1.0, .g=0.8, .b=0.3},
	.bottomLeft  = {.r=1.0, .g=0.8, .b=0.3}
    };

const quadVertice Square::emptyBackground =
    {
	.topLeft     = {.r=0, .g=0, .b=0},
	.topRight    = {.r=0, .g=0, .b=0},
	.bottomRight = {.r=0, .g=0, .b=0},
	.bottomLeft  = {.r=0, .g=0, .b=0}
    };
