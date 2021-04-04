from ecommerce.classes.Cliente import Cliente


class TestCliente:

    clnts = ['José da Silva', 'José da Silva Júnior', 'John Doe']

    def test_class_declared(self):
        objeto = Cliente(self.clnts[2])
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente(self.clnts[0])
        assert objeto.nome == self.clnts[0]

    def test_setters(self):
        objeto = Cliente(self.clnts[0])
        assert objeto.nome == self.clnts[0]
        objeto.nome = self.clnts[1]
        assert objeto.nome == 'José da Silva Júnior'

    def test_str_repr(self):
        cliente = Cliente(self.clnts[0])
        assert str(cliente) == self.clnts[0]
        assert repr(cliente) == 'Cliente: José da Silva'
