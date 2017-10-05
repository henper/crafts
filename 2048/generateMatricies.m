
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

% Generate colors for 2048 squares
numColors = 17; % We need a unique color for all unique square values:
                % 2, 4 ... 65536, 131072
                % 2¹, 2² ... 2¹⁶, 2¹⁷
                
% I like the last half of the bone (kind of blue) color scheme
scheme = flipud(bone(numColors*2*4)); % times 4 to get a nice gradient for each quad
colors = scheme(numColors+1:end,:);   % r-g-b values
prettyPrint(single(colors), 'colors');
