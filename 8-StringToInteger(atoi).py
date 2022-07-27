class Solution(object):
    def myAtoi(self,s):
        x=[]    #shows digit index list from string
        spe=[]  #shows non-digit index list 
        sl=s.strip() #remove leading space
        if len(sl) == 0: res =0
        elif ((len(sl) != 1 and sl[0] == '-' and sl[1].isdigit()) 
        or (len(sl) != 1 and sl[0] =='+' and sl[1].isdigit()) 
        or (sl[0].isdigit())): #when first element is "+" or "-" or digit 
            sign = -1 if sl[0] == '-' else 1
            if sl[0] in ['-','+'] : sl=sl[1:]
            for i in xrange(len(sl)):
                if sl[i].isdigit():            
                    x.append([int(sl[i]),i])
                else:
                    spe.append([sl[i],i])
            res = (sign)*int(sl) if len(spe) == 0 else (sign)*int(sl[0:spe[0][1]]) 
        else:
            res = 0
        return max(-2**31, min(res,2**31-1))