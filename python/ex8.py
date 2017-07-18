import os

for filename in os.listdir():
    name_list = list(filename)
    old_ext = ".txt"
    new_ext = ".py"
    if os.path.splitext(filename)[1] == old_ext:
        name_list[len(name_list) - len(old_ext):] = list(new_ext)
        os.rename(
            filename,''.join(name_list)
        )