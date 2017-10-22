/*
 * ai.h
 *
 *  Created on: Oct 6, 2017
 *      Author: henper
 */

#ifndef AI_H_
#define AI_H_

#include "board.h"

void ai_main(Board* board);

enum direction {Up, Down, Left, Right};


typedef struct compass
{
  direction horizontal;
  direction vertical;
} compass;

#endif /* AI_H_ */
