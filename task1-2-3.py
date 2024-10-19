class TreeNode:
    def __init__(self, key):
        # Ініціалізація вузла дерева
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол
        self.val = key  # Значення вузла

class BinarySearchTree:
    def __init__(self):
        # Ініціалізація кореня дерева
        self.root = None

    def insert(self, key):
        # Вставка нового значення у дерево
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        # Рекурсивна вставка нового значення у дерево
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        # Знаходження найбільшого значення у дереві
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        # Рекурсивний пошук найбільшого значення
        current = node
        while current.right is not None:
            current = current.right
        return current.val

    def find_min(self):
        # Знаходження найменшого значення у дереві
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        # Рекурсивний пошук найменшого значення
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def sum_values(self):
        # Обчислення суми всіх значень у дереві
        return self._sum_values(self.root)

    def _sum_values(self, node):
        # Рекурсивний обхід дерева для обчислення суми
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)

# Приклад використання
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(15)
    bst.insert(30)

    print("Найбільше значення у дереві:", bst.find_max())
    print("Найменше значення у дереві:", bst.find_min())
    print("Сума всіх значень у дереві:", bst.sum_values())