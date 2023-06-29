import demo
import pytest

# Agrupando por classes para deixar mais claro a especificidade de cada teste
class TestAdd:

    # Estrutura básica do teste
    def test(self):
        # Arrange: Configurando os parâmetros necessários para o teste
        calculator = demo.Calculator()

        # Act: Executando o que precisa ser testado
        result = calculator.add(2, 2)

        # Assert: Verificando se o resultado está correto
        assert result == 4

    # Teste de Exceptions
    def test_add_error(self, instance_calculator):
        # Neste bloco de código, usamos o pytest para verificar se ocorre uma exceção específica
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
        # Cada tupla configurada no parametrize é executada separadamente
        assert instance_calculator.add(a, b) == expected

    def test_output(self, capsys, instance_calculator):
        # Capturando a saída do método add usando capsys
        instance_calculator.add(2, 2)
        
        captured = capsys.readouterr()
        
        # Verificando se a saída está correta
        assert captured.out == f"adicao executada\n"
        assert captured.err == "sem erros"
        
    def test_with_mock(self, monkeypatch, instance_calculator):
        def mock_add(self, a, b):
            return 42
        
        # monkeypatch substitui o comportamento padrão da função "add" pelo "mock_add"
        monkeypatch.setattr(demo.Calculator, "add", mock_add)

        assert instance_calculator.add(2, 2) == 42
