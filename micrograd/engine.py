
class Value:
    """ stores a single scalar value and its gradient """

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        # internal variables used for autograd graph construction
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op # the op that produced this node, for graphviz / debugging / etc

    # addition operator
    def __add__(self, other):
        # if it is in correct format go ahead otherwise wrap it in Value
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out

    # multiplication operator
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out

    # power operator
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out

    # Rectified Linear Unit activation
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    def backward(self):

        # topological order all of the children in the graph
        topo = []
        visited = set()
        
        # topological sort algorithm
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        self.grad = 1
        for v in reversed(topo):
            v._backward()

    # Negation operator
    def __neg__(self): # -self
        return self * -1

    # reorder addition so that we could use __add__
    def __radd__(self, other): # other + self
        return self + other

    # subtract operator
    def __sub__(self, other): # self - other
        return self + (-other)

    # reorder subtraction so that we could use __sub__
    def __rsub__(self, other): # other - self
        return other + (-self)

    # reorder multiplication so that we could use __mul__
    def __rmul__(self, other): # other * self
        return self * other

    # division operator
    def __truediv__(self, other): # self / other
        return self * other**-1

    # reorder division so that we could use __truediv__
    def __rtruediv__(self, other): # other / self
        return other * self**-1

    # called when we print the object
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"