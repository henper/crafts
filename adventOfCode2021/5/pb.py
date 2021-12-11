# Line Intersect Line
import pygame
 
class Line:
    def __init__(self, x1, y1, x2, y2, color, width=1):
        self.a = pygame.Vector2(x1, y1)
        self.b = pygame.Vector2(x2, y2)
        self.color = color
        self.width = width
 
    def draw(self, surface):
        x1, y1, x2, y2 = self.get_points()
 
        pygame.draw.aaline(surface, self.color, (x1, y1), (x2, y2), self.width)
 
    def get_points(self):
        x1, y1 = self.a
        x2, y2 = self.b
        return x1, y1, x2, y2
 
    # @return None or Vector2 of intersect
    def intersect_line(self, line):
        if not isinstance(line, Line):
            return
 
        x1, y1, x2, y2 = line.get_points()
        x3, y3, x4, y4 = self.get_points()
 
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return
 
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / den
        if 0 < t < 1 and 0 < u < 1:
            return pygame.Vector2(x1 + t * (x2 - x1),
                           y1 + t * (y2 - y1))
 
class Main:
    def __init__(self, caption, width, height, flags=0):
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.delta = 0
        self.fps = 60
 
        self.line_color = pygame.Color("snow")
        self.lines = (Line(150, 200, 350, 200, self.line_color),
                      Line(200, 100, 250, 300, self.line_color))
 
        self.point = self.lines[0].intersect_line(self.lines[1])
 
    def draw(self):
        for line in self.lines:
            line.draw(self.surface)
 
        if self.point:
            pygame.draw.circle(self.surface, self.line_color, self.point, 5)
 
 
    def mainloop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
 
            self.surface.fill(pygame.Color("black"))
            self.draw()
            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)
 
def main():
    pygame.init()
    app = Main("Line Intersection Line", 400, 400)
    app.mainloop()
    pygame.quit()
 
main()