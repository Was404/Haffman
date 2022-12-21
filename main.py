import heapq
from collections import Counter
from collections import namedtuple

# структура дерева
class Node(namedtuple("Node", ["left", "right"])):  # класс внутренних узлов
    def walk(self, code, arret):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, arret + "0")  # пойти с левого потомка, добавив к префиксу "0"
        self.right.walk(code, arret + "1")  # затем пойти с правого потомка, добавив к префиксу "1"

class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева
    def walk(self, code, arret):
        code[self.char] = arret or "0"

def huffman_encode(s):
    order_with_P = []
    for ch, freq in Counter(s).items(): # Counter сколько раз каждый символ встречается в строке
        order_with_P.append((freq, len(order_with_P ), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(order_with_P)
    count = len(order_with_P)
    while len(order_with_P) > 1:
        fq1, _ct1, left = heapq.heappop(order_with_P )  # вытащим элемент с минимальной частотой - левый узел
        fq2, _ct2, right = heapq.heappop(order_with_P )  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
        heapq.heappush(order_with_P , (fq1 + fq2, count, Node(left, right))) # добавим новый внутренний узел у которого
                                                                     # потомки left и right соответственно
        count += 1
    code = {}  # инициализируем словарь кодов символов
    if order_with_P :  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = order_with_P   # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        root.walk(code, "")  # обход дерева от корня и заполнение code
    return code  # возвращаем словарь символов и соответствующих им кодов

def main():
    s = input()  #  до 10**4
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print("{}| {}".format(" "*6+ch, code[ch]))  # выведем символ и соответствующий ему код
    print("закодированное предложение: ",encoded)  # выведем  строку

if __name__ == "__main__":
    main()
