"""Test whitespace is preserved between inline tags

poetry run pytest tests/test_html/test_preserve_inline_tag_whitespace.py
"""
import pytest

from src.djlint.reformat import formatter
from tests.conftest import printer

test_data = [
    pytest.param(
        (
            "<span>     </span>"
        ),
        (
            "<span> </span>"
        ),
        id="preserve_inline_whitespace_multiple",
    ),
    pytest.param(
        (
            "<span></span>"
        ),
        (
            "<span> </span>"
        ),
        id="preserve_inline_whitespace_no_spaces",
    ),
    pytest.param(
        (
            "<span> </span>"
        ),
        (
            "<span> </span>"
        ),
        id="preserve_inline_whitespace_single",
    )
]


@pytest.mark.parametrize(("source", "expected"), test_data)
def test_base(source, expected, basic_config):
    output = formatter(basic_config, source)

    printer(expected, source, output)
    assert expected == output
