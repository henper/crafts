/*
 * Square.h
 *
 *  Created on: Oct 2, 2017
 *      Author: henper
 */

#ifndef SQUARE_H_
#define SQUARE_H_

#include <quad.h>

class Square : public QuadColor
{
public:
  Square() {QuadColor();};
  Square(int val);
};

#endif /* SQUARE_H_ */
