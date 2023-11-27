class Dog:
    APPROVED_BREEDS = [
            "Mastiff",
            "Chihuahua",
            "Corgi",
            "Shar Pei",
            "Beagle",
            "French Bulldog",
            "Pug",
            "Pointer"
        ]
    def __init__(self, name="Fido", breed="Mastiff"):
        self.breed = breed
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or 1 <= len(name) <= 25:
            self._name = name
        else:
            print(f'Name must be string between 1 and 25 characters. if empty string.')

        name = property(get_name, set_name)

