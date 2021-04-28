from IWeapon import IWeapon


class WeaponStartApply:

    def __init__(self, weapon: IWeapon):
        self.__weapon = weapon

    def execute(self):
        self.__weapon.to_apply()
