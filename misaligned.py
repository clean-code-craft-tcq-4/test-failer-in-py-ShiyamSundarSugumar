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
    str = ('{0:4} | {1:5}  | {2:6}'.format((i * 5 + j + 1),major,minor))
    str1 = (f'{i * 5 + j + 1} \t | {major}   \t | {minor}')
    print (str)
    Reference_Manual_List.append(str)

result = print_color_map()
assert(result == 25)
print(Reference_Manual_List[0])
print(Reference_Manual_List[24])
print(Reference_Manual_List[0].find('|'))
print(Reference_Manual_List[24].find('|'))
#assert(Reference_Manual_List[0].find('|') == Reference_Manual_List[24].find('|') )
print("All is well (maybe!)\n")
