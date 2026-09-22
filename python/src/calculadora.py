class calculadoraFisica:
    CONSTANTE_GRAVITACIONAL = 9.81

    @staticmethod
    def energiaPotencial(massa, altura):
        return massa * calculadoraFisica.CONSTANTE_GRAVITACIONAL * altura