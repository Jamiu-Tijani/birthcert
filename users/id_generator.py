import datetime as date


def get_id():   
    try:
        now = str(date.datetime.now())
        split = now.split() 
        done = [] 
        for x in split: #remove punctuations from the content of the list 
            if '-' in x:
                done.append(str(x).split('-'))
            else:
                done.append(x.split(':'))

        needed = done[1]+ [done[0][2]] # concatenate the needed id
        id = int(float(''.join(needed).replace('.','')))
        return id

    except Exception as e:

        return e