class Rule:
    def __init__(self, rows=5):
        self.rows = rows 
        self.rules = {}
        self.child()

    def add_child(self, child_node):
        self.rules.setdefault(child_node[0], []).append(child_node[-1])
        self.rules.setdefault(child_node[-1], []).append(child_node[0])

    def find_child(self, node, row, inc1, inc2):
        child = node + row + inc1
        grand = node + row + inc2
        self.add_child([node, child, grand+row])

    def find_horizontal(self, lst, chunk_size):
        sublists = [lst[i:i + chunk_size] for i in range(0, len(lst), 1) if len(lst[i:i + chunk_size]) == chunk_size]
        for x in sublists:
            self.add_child(x)

    def __repr__(self):
        return str(self.rules)

    def child(self):
        for i in range(self.rows):
            starPosition = (i * (i + 1)) // 2
            endPosition = starPosition + i
            array_range = range(starPosition, endPosition + 1)
            if i < self.rows - 2:
                for j in array_range:                
                    self.find_child(j, i, 1, 3) # find left child 
                    self.find_child(j, i, 2, 5) # find right child
            self.find_horizontal([*array_range], 3) # find horizontal child


