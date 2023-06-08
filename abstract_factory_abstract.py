from abc import ABC, abstractmethod



class AbstractProductA(ABC):
    '''
    general component or type of product:
    checkbox
    cabinet
    
    '''

    @abstractmethod
    def custom_method_a(self):
        pass

    @abstractmethod
    def another_custom_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    '''
    custom component or type of product:
    win_checkbox
    wooden_cabinet
    
    '''
    def custom_method_a(self):
        print('custom method a implementation')

    def another_custom_a(self):
        print('another custom method a implementation')

class ConcreteProductA2(AbstractProductA):
    '''
    custom component or type of product:
    win_checkbox
    wooden_cabinet
    
    '''
    def custom_method_a(self):
        print('custom method a implementation')
    def another_custom_a(self):
        print('another custom method a implementation')

class AbstractProductB(ABC):
    '''
    general component or type of product:
    checkbox
    cabinet
    
    '''
    @abstractmethod
    def custom_method_b(self):
        pass

    @abstractmethod
    def another_custom_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    '''
    custom component or type of product:
    win_checkbox
    wooden_cabinet
    
    '''
    def custom_method_b(self):
        print('custom method B implementation WHITE')

    def another_custom_b(self):
        print('another custom method b implementation')

class ConcreteProductB2(AbstractProductB):
    def custom_method_b(self):
        print('custom method B implementation BLACK')

    def another_custom_b(self):
        print('another custom method b implementation')




class AbstractProductFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
    
class ConcreteProductFactory1(AbstractProductFactory):
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()
    
class ConcreteProductFactory2(AbstractProductFactory):
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()
    
    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()
    
   
def client_code(factory: AbstractProductFactory):
    products = []
    product1 = factory.create_product_a()
    product2 = factory.create_product_b()

    products.append(product1)
    products.append(product2)

    return products



def main():
    factory = ConcreteProductFactory2()
    products = client_code(factory)
    for product in products:
        print(product)




if __name__ == "__main__":
    main()
