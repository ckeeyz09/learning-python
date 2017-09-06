class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal(self):
        print ("My name is {}".format(self.name))

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal(self):
        super(SuperHero, self).reveal()
        print ("... and I am also known as {}".format(self.hero_name))

sean = SuperHero("Sean", "Python Man")
sean.reveal()