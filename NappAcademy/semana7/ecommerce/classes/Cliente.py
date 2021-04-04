class Cliente:
    def __init__(self, nome):
<<<<<<< HEAD
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Cliente: ' + self._nome
=======
        self._name = nome

    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, value):
        self._name = value

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Cliente => ' + self._name
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
