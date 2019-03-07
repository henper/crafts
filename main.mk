# Begin: generic Makefile material

INC += $(addprefix -I, $(INC_DIR))

# For all source file paths, create a path to corresponding obj-file
# different than that of the source file itself. Steps:
# 1. Change .cpp to .o
# 2. Strip the directory from the source file
# 3. Add the path to the object directory
OBJ_DIR   = obj
SRC_FILES_NOPATH = $(notdir $(SRC_FILES))
OBJ_FILES_NOPATH = $(SRC_FILES_NOPATH:.cc=.o)
OBJ_FILES = $(addprefix $(OBJ_DIR)/, $(OBJ_FILES_NOPATH))

# Create a list of directories where Make should search for source files
VPATH = $(sort $(dir $(SRC_FILES)))

# This bit of magic (MMD) will tell the preprocessor to generate
# a list of an obejcts dependencies, i.e. the .c-file itself and
# all .h-files included, recursively.
CXXFLAGS += -MMD
# Create a list of all the dependecy files that will be generated
DEP_FILES = $(OBJ_FILES:%.o=%.d)
# By including that list we get specialised targets for all
# objects on subsequent builds. On first build there won't be any
# .d-files so we ask make to ignore non-existing files with '-'
-include $(DEP_FILES)

CXXFLAGS = -g -c -std=gnu++11

all : $(OBJ_DIR) $(TARGET)

# Silence output unless user invokes with > make VERBOSE=true
$(VERBOSE).SILENT :

.PHONY : clean

clean :
	rm -f $(OBJ_FILES) main

$(TARGET) : $(OBJ_FILES)
	g++ $^ -o $@ -lpthread -lGL -lGLU -lglut

$(OBJ_DIR) :
	mkdir -p $(OBJ_DIR)

$(OBJ_FILES) : $(OBJ_DIR)/%.o : %.cc
	mkdir -p $(@D)
	g++ $(CXXFLAGS) $(INC) $< -o $@
