class Methane:
    def __init__(self):
        pass

class Steam:
    def __init__(self, temp, pressure, impurity):
        self.temp = temp
        self.pressure = pressure
        self.impurity = impurity

class Ammonica:
    def __init__(self, catalizator1):
        self.catalizator = catalizator1

class Air:
    def __init__(self, percentO2):
        self.O2 = percentO2

class Nitrodioxide:
    def __init__(self, catalizator2):
        self.catalizator = catalizator2

class Nitroacid:
    def __init__(self):
        pass

class Camera:
    def __init__(self):
        pass

    def camera1(self, methane, steam, catalizator1: str):
        if (isinstance (methane, Methane)) and (isinstance (steam, Steam)):
            return Ammonica(catalizator1)
        else:
            raise ValueError("Ammonica can not be created this way")

    def camera2(self, ammonica, air, catalizator2: str):
        if (isinstance (ammonica, Ammonica)) and (isinstance (air, Air)):
            return Nitrodioxide(catalizator2)
        else:
            raise ValueError("Nitrodioxide can not be created this way")

class Filter:
    def __init__(self, firm, model, pollution, tolerable_pollution):
        self.firm = firm,
        self.model = model,
        self.pollution = pollution
        self.tolerable_pollution = tolerable_pollution

    def filtration(self, nitrodioxide: Nitrodioxide):
        if self.pollution >= self.tolerable_pollution - 1:
            raise ValueError("Pollution of the filter exceeded or almost exceeded its tolerable level")
        elif (not isinstance (nitrodioxide, Nitrodioxide)):
            raise ValueError("Nitric acid can not be created this way")
        else:
            self.tolerable_pollution += 1
            return Nitroacid()


#x = Filter(2, 3, 4, 6)
#cameras = Camera()
#m, s = Methane(), Steam(1, 2, 3)
#amm = cameras.camera1(m, s, "catalize1")
#print(amm.catalizator)
#air = Air(1)
#nd = cameras.camera2(amm, air, "catalize2")
#print(nd.catalizator)
#na = x.filtration(nd)
#print(na)
