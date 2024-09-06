class AVLTreeNode:
    def __init__(self, key, size):
        self.key = key
        self.size = size
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right if x else None
        if x:
            x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        if x:
            x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right if x else None
        T2 = y.left if y else None
        if y:
            y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        if y:
            y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, node, key, size):
        if not node:
            return AVLTreeNode(key, size)
        if key < node.key:
            node.left = self.insert(node.left, key, size)
        else:
            node.right = self.insert(node.right, key, size)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        balance = self.get_balance(node)
        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.size = temp.size
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)
        
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_best_fit(self, node, size):
        if not node:
            return None, None
        if node.size >= size:
            best_fit_left, best_fit_left_node = self.find_best_fit(node.left, size)
            if best_fit_left is None or (node.size < best_fit_left_node.size):
                return node.key, node
            return best_fit_left, best_fit_left_node
        return self.find_best_fit(node.right, size)

    def insert_node(self, key, size):
        self.root = self.insert(self.root, key, size)

    def delete_node(self, key):
        self.root = self.delete(self.root, key)

    def find_best_fit_node(self, size):
        return self.find_best_fit(self.root, size)

#---------------------------------------------------------------------
class IntervalTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = high
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, root, low, high):
        if not root:
            return IntervalTreeNode(low, high)
        if low < root.low:
            root.left = self.insert(root.left, low, high)
        else:
            root.right = self.insert(root.right, low, high)
        
        if root.max < high:
            root.max = high
        
        return root

    def delete(self, root, low, high):
        if not root:
            return root
        if low < root.low:
            root.left = self.delete(root.left, low, high)
        elif low > root.low:
            root.right = self.delete(root.right, low, high)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_value_node(root.right)
            root.low = temp.low
            root.high = temp.high
            root.right = self.delete(root.right, temp.low, temp.high)
        
        root.max = self.get_max(root)
        return root

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_max(self, node):
        if not node:
            return float('-inf')
        max_val = node.high
        if node.left:
            max_val = max(max_val, node.left.max)
        if node.right:
            max_val = max(max_val, node.right.max)
        return max_val

    def overlap_search(self, root, low, high):
        if not root:
            return None
        if root.low <= high and low <= root.high:
            return root
        if root.left and root.left.max >= low:
            return self.overlap_search(root.left, low, high)
        return self.overlap_search(root.right, low, high)

    def insert_interval(self, low, high):
        self.root = self.insert(self.root, low, high)

    def delete_interval(self, low, high):
        self.root = self.delete(self.root, low, high)

    def find_overlap(self, low, high):
        return self.overlap_search(self.root, low, high)

#========================================================================
class Allocator:
    def __init__(self):
        self.chunk_size = 4096
        self.arena = []
        self.free_list = {
            (0, 128): AVLTree(),
            (128, 512): AVLTree(),
            (512, 1024): AVLTree(),
            (1024, 2048): AVLTree(),
            (2048, 4096): AVLTree(),
            (4096, float('inf')): AVLTree()
        }
        self.allocations = {}
        self.interval_tree = IntervalTree()

    def get_free_list_range(self, size):
        for key in self.free_list:
            if key[0] < size <= key[1]:
                return key
        return None

    def malloc(self, id, size):
        range_key = self.get_free_list_range(size)
        if not range_key:
            return None
        free_tree = self.free_list[range_key]
        best_fit_key, best_fit_node = free_tree.find_best_fit_node(size)
        if best_fit_node:
            free_tree.delete_node(best_fit_key)
            self.allocations[id] = (best_fit_key, size)
            if best_fit_node.size > size:
                remaining_size = best_fit_node.size - size
                remaining_key = best_fit_key + size
                remaining_range = self.get_free_list_range(remaining_size)
                if remaining_range:
                    self.free_list[remaining_range].insert_node(remaining_key, remaining_size)
        else:
            new_chunk_key = len(self.arena) * self.chunk_size
            self.arena.append(bytearray(self.chunk_size))
            remaining_size = self.chunk_size - size
            self.allocations[id] = (new_chunk_key, size)
            if remaining_size > 0:
                remaining_key = new_chunk_key + size
                remaining_range = self.get_free_list_range(remaining_size)
                if remaining_range:
                    self.free_list[remaining_range].insert_node(remaining_key, remaining_size)

    def free(self, id):
        if id in self.allocations:
            start, size = self.allocations.pop(id)
            end = start + size
            self.interval_tree.insert_interval(start, end)
            range_key = self.get_free_list_range(size)
            self.free_list[range_key].insert_node(start, size)
            overlap_node = self.interval_tree.find_overlap(start, end)
            if overlap_node:
                self.interval_tree.delete_interval(overlap_node.low, overlap_node.high)
                merged_start = min(start, overlap_node.low)
                merged_end = max(end, overlap_node.high)
                merged_size = merged_end - merged_start
                merged_range = self.get_free_list_range(merged_size)
                if merged_range:
                    self.free_list[merged_range].insert_node(merged_start, merged_size)

    def print_stats(self):
        total_allocated = len(self.arena) * self.chunk_size
        total_used = sum(size for _, size in self.allocations.values())
        utilization = total_used / total_allocated if total_allocated > 0 else 0
        print(f"Arena: {total_allocated / (1024 * 1024):.2f} MB")
        print(f"In-use: {total_used / (1024 * 1024):.2f} MB")
        print(f"Utilization: {utilization:.2f}")

if __name__ == "__main__":
    allocator = Allocator()
    
    with open("allocator\inputdata.txt", "r") as file:
        n = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                allocator.free(int(req[1]))

            # if n%100 == 0:
            #     print(n, "...")
            
            n += 1
    
    allocator.print_stats()












