from utils import dicts
import pytest


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"


@pytest.mark.parametrize("collection, key, default, expected", [
    ({}, "vcs", "git", "git"),
    ({}, "vcs", "bazaar", "bazaar")
])
def test_get_val(collection, key, default, expected):
    assert dicts.get_val(collection, key, default) == expected
