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
    Reference_Manual_List.append(f'{i * 5 + j} | {major} | {minor}')

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
