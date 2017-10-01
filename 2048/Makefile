
all : main

.PHONY : clean

clean :
	rm -f main.o *.h.gch

main.o : main.cpp colors.h vertices.h
	g++ -g -c $^

main : main.o
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut
