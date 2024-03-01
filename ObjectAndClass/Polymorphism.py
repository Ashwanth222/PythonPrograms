class Polygon:
    def render(self):
        print("Rendering Polygon...")

class Rectange(Polygon):

    def render(self):
        print("rendering rectangle")

class Circle(Polygon):

    def render(self):
        print("rendering circle")

c = Circle()
c.render()

r = Rectange()
r.render()