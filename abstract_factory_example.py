from abc import abstractmethod, ABC
import random


class Keyboard(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

class KeyboardWired(Keyboard):
    def connect(self) -> None:
        print('Plug in USB to your computer')

class KeyboardWireless(Keyboard):
    def connect(self) -> None:
        print('Use bluetooth settings to pair new device!')

class Mouse(ABC):
    @abstractmethod
    def click(self) -> None:
        pass

class MouseWired(Mouse):
    def click(self) -> None:
        print('Click! I\'m clickn faster since I\'m pro gamers wired stuff')

class MouseWireless(Mouse):
    def click(self) -> None:
        print('.... what, ah, ok... (one hour later...) click!')

class AccessoriesFactory(ABC):
    @abstractmethod
    def create_mouse() -> Mouse:
        pass
    @abstractmethod
    def create_keyboard() -> Keyboard:
        pass

class AccessoriesFactoryWired(AccessoriesFactory):
    def create_mouse(self) -> MouseWired:
        return MouseWired()
    def create_keyboard(self) -> KeyboardWired:
        return KeyboardWired()
    
class AccessoriesFactoryWireless(AccessoriesFactory):
    def create_mouse(self) -> MouseWireless:
        return MouseWireless()
    
    def create_keyboard(self) -> KeyboardWireless:
        return KeyboardWireless()

def client_set(factory: AccessoriesFactory):
    print('preparing set of accessories for your system')
    mouse = factory.create_mouse()
    keyboard = factory.create_keyboard()
    return mouse, keyboard

def main():
    bluetooth_conditions = [True, False] 
    has_bluetooth = random.choice(bluetooth_conditions)
    
    if has_bluetooth:
        custom_factory = AccessoriesFactoryWireless()
    else:
        custom_factory = AccessoriesFactoryWired()

    mouse, keyboard = client_set(custom_factory)
    mouse.click()
    keyboard.connect()

if __name__=='__main__':
    main()