class Car:
    name = "Old"
    drive = "front"
    state = 3

class Service:
    def __init__(self, car):
        self.car = car

    def upgrade_name(self, newname):
        self.car.name = newname
        return newname

    def upgrade_drive(self, newdrive):
        self.car.drive = newdrive
        return newdrive

    def upgrade_state(self, newstate):
        self.car.state = newstate
        return newstate

# создаем обьект машин
obj1_car = Car()
obj2_car = Car()

# создаем обьект авто-сервисов СТО
auto1_service = Service(obj1_car)
auto2_service = Service(obj2_car)

# В авто-сервисе1 обновляем и меняем запчасти в машине 1
up_name_car1 = auto1_service.upgrade_name("Audi A3")
up_drive_car1 = auto1_service.upgrade_drive("4x4")
up_state_car1 = auto1_service.upgrade_state(4)

car1 = {"marka": up_name_car1, "privod": up_drive_car1, "state car": up_state_car1}

print(car1)

# В авто сервисе2 обновляем и меняем запчасти в машине 1
up_name_car2 = auto2_service.upgrade_name("Nissan Qashqai")
up_drive_car2 = auto2_service.upgrade_drive("front")
up_state_car2 = auto2_service.upgrade_state(5)

car2 = {"marka": up_name_car2, "privod": up_drive_car2, "state car": up_state_car2}
print(car2)








