from store.in_memory_store import InMemoryStore

def test_add():
    store = InMemoryStore()
    assert store.add('short', 'long')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long2') == False
    assert store.add('', '') == False
    assert store.add(None, '') == False

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
    assert store.get('') is None
    assert store.get(None) is None
