def unique(el):
    new_list = []
    for i in el:
        if i not in new_list:
            new_list.append(i)
    print(new_list)



el = input().split()
unique(el)
