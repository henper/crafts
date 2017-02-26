% Generate test matrices for inlines transpose Gtest

smallSquare = randi(100, 50);
prettyPrint(smallSquare , 'smallSquare');
prettyPrint(smallSquare', 'smallSquareTrans');

smallRectangle = randi(100, [4, 3]);
prettyPrint(smallRectangle , 'smallRectangle');
prettyPrint(smallRectangle', 'smallRectangleTrans');
