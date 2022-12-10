import heapq
import math
from HuffmanNode import HuffmanNode
from operator import itemgetter


class Huffman:

    def __init__(self):
        self.heap = []
        self.codes = {}
        self.frequency = {}
        self.reverse_mapping = {}
        self.summary = []
        self.root_node = None

    def encode(self, data, frequency_dict=None):
        """
        :param data: string to encode
        :param frequency_dict: frequencies dict (Optional)
        :return: byte array of the encoded result
        """
        data.rstrip()
        """
        If frequency_dict arrives by parameter, we assign it.
        Else we build the frequency_dict.
        """
        if frequency_dict:
            self.frequency = frequency_dict
        else:
            self.frequency = self.__make_frequency_dict(data)

        self.__make_heap(self.frequency)
        self.__merge_nodes()
        
        self.root_node = self.heap[0]

        self.__make_codes()
        self.__make_summary()
        
        encoded_text = self.__get_encoded_text(data)
        padded_encoded_text = self.__pad_encoded_text(encoded_text)

        b = self.__get_byte_array(padded_encoded_text)
        return bytes(b)

    def decode(self, bts):
        """
        :param bts: byte array to decode
        :return: decoded string
        """
        bit_string = ""
        for byte in bts:
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits

        encoded_text = self.__remove_padding(bit_string)
        decompressed_text = self.__decode_text(encoded_text)
        return decompressed_text

    def print_huffman_tree(self):
        print(self.root_node.to_json())

    def print_summary_ordered_by_probability(self):
        summary_ordered_by_probability = sorted(self.summary, key=itemgetter("probability"), reverse=True)
        print("{}{}{}{}{}".format(
            "CARACTER".ljust(10),
            "FRECUENCIA".ljust(15),
            "PROBABILIDAD".ljust(25),
            "CODIGO".ljust(10),
            "NUM_DE_BITS".ljust(10))
        )

        for record in summary_ordered_by_probability:
            print("{}{}{}{}{}".format(
                record["character"].ljust(10),
                str(record["frequency"]).ljust(15),
                str(record["probability"]).ljust(25),
                record["code"].ljust(10),
                str(record["bits_number"]).ljust(10))
            )

    def calculate_average_length(self):
        """
        L = ∑ P(i) x No. of bits
        """
        return sum([record["probability"] * record["bits_number"] for record in self.summary])

    def calculate_entropy(self):
        """
        negative sum of { Prob(source letter i) * log_2(Prob(source letter i)) }
        """
        return -sum([record["probability"] * math.log(record["probability"], 2) for record in self.summary])

    def __make_summary(self):
        total_freq = self.__make_total_freq()
        self.summary = []
        for code in self.codes:
            prob = self.frequency[code] / total_freq
            num_bits = len(self.codes[code])
            self.summary.append({
                "character": code,
                "frequency": self.frequency[code],
                "probability": self.frequency[code] / total_freq,
                "code": self.codes[code],
                "bits_number": num_bits
            })

    def __make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if character not in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def __make_total_freq(self):
        tot = 0
        for c in self.frequency:
            tot += self.frequency[c]

        return tot

    def __make_heap(self, frequency):
        for key in frequency:
            node = HuffmanNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def __merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def __make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.__make_codes_helper(root.left, current_code + "0")
        self.__make_codes_helper(root.right, current_code + "1")

    def __make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.__make_codes_helper(root, current_code)

    def __get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def __pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def __get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def __remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def __decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

