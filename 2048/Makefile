
CXXFLAGS = -g -c -std=gnu++11

SRC_FILES = $(wildcard *.cpp)
OBJ_FILES = $(SRC_FILES:.cpp=.o)

all : main

.PHONY : clean

clean :
	rm -f *.o *.h.gch

main : $(OBJ_FILES)
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut
