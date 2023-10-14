import tkinter as tk
import heapq
from collections import Counter
from collections import namedtuple

# Constants
WIDTH = 500
HEIGHT = 500
RADIUS = 20

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

def on_button_click():
    user_input = entry.get("1.0", "end")
    s = user_input
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    rp = []
    for ch in sorted(code):
        rp.append("{}|{}".format(" "*6+ch, code[ch]))
        print("{}|{}".format(" "*6+ch, code[ch]))
    print("закодированное предложение: ",encoded)
    rp_string = "\n".join(rp) 
    entry.delete("1.0", "end")  # Очищаем поле ввода
    entry.insert("1.0", f"{len(code)}, {len(encoded)}{rp_string}, \nзакодированное предложение:\n{encoded}")  # Выводим сообщение в поле ввода
    

root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
entry = tk.Text(root, width=30, height=10, font=('Arial', 12))
entry.pack()

button = tk.Button(root, text="Нажмите", command=on_button_click)
button.pack()

root.mainloop()