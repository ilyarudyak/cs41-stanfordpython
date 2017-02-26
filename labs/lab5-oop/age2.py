class OutOfRangeError(ValueError):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


def getAge():
    while True:
        try:
            age = int(input('How old are you? '))
            if 0 < age and age < 123:
                return age
        except ValueError as e:
            print('Invalid integer input.')
        else:
            raise OutOfRangeError('Age {} is out of range'.format(age))

def main():
    print('age: {}'.format(getAge()))


if __name__ == '__main__':
    main()