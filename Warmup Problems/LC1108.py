class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = address.split(".")
        new_str = ''
        for i in range(len(temp)):
            if(i==len(temp)-1):
                new_str+=temp[i]
                return new_str
            new_str+=temp[i]+'[.]'
            