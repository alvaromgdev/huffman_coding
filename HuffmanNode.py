import functools
import json


@functools.total_ordering
class HuffmanNode:
    """
    Class to represent a Huffman node.
    It has a character, a frequency, a left child node, a right child node.
    It implements __eq__ and __lt__ methods, to be easily sorted using heapq.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not isinstance(other, HuffmanNode):
            return False

        return self.freq == other.freq

    def __lt__(self, other):
        """
        It compares in first step by frequency,
        in second step (if same frequency detected), it compares by its character
        """
        if other is None:
            return False

        if not isinstance(other, HuffmanNode):
            return False

        res = self.freq - other.freq
        if res == 0:
            if self.char is not None and other.char is not None:
                return self.char < other.char
            else:
                if self.char is None:
                    return True
                elif other.char is None:
                    return True

        return res < 0


    def __repr__(self):
        return "char: {}, freq: {}, left: {}, right: {}".format(
            self.char, self.freq, self.left, self.right
        )

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

