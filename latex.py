# This file was generated from latex.peg
# See http://canopy.jcoglan.com/ for documentation.

from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.N1 = elements[0]
        self.N = elements[2]
        self.K = elements[1]
        self.N2 = elements[2]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.A = elements[0]
        self.N = elements[1]
        self.D = elements[2]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.A = elements[0]
        self.D = elements[1]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.M = elements[0]
        self.B = elements[1]
        self.A = elements[2]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.M = elements[0]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self.B = elements[1]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.A = elements[0]
        self.N = elements[1]
        self.D = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[-]')
    REGEX_2 = re.compile('^[A-Za-z0-9" "]')

    def _read_S(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['S'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_N()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_K()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_N()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'SNode1', (cls0, self._types.SNode1), {})
        self._cache['S'][index0] = (address0, self._offset)
        return address0

    def _read_K(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['K'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_A()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_N()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_D()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode2(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'KNode', (cls0, self._types.KNode), {})
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address4 = FAILURE
            address4 = self._read_A()
            if address4 is not FAILURE:
                elements1.append(address4)
                address5 = FAILURE
                address5 = self._read_D()
                if address5 is not FAILURE:
                    elements1.append(address5)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode3(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'KNode1', (cls1, self._types.KNode1), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['K'][index0] = (address0, self._offset)
        return address0

    def _read_A(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['A'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_M()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_B()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_A()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode4(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'ANode1', (cls0, self._types.ANode1), {})
        if address0 is FAILURE:
            self._offset = index1
            index3, elements1 = self._offset, []
            address4 = FAILURE
            address4 = self._read_M()
            if address4 is not FAILURE:
                elements1.append(address4)
                address5 = FAILURE
                chunk0 = None
                if self._offset < self._input_size:
                    chunk0 = self._input[self._offset:self._offset + 1]
                if chunk0 == '#':
                    address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"#"')
                if address5 is not FAILURE:
                    elements1.append(address5)
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode5(self._input[index3:self._offset], index3, elements1)
                self._offset = self._offset
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'ANode2', (cls1, self._types.ANode2), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['A'][index0] = (address0, self._offset)
        return address0

    def _read_B(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['B'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '|':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"|"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_B()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode6(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'BNode1', (cls0, self._types.BNode1), {})
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '|':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"|"')
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'BNode2', (cls1, self._types.BNode2), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['B'][index0] = (address0, self._offset)
        return address0

    def _read_D(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['D'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_A()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_N()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_D()
                if address3 is not FAILURE:
                    elements0.append(address3)
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode7(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'DNode2', (cls0, self._types.DNode2), {})
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_A()
            if address0 is not FAILURE:
                cls1 = type(address0)
                address0.__class__ = type(cls1.__name__ + 'DNode1', (cls1, self._types.DNode1), {})
            if address0 is FAILURE:
                self._offset = index1
        self._cache['D'][index0] = (address0, self._offset)
        return address0

    def _read_N(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['N'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[-]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'NNode', (cls0, self._types.NNode), {})
        self._cache['N'][index0] = (address0, self._offset)
        return address0

    def _read_M(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['M'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 1]
            if chunk0 is not None and Grammar.REGEX_2.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[A-Za-z0-9" "]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        if address0 is not FAILURE:
            cls0 = type(address0)
            address0.__class__ = type(cls0.__name__ + 'MNode', (cls0, self._types.MNode), {})
        self._cache['M'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_S()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
