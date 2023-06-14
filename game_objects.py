class GameManager():
    def __init__(self, m_cash) -> None:
        self.m_cash = m_cash

    def newGame() -> None:
        pass

    def endGame() -> None:
        pass

class GameObject(GameManager):
    def __init__(self, m_cash, name, tag, enabled) -> None:
        super().__init__(m_cash)
        self.name = name
        self.tag = tag
        self.enabled = enabled

    def onCollision(self,) -> None:
        pass

    def isEnabled(self,) -> bool:
        pass

    def setName(self, name) -> None:
        self.name = name

    def setTag(self, tag) -> None:
        self.tag = tag
    
    def setEnabled(self, enabled) -> None:
        self.enabled = enabled

class Player(GameObject):
    def __init__(self, name, tag, enabled , m_health: int) -> None:
        super().__init__(name, tag, enabled)
        self.m_health = m_health
    
    def isAlive(self,) -> bool:
        pass
    
    def accelerate(self,) -> None:
        pass
        
    def brake(self,) -> None:
        pass
            
    def steeRight(self,) -> None:
        pass
             
    def steeLeft(self,) -> None:
        pass
             
    def applyDamage(self,) -> None:
        pass

class TrafficCar(GameObject):
    def __init__(self, name, tag, enabled, damage: int, cash: float) -> None:
        super().__init__(name, tag, enabled)
        self.damage = damage
        self.cash = cash
    
    def getDamage() -> int:
        pass

    def GetCash() -> int:
        pass

class Sedan(TrafficCar):
    def onCollision(self) -> None:
        return super().onCollision()

class Van(TrafficCar):
    def onCollision(self) -> None:
        return super().onCollision()

class Truck(TrafficCar):
    def onCollision(self) -> None:
        return super().onCollision()

class SideObject(GameObject):
    def __init__(self, name, tag, enabled, damage: int, cash: int, count: int) -> None:
        super().__init__(name, tag, enabled)
        self.damage = damage
        self.cash = cash
        self.count = count

class Firehydrant(SideObject):
    def __init__(self, name, tag, enabled, damage: int, cash: int, count: int) -> None:
        super().__init__(name, tag, enabled, damage, cash, count)
    
    def onCollision(self) -> None:
        return super().onCollision()

class LetterBox(SideObject):
    def __init__(self, name, tag, enabled, damage: int, cash: int, count: int) -> None:
        super().__init__(name, tag, enabled, damage, cash, count)

class Sparks():
    pass