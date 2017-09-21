
import pytest

from eth_abi.utils.parsing import (
    process_type,
)


@pytest.mark.parametrize(
    'typestr, expected_parse',
    (
        ('uint256', ('uint', '256', [])),
        ('uint', ('uint', '256', [])),
        ('function', ('bytes', '24', [])),
    )
)
def test_process_type(typestr, expected_parse):
    assert process_type(typestr) == expected_parse


@pytest.mark.parametrize(
    'typestr',
    (
        ('fixed0x1'),
        ('fixed264x1'),
        ('fixed9x1'),
        ('fixed256x0'),
        ('fixed256x81'),
        ('ufixed0x1'),
        ('ufixed264x1'),
        ('ufixed9x1'),
        ('ufixed256x0'),
        ('ufixed256x81'),
    )
)
def test_process_exceptions(typestr):
    with pytest.raises(ValueError):
        process_type(typestr)