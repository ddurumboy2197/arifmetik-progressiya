**Pytest uchun test kod**
```python
import pytest
from arifmetik_progressiya import ArifmetikProgressiya

def test_arifmetik_progressiya():
    ap = ArifmetikProgressiya(1, 2, 3)
    assert ap.terminal() == 1
    assert ap.next() == 2
    assert ap.next() == 3
    assert ap.next() == 4

def test_arifmetik_progressiya_empty():
    ap = ArifmetikProgressiya()
    assert ap.terminal() is None
    assert ap.next() is None

def test_arifmetik_progressiya_invalid():
    with pytest.raises(ValueError):
        ArifmetikProgressiya(1, 2, 4)
```

**Jest uchun test kod**
```javascript
import ArifmetikProgressiya from './arifmetik-progressiya';

describe('ArifmetikProgressiya', () => {
  it('terminal', () => {
    const ap = new ArifmetikProgressiya(1, 2, 3);
    expect(ap.terminal()).toBe(1);
  });

  it('next', () => {
    const ap = new ArifmetikProgressiya(1, 2, 3);
    expect(ap.next()).toBe(2);
    expect(ap.next()).toBe(3);
    expect(ap.next()).toBe(4);
  });

  it('empty', () => {
    const ap = new ArifmetikProgressiya();
    expect(ap.terminal()).toBeNull();
    expect(ap.next()).toBeNull();
  });

  it('invalid', () => {
    expect(() => new ArifmetikProgressiya(1, 2, 4)).toThrowError();
  });
});
```
