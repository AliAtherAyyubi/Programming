
def longestCommonPrefix(strs):
    prefix=''
    if len(strs)==0:
        return prefix
    else:
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != char:
                    return prefix
            prefix += char
        
        return prefix

            
# Test cases

strs=["fligher","fligh","flight"]
print(longestCommonPrefix(strs))  # Output: "fl"