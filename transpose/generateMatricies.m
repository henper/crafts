% Generate test matrices for inlines transpose Gtest

smallSquare = randi(100, 50);
prettyPrint(smallSquare , 'smallSquare');
prettyPrint(smallSquare', 'smallSquareTrans');

smallRectangle = randi(100, [25, 100]);
%smallRectangle = [  1,  2 ; ...
%                    3,  4 ; ...
%                    5,  6 ];
prettyPrint(smallRectangle , 'smallRectangle');
prettyPrint(smallRectangle', 'smallRectangleTrans');
