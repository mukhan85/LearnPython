import pip


class Animal(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def __repr__(self):
        return "Animal: " + self.name


cat = Animal("Cat")

print(cat)

# print(platform.platform())
print(pip.pep425tags.get_supported())
