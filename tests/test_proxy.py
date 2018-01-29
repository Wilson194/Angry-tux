from angrytux.proxy.Proxy import Proxy
import pytest
from io import StringIO
import sys


@pytest.mark.parametrize('function_name', ('not_existing_function', 'its_a_trap'))
def test_proxy_caller_not_existing_functions(function_name):
    proxy = Proxy()
    with pytest.raises(AttributeError):
        getattr(proxy, function_name)()


@pytest.mark.parametrize(['function_name', 'parameters'],
                         [('change_gravity', [10]),
                          ('change_cannon_state', []),
                          ('move_cannon', [10, 20])])
def test_proxy_caller_existing_functions(function_name, parameters):
    proxy = Proxy()

    old_std = sys.stdout
    result_std = StringIO()
    sys.stdout = result_std
    getattr(proxy, function_name)(*parameters)

    if not parameters:
        assert result_std.getvalue() == ''
    else:
        for string in parameters:
            assert str(string) in result_std.getvalue()
    sys.stdout = old_std
