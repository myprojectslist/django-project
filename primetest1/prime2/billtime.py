def timevalidater(r):
    l=r.split(':')
    print(l)

    if len(l)==2:
        if l[0].isnumeric() and l[1].isnumeric(): 
            if int(l[0])<24 and int(l[1])<61:
                return True
            else:

                return False

        else:
            return False
            
    else:
        return False 
     
