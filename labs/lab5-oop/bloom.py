class BloomFilter:

    def __init__(self, size, hashCount=2):
        self.filter = [0] * size
        self.size = size
        self.hashCount = hashCount

    def add(self, elem):
        h = hash(elem)
        for _ in range(self.hashCount):
            self.filter[h % self.size] = 1
            h = hash(h)

    def __contains__(self, elem):
        h = hash(elem)
        for _ in range(self.hashCount):
            if self.filter[h % self.size] == 0:
                return False
            h = hash(h)    
        return True    


def main():
    bf = BloomFilter(20)
    animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle']
    for animal in animals:
        bf.add(animal)

    print(bf.filter)    
    for animal in animals:
        print(animal in bf, end = ' ')
    print()    
    print('bird' in bf)

if __name__ == '__main__':
    main()

