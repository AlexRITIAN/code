formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % ("i had this thing",
        "That you could up right",
        "But it didn't sing",
        "So i said goodnight"))
print(formatter % ("中文模式","中文模式","中文模式","中文模式"))