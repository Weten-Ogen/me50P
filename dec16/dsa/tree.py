class Tree:

    class Position:
        def element(self):
            raise NotImplementedError()
        
        def __eq__(self,other):
            pass

        def __ne__(self,other):
            pass

    def root(self):
        pass

    def parent(self):
        pass
    
    def num_children(self):
        pass

    def children(self):
        pass

    def __len__(self):
        pass

    def _is_root(self):
        pass

    def _is_leaf(self):
        pass
    def _is_empty(self):
        return len(self) == 0
