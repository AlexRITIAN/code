import collections
import pprint

print(collections.Counter("abbccc"))
print(collections.Counter({"aaaa": 2, "cc": 3}))
print(collections.Counter(abc=1, efg=3))

pprint.pprint(pprint.pformat(collections.Counter("abbccc")))
pprint.pprint(pprint.pformat(collections.Counter({"aaaa": 2, "cc": 3})))
pprint.pprint(pprint.pformat(collections.Counter(abc=1, efg=3)))
