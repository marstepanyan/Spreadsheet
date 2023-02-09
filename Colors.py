class Color:

    def __init__(self, num):
        colors = {
            1: 'white',
            2: 'red',
            3: 'black',
            4: 'yellow',
            5: 'green',
            6: 'pink',
            7: 'blue'
        }
        self.color = colors[num]

    def __eq__(self, other):
        if self.color == other.color:
            return True

    def __repr__(self):
        return str(self.color)
