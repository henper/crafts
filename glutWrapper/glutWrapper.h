/*
 * glutWrapper.h
 *
 *  Created on: Dec 26, 2018
 *      Author: eponhik
 */

#ifndef GLUTWRAPPER_H_
#define GLUTWRAPPER_H_

#include "quad.h"

/* Types *********************************************************************/

typedef struct windowParamsS
{
  const char* title;
  coord2dS position;
  coord2dS size;
  QuadVertex* vertices;
  QuadColor*  colors;
  int length;
} WindowParamsS;

typedef struct callbacksS
{
  void (* draw)( void );
  void (* alphaKey)( unsigned char, int, int );
  void (* specialKey)( int, int, int );
  void (* idle)( void );
  void (* timer)( int );
  int period; // in millis

} callbacksS;

/* Functions *****************************************************************/

// call this 'first' in your main
void glwInit(int* argc, char** argv, windowParamsS winp, callbacksS cb);

// call this last in your main
void glwMainLoop(void);

#endif /* GLUTWRAPPER_H_ */
