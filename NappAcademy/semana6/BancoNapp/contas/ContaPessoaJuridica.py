from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta corrente de pessoa jurídica.
    Limite padrão da conta: R$ 500,00
    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe ContaPessoaJuridica.
        """
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)
