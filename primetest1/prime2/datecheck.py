def datetimevalidation(r):

    l=r.split('-')

    thirty =[4,6,9,11]
    thirtyone=[1,3,5,7,8,10,12]
    feb=[2]




    if len(l)!=3:
        return False

    if len(l)==1:
         return False
         

    if len(l)==3:

        if l[0].isnumeric():

            if l[1].isnumeric():   
                
                if int(l[1])in thirty:

                    if l[2].isnumeric():
                        if int(l[2])<31:
                            return True

                        else:
                            return False


                elif int(l[1])in thirtyone:

                    if l[2].isnumeric():
                        if int(l[2])<32:
                            return True
                        else:
                             return False

                elif int(l[1])in feb:

                    if l[2].isnumeric():    
                        if int(l[0])%4==0:
                            if int(l[2])<30:
                                return True

                            else:
                                 return False
                        if int(l[0])%4!=0:
                            if int(l[2])<29:
                                return True

                            else:
                                 return False
                    else:


                        return False


            else:
                return False
        else:
            return False


datetimevalidation('201-3-3')            

