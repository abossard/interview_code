class Trie(object):

    root = None

    class Node(object):
        value = None
        children = None
        leaf = False

        def __init__(self, root=False):
            self.children = dict()
            self.root = root

        def insert(self, value):
            if self.root:
                self.value = ''
                self._find_node(value)
            else:
                self.value = value[:1]
                if len(value) > 1:
                    self._find_node(value[1:])
                else:
                    self.leaf = True

        def _find_node(self, value):
            if not value[:1] in self.children:
                self.children[value[:1]] = Trie.Node()
            self.children[value[:1]].insert(value)

        def __str__(self):
            output = ''
            output += self.value
            for childnode in self.children.itervalues():
                output += "(%s)" % (childnode,)
            return output

trie = Trie()
trie.root = Trie.Node(root=True)
trie.root.insert("lorem")
trie.root.insert("lorum")
trie.root.insert("loren")
trie.root.insert("larum")

print trie.root
