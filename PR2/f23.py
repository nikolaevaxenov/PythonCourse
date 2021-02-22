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


r1 = f23([["Да!+78701307842", None, "Захар М. Мошли", None, "15/10/04"],
          ["Нет!+73818079627", None, "Павел Е. Чачман", None, "16/12/04"],
          ["Да!+78154289070", None, "Борис Г. Кибяк", None, "10/02/01"],
          ["Нет!+70616209982", None, "Семен И. Гекко", None, "28/03/04"],
          ["Нет!+70616209982", None, "Семен И. Гекко", None, "28/03/04"]])

r2 = f23([["Да!+73536474266", None, "Арсен З. Мемовли", None, "27/07/04"],
          ["Нет!+77134678251", None, "Василий Ц. Вацагий", None, "15/11/99"],
          ["Нет!+71204119690", None, "Арсен Д. Тошацли", None, "18/08/00"],
          ["Да!+73536474266", None, "Арсен З. Мемовли", None, "27/07/04"]])

for i in r1:
    print(i)

print("\n\n")

for i in r2:
    print(i)