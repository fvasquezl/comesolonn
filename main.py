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

    def __repr__(self):
        return str(self.rule)

    def child(self):
        for i in range(5-2):
            starPosition = (i * (i + 1)) // 2
            endPosition = starPosition + i
            for j in range(starPosition, endPosition + 1):                
                self.find_child(j, i, 1, 3) # find left child 
                self.find_child(j, i, 2, 5) # find right child

if __name__ == "__main__":
    rule = Rule()
    print(rule)
