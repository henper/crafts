
SRC_FILES = $(wildcard *.cc)
OBJ_FILES = $(SRC_FILES:.cc=.o)

LIBS = -lgtest_main -lgtest -lpthread -lprimesieve

CXXFLAGS = -MMD -g -c -std=gnu++11

all : gbt

-include $(OBJ_FILES:.o=.d)

.PHONY : clean

clean :
	rm -f *.o *.d gbt

gbt : $(OBJ_FILES)
	g++ $^ -o $@ $(LIBDIRS) $(LIBS)
