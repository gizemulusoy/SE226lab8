from abc import ABC, abstractmethod

class FrequencyCounter(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass

class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_list = [0] * 26

        with open(self.address, 'r') as file:
            data = file.read().lower()

            for char in data:
                if char.isalpha():
                    index = ord(char) - ord('a')
                    frequency_list[index] += 1

        for i, frequency in enumerate(frequency_list):
            letter = chr(i + ord('a'))
            print(f"{letter} = {frequency}")

class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        frequency_dict = {}

        with open(self.address, 'r') as file:
            data = file.read().lower()

            for char in data:
                if char.isalpha():
                    if char in frequency_dict:
                        frequency_dict[char] += 1
                    else:
                        frequency_dict[char] = 1

        sorted_dict = dict(sorted(frequency_dict.items(), key=lambda x: x[0]))

        for letter, frequency in sorted_dict.items():
            print(f'"{letter}" {frequency}')




file_address = "weirdWords.txt"

list_counter = ListCount(file_address)
print("ListCount results:")
list_counter.calculateFreqs()
print(" \n----------------------------------------------")
dict_counter = DictCount(file_address)
print("\nDictCount results:")
dict_counter.calculateFreqs()