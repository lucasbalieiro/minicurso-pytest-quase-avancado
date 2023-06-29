import pytest
import demo

#Usamos esta fixture para evitar duplicacao de codigo
@pytest.fixture
def instance_calculator() -> demo.Calculator:
    return demo.Calculator()