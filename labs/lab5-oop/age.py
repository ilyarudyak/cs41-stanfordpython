import sys


def getAge():
    while True:
        try:
            age = int(input('How old are you? '))
            if 0 < age and age < 123:
                return age
        except ValueError as e:
            print('Invalid integer input.')
        else:
            raise ValueError('Age {} is out of range'.format(age))

def main():
    print('age: {}'.format(getAge()))


if __name__ == '__main__':
    main()