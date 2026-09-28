# perform basic vector operations on x and y
# addition, substrcation, scalar multiplication, scalar division, euqality, dot product, magnitude

class vector:
    def __add__(self, v1, v2):
        self.v1=v1
        self.v2=v2
        return vector (self.v1 + self.v2)