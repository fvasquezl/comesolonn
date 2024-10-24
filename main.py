class Rule:
    def __init__(self):
        self.rule = []
        self.child()

    def add_child(self, child_node):
        self.rule.append(child_node)

    def find_child(self, node, row, inc1, inc2):
        child = node + row + inc1
        grand = node + row + inc2
        self.add_child([node, child, grand+row])

    def find_horizontal(self, lst, chunk_size):
        sublists = [lst[i:i + chunk_size] for i in range(0, len(lst), 1) if len(lst[i:i + chunk_size]) == chunk_size]
        for x in sublists:
            self.add_child(x)

    def __repr__(self):
        return str(self.rule)

    def child(self):
        for i in range(5):
            starPosition = (i * (i + 1)) // 2
            endPosition = starPosition + i
            array_range = range(starPosition, endPosition + 1)
            if i < 3:
                for j in array_range:                
                    self.find_child(j, i, 1, 3) # find left child 
                    self.find_child(j, i, 2, 5) # find right child
            self.find_horizontal([*array_range], 3) # find horizontal child

if __name__ == "__main__":
    rule = Rule()
    print(rule)
