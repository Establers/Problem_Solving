# 트리 순회
class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def 전위순회(node) :
    print(node.item, end = '')
    if node.left != '.' :
        전위순회(tree[node.left])
    if node.right != '.' :
        전위순회(tree[node.right])

def 후위순회(node) :
    if node.left != '.' :
        후위순회(tree[node.left])
    if node.right != '.' :
        후위순회(tree[node.right])
    print(node.item, end='')

def 중위순회(node) :
    if node.left != '.' :
        중위순회(tree[node.left])
    print(node.item, end='')
    if node.right != '.' :
        중위순회(tree[node.right])



import sys
input = sys.stdin.readline

n = int(input())

# 노드/ 왼자식/ 오자식
tree = {}
for i in range(n) :
    p, rc, lc = input().split()
    tree[p] = Node(p,rc,lc)

전위순회(tree['A'])
print("\n",end='')
중위순회(tree['A'])
print("\n",end='')
후위순회(tree['A'])




