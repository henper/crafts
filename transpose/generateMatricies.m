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

% Generate matrices of vertices and colours for transpose visrep
width = height = 16;
y = x = linspace(-1, 1, width+1); % square matrix

vertices = zeros(width*height,4*2); % each vertex consists of a quad of xy-values

for i = 1:width
  for j = 1:height
    index = j + (i-1)*height;
    vertices(index,:) = [x(i), y(j), x(i), y(j+1), x(i+1), y(j+1), x(i+1), y(j)];
  end
end

%rotate the vertices matrix to put the origin at the top left (instead of bottom left)
vertices = reshape(vertices, width, height, 4*2);
vertices = rot90(vertices, -1); % -90 degrees
vertices = reshape(vertices, width*height, 4*2);

prettyPrint(single(vertices), 'vertices');

colours   = jet(width*height*4);   % r-g-b values for each quad
prettyPrint(single(colours), 'colors');
