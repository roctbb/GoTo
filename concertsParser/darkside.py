import lxml.html as html

main_domain = 'http://www.darkside.ru/'
adress = "/show/index.phtml"

page = 0
result = {}
for page in range(0,8217,104):
    print("Now processing page "+str(page))
    page = html.parse(main_domain + adress+ '?cp=' + str(page))

    concerts = page.getroot().find_class('titleshow')

    for concert in concerts:
        name = concert.text_content()
        if name in result.keys():
            result[name]+=1
        else:
            result[name] = 1

    concerts = page.getroot().find_class('titles')
    for concert in concerts:
        name = concert.findall('.//a').pop().text_content()
        if name in result.keys():
            result[name] += 1
        else:
            result[name] = 1
count = []
for key in result.keys():
    count.append({"name": key, "concerts": result[key]})
count = sorted(count, key=lambda x: x["concerts"], reverse=True)
for concert in count:
    print(concert["name"]+" - "+str(concert["concerts"]))
