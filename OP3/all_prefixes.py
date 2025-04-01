'''Prefixes function'''
def all_prefixes(line:str):
    '''Looks for compilations'''
    set_ = set(line[0])
    line = line.lower()
    for i in range (1, len(line)+1):
        set_.add(line[:i])
    first_letter = line[0]
    indexes = []
    for i in range(len(line)):
        if line[i] == first_letter:
            indexes.append(i)
    for start in indexes:
        for end in range(start + 1, len(line) + 1):
            set_.add(line[start:end])
    return set_
print(all_prefixes('lll'))
