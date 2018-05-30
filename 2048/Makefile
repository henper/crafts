
CXXFLAGS = -MMD -g -c -std=gnu++11

SRC_FILES = $(wildcard *.cpp)
OBJ_FILES = $(SRC_FILES:.cpp=.o)

-include $(OBJ_FILES:.o=.d)

all : main

.PHONY : clean

clean :
	rm -f *.o *.d main

main : $(OBJ_FILES)
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut
