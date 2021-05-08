from store.in_memory_store import InMemoryStore
import pytest

def test_add():
    store = InMemoryStore()
    assert store.add('short', 'long')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long2') == False
    with pytest.raises(ValueError):
        store.add('', '')
    with pytest.raises(ValueError):
        store.add(None, '')

def test_get():
    store = InMemoryStore()
    store.add('short', 'long')
    store.add('short1', 'long1')
    store.add('short1', 'longlong')
    store.add('short2', 'long2')

    assert store.get('short') == 'long'
    assert store.get('short1') == 'long1'
    assert store.get('short2') == 'long2'
    assert store.get('short3') is None
    with pytest.raises(ValueError):
        store.get('')
    with pytest.raises(ValueError):
        store.get(None)

def test_update():
    store = InMemoryStore()
    assert store.add('short', 'long', 'user')
    assert store.add('short1', 'long1', 'user')
    assert store.add('short1', 'long1', 'user')
    assert store.get('short1') == 'long1'
    assert store.update('short1', 'long2', 'user')
    assert store.get('short1') == 'long2'
    assert store.add('short1', 'longlong') == False
    assert store.update('short', 'longlong', 'user2') == False
    with pytest.raises(ValueError):
        assert store.update('short1', '', '')