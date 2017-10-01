
% Generate matrices of vertices 2048 game board
width  = 4;
height = width;
x = linspace(-1, 1, width+1);
y = linspace(-1, 1, height+1);

vertices = zeros(width*height,4*2); % each vertex consists of a quad of xy-values

for i = 1:width
  for j = 1:height
    index = j + (i-1)*width;
    vertices(index,:) = [x(i), y(j), x(i), y(j+1), x(i+1), y(j+1), x(i+1), y(j)];
  end
end

prettyPrint(single(vertices), 'vertices');

colours   = jet(width*height*4);   % r-g-b values for each quad
prettyPrint(single(colours), 'colors');
