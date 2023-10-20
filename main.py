import heapq
from collections import Counter
from collections import namedtuple
#from gui import user_input
# структура дерева
class Node(namedtuple("Node", ["left", "right"])):  
    def walk(self, code, arret):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, arret + "0") 
        self.right.walk(code, arret + "1")  

class Leaf(namedtuple("Leaf", ["char"])): 
    def walk(self, code, arret):
        code[self.char] = arret or "0"

def huffman_encode(s):
    order_with_P = []
    for ch, freq in Counter(s).items(): 
        order_with_P.append((freq, len(order_with_P ), Leaf(ch))) 
    heapq.heapify(order_with_P)
    count = len(order_with_P)
    while len(order_with_P) > 1:
        fq1, _ct1, left = heapq.heappop(order_with_P ) 
        fq2, _ct2, right = heapq.heappop(order_with_P ) 
        # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
        heapq.heappush(order_with_P , (fq1 + fq2, count, Node(left, right)))
                                                                     
        count += 1
    code = {}  
    if order_with_P : 
        [(_freq, _count, root)] = order_with_P   
        root.walk(code, "") 
    return code 

def main():
    s = input()  #  до 10**4
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}| {}".format(" "*6+ch, code[ch])) 
    print("закодированное предложение: ",encoded) 

if __name__ == "__main__":
    main()
