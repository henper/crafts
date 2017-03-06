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

% Generate matrices of vertexes and colours for transpose visrep
width = height = 4;
y = x = linspace(-1, 1, width+1); % square matrix

vertices = zeros(width*height,4*2); % each vertex consists of a quad of xy-values

r = g = b = linspace(0, 1, width*height);
colours   = jet(width*height*4);   % r-g-b values for each quad

for i = 1:width
  for j = 1:height
    index = j + (i-1)*height;
    vertices(index,:) = [x(i), y(j), x(i), y(j+1), x(i+1), y(j+1), x(i+1), y(j)];
  end
end

prettyPrint(single(vertices), 'vertices');
prettyPrint(single(colours), 'colors');
