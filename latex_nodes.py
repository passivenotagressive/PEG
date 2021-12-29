class SNode1:
    def compute(self):
        s = "\\begin{table}[]\n\\begin{tabular}" + "{|" + self.K.format() + "|}\n" 
        s += "\\hline\n" * self.N1.number() + self.K.compute() + " \\hline" * self.N2.number() + "\n"
        s += "\\end{tabular}\n\\end{table}"
        return s

class KNode:
    def compute(self):
        s = self.A.compute() + " \\hline " * self.N.number() + "\n" + self.D.compute()
        return s
    def format(self):
        return self.A.format()
class KNode1:
    def compute(self):
        s = self.A.compute() + self.D.compute()
        return s
    def format(self):
        return self.A.format()
class ANode1:
    def compute(self):
        return self.M.save() + " & " + self.A.compute()
    def format(self):
        return "l" + self.B.compute() + self.A.format()
class ANode2:
    def compute(self):
        return self.M.save() + " \\\\"
    def format(self):
        return "l"
class MNode:
    def save(self):
        return self.text
class BNode1:
    def compute(self):
        return "|" + self.B.compute()
class BNode2:
    def compute(self):
        return "|"
class DNode1:
    def compute(self):
        return self.A.compute()
class DNode2:
    def compute(self):
        return self.A.compute() + " \\hline " * self.N.number() + "\n" + self.D.compute()
class NNode:
    def number(self):
        return len(self.text)

