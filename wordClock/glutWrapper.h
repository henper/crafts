/*
 * glutWrapper.h
 *
 *  Created on: Dec 26, 2018
 *      Author: eponhik
 */

#ifndef GLUTWRAPPER_H_
#define GLUTWRAPPER_H_

typedef struct coord2dS
{
  int x,y;

  void scale(int factor) { x *= factor; y *= factor; };
} coord2dS;

typedef struct windowParamsS
{
  const char* title;
  coord2dS position;
  coord2dS size;
} WindowParamsS;

typedef struct callbacksS
{
  void (* window)( void );
  void (* alphaKey)( unsigned char, int, int );
  void (* specialKey)( int, int, int );
  void (* idle)( void );
  void (* timer)( int );
  int period; // in millis

} callbacksS;

void glwInit(int* argc, char** argv, windowParamsS winp, callbacksS cb);

void glwMainLoop(void);

#endif /* GLUTWRAPPER_H_ */
