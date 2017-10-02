
all : main

.PHONY : clean

clean :
	rm -f *.o *.h.gch

square.o : square.cpp square.h
	g++ -g -c $^

board.o : board.cpp board.h
	g++ -g -c $^

main.o : main.cpp colors.h vertices.h
	g++ -g -c $^

main : main.o board.o square.o
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut
