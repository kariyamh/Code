def add(a,b):
    return a+b

def dedupe_rows(rows):
    seen=set()
    out=[]
    for r in rows:
        t=tuple(r.items())
        if t in seen:
            continue
        seen.add(t)
        out.append(r)
    return out
