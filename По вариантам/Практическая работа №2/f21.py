def f21(x):
    if x[1] == 1995:
        return 13
    elif x[1] == 1985:
        if x[0] == 'yang':
            return 12
        elif x[0] == 'org':
            if x[2] == 1971:
                return 7
            elif x[2] == 1957:
                return 8
            elif x[2] == 1998:
                if x[3] == 'org':
                    return 9
                elif x[3] == 'raml':
                    return 10
                elif x[3] == 'eq':
                    return 11
        elif x[0] == 'txl':
            if x[4] == 1961:
                return 6
            elif x[4] == 2020:
                if x[2] == 1971:
                    return 3
                elif x[2] == 1957:
                    return 4
                elif x[2] == 1998:
                    return 5
            elif x[4] == 2014:
                if x[3] == 'org':
                    return 0
                elif x[3] == 'raml':
                    return 1
                elif x[3] == 'eq':
                    return 2
