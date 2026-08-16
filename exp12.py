class BSTNode:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    # Insert a value
    def insert(self, val):

        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
        else:
            self.right = BSTNode(val)

    # Find minimum value
    def get_min(self):
        current = self

        while current.left is not None:
            current = current.left

        return current.val

    # Find maximum value
    def get_max(self):
        current = self

        while current.right is not None:
            current = current.right

        return current.val

    # Delete a value
    def delete(self, val):

        if self is None:
            return self

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)

            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)

            return self

        # Node has no right child
        if self.right is None:
            return self.left

        # Node has no left child
        if self.left is None:
            return self.right

        # Node has two children
        min_larger_node = self.right

        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val

        self.right = self.right.delete(min_larger_node.val)

        return self

    # Search for a value
    def exists(self, val):

        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False

            return self.left.exists(val)

        if self.right is None:
            return False

        return self.right.exists(val)

    # Preorder traversal
    def preorder(self, vals):

        if self.val is not None:
            vals.append(self.val)

        if self.left is not None:
            self.left.preorder(vals)

        if self.right is not None:
            self.right.preorder(vals)

        return vals

    # Inorder traversal
    def inorder(self, vals):

        if self.left is not None:
            self.left.inorder(vals)

        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.inorder(vals)

        return vals

    # Postorder traversal
    def postorder(self, vals):

        if self.left is not None:
            self.left.postorder(vals)

        if self.right is not None:
            self.right.postorder(vals)

        if self.val is not None:
            vals.append(self.val)

        return vals


# Creating BST
nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 17]

bst = BSTNode()

for num in nums:
    bst.insert(num)


# Preorder
print("preorder:")
print(bst.preorder([]))

print("#")

# Postorder
print("postorder:")
print(bst.postorder([]))

print("#")

# Inorder
print("inorder:")
print(bst.inorder([]))

print("#")


# Delete nodes
nums = [2, 6, 20]

print("deleting " + str(nums))

for num in nums:
    bst = bst.delete(num)

print("#")


# Search
print("4 exists:")
print(bst.exists(4))

print("2 exists:")
print(bst.exists(2))

print("12 exists:")
print(bst.exists(12))

print("18 exists:")
print(bst.exists(18))
