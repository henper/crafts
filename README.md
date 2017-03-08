# crafts
My solutions, or attempts thereof, to our companys:
"Software Craftsmanship Community of Practices" challenges.

How-Tos and dependencies for anyone who whish to run these snippets
(or the more likely scenario that I've simply forgotten)

goldbach.py
------------------------------------------------------------------------
Depends on Symbolic Python: http://www.sympy.org/en/index.html


transpose
------------------------------------------------------------------------
Depends on: GoogleTest: https://github.com/google/googletest and
OpenGL and GLUT: http://kiwwito.com/installing-opengl-glut-libraries-in-ubuntu/

How-To:
Generate test vectors with Matlab or Octave by running the script
generateTestVectors.m

Compile with 'make' (remember to update paths to googletest in Makefile)
Run ./transpose to execute tests.
