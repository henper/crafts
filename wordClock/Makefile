
SRC_FILES = $(wildcard *.cpp)

# Begin: generic Makefile material

# For all source file paths, create a path to corresponding obj-file
# different than that of the source file itself. Steps:
# 1. Change .cpp to .o
# 2. Strip the directory from the source file
# 3. Add the path to the object directory
OBJ_DIR = obj
OBJ_FILES = $(addprefix $(OBJ_DIR)/, $(SRC_FILES:.cpp=.o))

CXXFLAGS = -MMD -g -c -std=gnu++11

all : $(OBJ_DIR) main

.PHONY : clean

clean :
	rm -f $(OBJ_FILES) main

main : $(OBJ_FILES)
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut

$(OBJ_DIR) :
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o: %.cpp
	g++ $(CXXFLAGS) $< -o $@
