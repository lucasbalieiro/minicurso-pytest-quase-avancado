import demo
import pytest

#agrupamos por classes para deixar mais claro a especificidade de cada teste
class TestAdd:

    #Estrutura basica do teste
    def test(self):
        #Arrange: configuramos os parametros necessarios para o teste
        calculator = demo.Calculator()

        #Execute : Executamos o que precisa ser testado
        result = calculator.add(2,2)

        #Assert: Fazemos as verificacoes para saber se os testes passaram
        assert result == 4

    # Teste de Exceptions
    def test_add_error(self,instance_calculator):
        # neste gerenciador de contexto, fazemos o pytest esperar
        #  o lancamento de uma exception
        with pytest.raises(demo.CustomError):
            instance_calculator.add(666, 6)


    @pytest.mark.parametrize(
        "a, b, expected", 
        [
            (100, 100, 200),
            (-1, 100, 99)
        ]
    )
    def test_with_multiple_parameters(self, a, b, expected, instance_calculator):
        #cada tupla configurada no parametrize eh executada
        assert instance_calculator.add(a, b) == expected

    def test_output(self, capsys, instance_calculator):
        
        instance_calculator.add(2,2)
        
        captured = capsys.readouterr()
        
        assert captured.out == f"adicao executada\n"
        assert captured.err == "sem erros"
        
    def test_with_mock(self, monkeypatch, instance_calculator):
        def mock_add(self, a , b):
            return 42
        
        #monkeypatch subsitui o comportamento padrao de uma funcao
        # para o mock_add
        monkeypatch.setattr(demo.Calculator, "add", mock_add)

        assert instance_calculator.add(2,2) == 42
       

