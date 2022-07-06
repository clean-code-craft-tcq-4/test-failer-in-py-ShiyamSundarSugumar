Reference_Manual_List = []
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            Concate_ReferenceManual(i,j,major,minor)         
            
    return len(major_colors) * len(minor_colors)

def Concate_ReferenceManual(i,j,major,minor):
    global Reference_Manual_List
    Reference_Manual_List.append(f'{i * 5 + j + 1} \t | {major} | \t {minor}')

result = print_color_map()
assert(result == 25)
assert(Reference_Manual_List[0].find("|") == Reference_Manual_List[24].find("|"))
print("All is well (maybe!)\n")
