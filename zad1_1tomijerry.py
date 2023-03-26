
import random

class Cat:
    def __init__(self, name="Tom"):
        self.name = name
        self.speed = 5
        self.hunger = 50
        self.tiredness = 0
    
    def hunt(self, mouse):
        distance = abs(self.position - mouse.position)
        
        if distance > 10:
            print("The mouse is too far away!")
            return
        
        time_to_catch = distance / (self.speed + mouse.speed)
        
        if time_to_catch > 10:
            print("The mouse is too fast!")
            return
        
        if mouse.hidden:
            print("Can't find the mouse!")
            return
        
        print("The cat caught the mouse!")
        self.hunger += 10
        self.tiredness += 5
        mouse.caught()
        
    def sleep(self):
        self.tiredness = 0
        self.hunger += 5
    
    def search(self, mouse):
        if mouse.hidden:
            print("Can't find the mouse!")
            return
        
        print("The cat found the mouse!")
        self.tiredness += 3
        self.hunger += 2
        
    def wander(self):
        print("The cat is wandering around...")
        self.tiredness += 10
    
    def is_alive(self):
        if self.hunger >= 100:
            print(f"{self.name} died of starvation!")
            return False
        if self.tiredness >= 100:
            print(f"{self.name} died of exhaustion!")
            return False
        return True

class Mouse:
    def __init__(self, name="Jerry"):
        self.name = name
        self.speed = 10
        self.hunger = 50
        self.tiredness = 0
        self.hidden = True
        self.position = 0
    
    def hide(self):
        self.hidden = True
        self.tiredness += 3
    
    def escape(self, cat):
        distance = abs(self.position - cat.position)
        
        if distance > 20:
            print("The cat is too far away!")
            return
        
        time_to_escape = distance / (self.speed + cat.speed)
        
        if time_to_escape > 10:
            print("The cat is too fast!")
            return
        
        self.position += 5
        self.tiredness += 5
        
        print("The mouse escaped!")
        
    def feed(self):
        self.hunger += 10
        self.tiredness += 5
    
    def caught(self):
        self.tiredness += 10
        self.hunger += 5
        self.hide()
        
    def is_alive(self):
        if self.hunger >= 100:
            print(f"{self.name} died of starvation!")
            return False
        if self.tiredness >= 100:
            print(f"{self.name} died of exhaustion!")
            return False
        return True

if __name__ == '__main__':
    cat = Cat()
    mouse = Mouse()
    
    for day in range(1, 8):
        print(f"Day {day}")
        if not cat.is_alive() or not mouse.is_alive():
            break
        
        if not mouse.hidden:
            cat.hunt(mouse)
        
        if mouse.hidden:
            if random.random() < 0.3:
                mouse.hidden = False
                print("The mouse came out of hiding!")
            else:
                cat.wander()
        
        if not mouse.hidden:
            mouse.escape(cat)
        
        if random.random() < 0.2:
            cat.search(mouse)
        
        if mouse.hunger <= 25:
            mouse.feed()
        
        if cat.tiredness >= 75:
            cat.sleep()
        
        print(f"Cat: Hunger {cat.hunger}, Tiredness {cat.tiredness}")
        print(f"Mouse: Hunger {mouse.hunger}, Tiredness {mouse.tiredness}")```