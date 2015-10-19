

from osp.hlom.utils import sanitize_query


def test_remove_punctuation():
    assert sanitize_query('Antonio (Flaminio),') == 'antonio flaminio'


def test_remove_numbers():
    assert sanitize_query('Keats, John, 1795-1821') == 'keats john'
