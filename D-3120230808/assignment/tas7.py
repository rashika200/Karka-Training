strs=["flower","flow","flight"]
def longest_common_prefix(strs):
    if not strs:
        return ""   
    prefix = strs[0]   
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return "" 
    return prefix
print(longest_common_prefix(strs))