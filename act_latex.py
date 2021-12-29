import latex 
import latex_nodes 

s = ""

f = open('input.txt', 'r')

for line in f:
    if line == "\n": 
        break
    if line[0] == '-':
        s += "-"
    else:
        s += line[:-1] + "#"

f.close()
tree = latex.parse(s, types=latex_nodes)
print(tree.compute())