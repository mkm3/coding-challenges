class Node(object):
    """Doubly-linked node in a tree.

        >>> na = Node("na")
        >>> nb1 = Node("nb1")
        >>> nb2 = Node("nb2")

        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)

        >>> na.children
        [<Node nb1>, <Node nb2>]

        >>> nb1.parent
        <Node na>
    """

    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.

        Also sets the children of the parent to include this node.
        """

        self.parent = parent
        parent.children.append(self)

    def cousins(self):
        """Find nodes on the same level as this node."""

        current = self
        sought_depth = 0

        while current.parent is not None:
            sought_depth += 1
            current = current.parent
            
        cousins = set()

        # Recursive function to find examine a node, decide whether to
        # consider it a cousin, and to explore its children.
        #
        # We could make this a free-standing function outside of the class,
        # of a method of the class -- but we don't need access to the
        # `self`, and by nesting this, we'll have access to the
        # `cousins` and `sought_depth` variables, so we conveniently don't
        # need to pass them around explicitly.

        def _cousins(node, curr_depth):

            # Base case: we're a leaf node, so can't look further
            if node is None:
                return

            # Second base case: we're at the right level, so don't need
            # to look further
            if curr_depth == sought_depth:
                cousins.add(node)
                return

            for child in node.children:
                # Look at the children, noting that we're one level deeper then.
                _cousins(child, curr_depth + 1)

        _cousins(node=current, curr_depth=0)

        # We don't want to include the original node
        cousins.remove(self)
        return cousins

b.cousins() == {c, d} # True
c.cousins() == {b, d} # True
e.cousins() == {f, g, h, i, j} # True
k.cousins() == {l} # True
a.cousins() == set()   # empty set | True