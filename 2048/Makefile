
CC_FLAGS = -g -c -std=gnu++14

all : main

.PHONY : clean

clean :
	rm -f *.o *.h.gch

quad.o : quad.cpp
	g++ $(CC_FLAGS) $^

board.o : board.cpp
	g++ $(CC_FLAGS) $^

main.o : main.cpp vertices.h
	g++ $(CC_FLAGS) $^

main : main.o board.o quad.o
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut
