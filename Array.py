class Array():
    def __init__(self, array):
        self.array = array

    def find_element(self, num1):
        try:
            if num1 in self.array:
                print(f"{num1} found in array")
            else:
                print(f"{num1} not found in array")
        except:
            print("Error in code")
            pass

    def printFirstElements(self, num1):
        return self.array[:num1]

    def printLastElements(self, num1):
        return self.array[num1::]
        
    def updateElement(self, num1, num2):
        return self.array.insert(num1, num2)

    def addElement(self, num1):
        print(f"{num1} has been added in array\nArray is now: {self.array}")
        pass

    def removeElement(self, num1):
        x = self.array.pop(num1)
        print(f"{x} has been removed from array\nArray is now: {self.array}")
        pass

    def print_elements(self, num1, num2):
        return self.array[num1:num2]

    def reverse(self):
        return self.array[::-1]

    def printArray(self):
        print(self.array)
