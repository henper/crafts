#include <GL/glut.h>

typedef struct 
{
	GLfloat r,g,b;
} quadColor;

typedef struct 
{
	GLfloat x,y;
	GLfloat quadColor[3];
} quadRgb;