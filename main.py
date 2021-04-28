from AK47 import AK47
from Gamer import Gamer
from Knife import Knife
from WeaponStartApply import WeaponStartApply

if __name__ == '__main__':
    weapon = AK47()

    onStartApply = WeaponStartApply(weapon)
    gamer = Gamer(onStartApply)
    gamer.execute()
