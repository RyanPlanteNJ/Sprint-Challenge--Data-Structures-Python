class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # elif value >= self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            found = self.left.contains(target)
        if target >= self.value:
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found
