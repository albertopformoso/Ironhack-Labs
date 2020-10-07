# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health   = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name     = name
        Soldier.__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy  = []
    
    def addViking(self, vikingo_nuevo):
        self.vikingArmy.append(vikingo_nuevo)

    def addSaxon(self, saxon_nuevo):
        self.saxonArmy.append(saxon_nuevo)

    def vikingAttack(self):
        saxon_soldier = self.saxonArmy[0]
        viking_soldier = self.vikingArmy[0]
        damage_received = saxon_soldier.receiveDamage(viking_soldier.attack())
        if saxon_soldier.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            self.saxonArmy.pop(0)

    def saxonAttack(self):
        saxon_soldier = self.saxonArmy[0]
        viking_soldier = self.vikingArmy[0]
        damage_received = viking_soldier.receiveDamage(saxon_soldier.attack())
        if viking_soldier.health > 0:
            return f'A Viking has received {damage} points of damage'
        else:
            self.vikingArmy.pop(0)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'
    
    
