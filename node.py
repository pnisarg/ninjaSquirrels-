class Node:
    def __init__(self, state = [], parent = None, depth = 0, value = 0, name = "root"):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.value = value
        self.name = name

    def __repr__(self):
        return "<Node %s, state = %s, parent: %s" % (self.name, self.state, self.parent.name if self.parent!=None else "") 
