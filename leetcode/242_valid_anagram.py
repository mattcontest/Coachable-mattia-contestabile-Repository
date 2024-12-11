#In this problem we are tasked to determine whether two strings are two valid anagrams.
#Two words are valid anagrams  iff they share the same frequency of chars
#Even if they are not in the same order.


#Loom Explanation: https://www.loom.com/share/73fb993f5e3d4071add705f9e0ac6bdf
def isAnagram(self, s: str, t: str) -> bool:
    #First we check whether these two words have the same lenght
    if(len(s) != len(t)):
        return False;
        
    #Second we create two empty hashmaps
    sCount = {};
    tCount = {};

    #We now check the frequency of each single character within both s & t
    #Time complexity: O(n)
    for i in range(len(t)):
        sCount[s[i]] = 1 + sCount.get(s[i], 0);
        tCount[t[i]] = 1 + tCount.get(t[i],0);
        
    #Comparing the two hashmaps for checking whether these two strings are valid anagrams
    #Time Complexity: O(n)
    for i in tCount:
        if( tCount[i] != sCount.get(i,-1)):
            return False
    return True

    #Time complexity O(n) + O(n) = O(n)
