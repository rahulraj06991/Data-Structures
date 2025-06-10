def group_anagrams(list1):
    anagram = {}
    for item in list1:
       #canomical means the standardidzed or normalized form of a string
       canonical = ''.join(sorted(item))
       #print(canonical)
       if canonical in anagram:
           anagram[canonical].append(item)
       else:
           anagram[canonical] = [item]
    print(anagram)
    return list(anagram.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )