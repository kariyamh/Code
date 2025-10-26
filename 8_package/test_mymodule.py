import mymodule

def test_add():
    assert mymodule.add(2,3)==5

def test_dedupe():
    rows=[{"a":1},{"a":1},{"a":2}]
    out=mymodule.dedupe_rows(rows)
    assert len(out)==2

print("2 tests passed")
