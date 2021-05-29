def f23(lst):
    nlst = [['1' if r[0].split('!')[0] == 'Да' else '0',
             f"{r[2].split()[2]} {r[2].split()[0][:1]}.{r[2].split()[1]}",
             r[4].replace('/', '-'),
             f"{r[0].split('!')[1][:2]} {r[0].split('!')[1][2:5]} {r[0].split('!')[1][5:8]}-{r[0].split('!')[1][8:10]}-{r[0].split('!')[1][10:]}"]
            for r in lst]
    result = []
    for x in nlst:
        if x not in result:
            result.append(x)
    return result
