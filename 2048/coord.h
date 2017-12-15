#ifndef COORD_H_
#define COORD_H_

class Coord
{
public:
  int x, y;

  bool isInBottomLeftCorner()  { return (x == 0 && y == 0); }
  bool isInBottomRightCorner() { return (x == 0 && y == 4); }
  bool isInTopLeftCorner()     { return (x == 4 && y == 0); }
  bool isInTopRightCorner()    { return (x == 4 && y == 4); }

  bool isInCorner() { return (isInBottomLeftCorner()  ||
                              isInBottomRightCorner() ||
                              isInTopLeftCorner()     ||
                              isInTopRightCorner()); }
};

#endif