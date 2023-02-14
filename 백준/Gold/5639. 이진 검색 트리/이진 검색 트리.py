import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

class Node() :
    def __init__(self, item):
        self.item = item
        self.lc = None
        self.rc = None

    def insert(self, toBeInsert) :
        #print(toBeInsert, " 넣는 중...")

        if toBeInsert < self.item :
            if self.lc == None :
                self.lc = Node(toBeInsert)
            else : #
                self.lc.insert(toBeInsert)

        else :
            if self.rc == None :
                self.rc = Node(toBeInsert)
            else :
                self.rc.insert(toBeInsert)


nums = []

while True :
    try :
        nums.append(int(input()))
    except :
        break

Tree = {}


Tree[nums[0]] = Node(nums[0])

for i in range(1, len(nums)) :
    Tree[nums[0]].insert(nums[i])


def postOrder(node) :
    #print(node.lc)
    #print(node.rc)
    if node.lc != None :
        #print("NODE LC 가 NONE 이 아님니다")
        postOrder(node.lc)
    if node.rc != None :
        #print("NODE RC 가 NONE 이 아님니다")
        postOrder(node.rc)
    print(node.item, end='\n')


postOrder(Tree[nums[0]])

#print(Tree)