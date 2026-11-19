import importlib.util, os, sys
_t = importlib.util.spec_from_file_location("topics", os.path.join(os.path.dirname(__file__), "..", "factory", "topics.py")); topics = importlib.util.module_from_spec(_t); _t.loader.exec_module(topics)
S = []; C = []; T = []
def duo(id, segment, bucket, scene, hook, lines, end, cta, names=None, sound=None, **kw):
    d = dict(id=id, kind="duo3d", scene=scene, names=names, segment=segment, bucket=bucket, hook=hook, lines=lines, end=end, cta=cta, **kw)
    if sound: d["sound"] = sound
    S.append(d)
def chat(id, segment, bucket, hook, names, lines, end, cta, **kw): S.append(dict(id=id, kind="chat", segment=segment, bucket=bucket, hook=hook, names=names, lines=lines, end=end, cta=cta, **kw))
def lst(id, segment, bucket, hook, items, end, cta, **kw): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta, **kw))
def car(id, segment, tag, hook, slides, end, cta, **kw): C.append(dict(id=id, kind="carousel", segment=segment, tag=tag, hook=hook, slides=slides, end=end, cta=cta, **kw))
def tip(id, segment, title, body): T.append(dict(id=id, kind="tip", segment=segment, title=title, body=body))
def quiz(id, segment, q, a, why): T.append(dict(id=id, kind="quiz", segment=segment, q=q, a=a, why=why))
def contact(id, segment, line, kw): T.append(dict(id=id, kind="contact", segment=segment, line=line, kw=kw))
