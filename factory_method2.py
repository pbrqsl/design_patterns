class TypeOne:
    def __init__(self):
        self.property = "one"
        print('creting object of ClassOne')
        #print(f'{self.__name__}')

class TypeTwo:
    def __init__(self):
        self.property = "two"
        print('Creating Object of class two')


def NumberFactory(name: str):
    config = {
        'one': TypeOne,
        'two': TypeTwo
    }
    
    target_class = config.get(name, 'one')
    
    return target_class()


def main():
    NumberFactory('two')


if __name__ == "__main__":
    main()