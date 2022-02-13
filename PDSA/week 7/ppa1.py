class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

res = {}

def phuffman(node, prevVal = '', currVal=''):
    newVal = currVal+prevVal
    if node.left:
        phuffman(node.left, '0', newVal)
        
    if node.right:
        phuffman(node.right, '1', newVal)
        
    if not node.left and not node.right:
        res[node.symbol] = newVal

def Huffman(s):
    freq = {}
    for i in s:
        try:
            freq[i]+=1
        except KeyError:
            freq[i] = 1
    freqVal = list(freq.values())
    freqLet = list(freq.keys())
    # minfreq1 = min(freqa)
    # minlet1 = freql.pop(freqa.index(minfreq1))
    # minfreq1.pop(freqa.index(minfreq1))
    nodes = []
    for i in range(len(freqVal)):
        nodes.append(Node(freqVal[i], freqLet[i]))
    
    
    while(len(nodes) > 1):
        nodes = sorted(nodes, key = lambda x:x.symbol)
        nodes = sorted(nodes, key = lambda x:x.frequency)
        left = nodes[0]
        right = nodes[1]
        
        newnode = Node(left.frequency+right.frequency, left.symbol+right.symbol, left, right)
        
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newnode)
        
    phuffman(nodes[0])
    
    return res
    
s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])