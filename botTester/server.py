__author__ = 'roctbb'
import tornado.web
import tornado.httpserver
import sqlite3
import sys
import os

fight_iterations = 1001

def makeFight(file1, file2):
        #if file1!="6B63h" or file2!="SIL5E":
        #    return "error"
    try:

        func1 = getattr(__import__(file1, fromlist=["step"]), "step")
        #print(dir(__import__(file1)))
        func2 = getattr(__import__(file2, fromlist=["step"]), "step")
        history1 = []
        history2 = []
        table = [0,0,0]
        for game in range(fight_iterations):
            try:
                choice1 = func1(history1)
            except:
                print("error in "+file1)
                return "error"
            try:
                choice2 = func2(history2)
            except:
                print("error in "+file2)
                return "error"

            history1.append([choice2, choice1])
            history2.append([choice1, choice2])
            if choice1==choice2:
                table[2]+=1
            else:
                if choice1 == "камень":
                    if choice2 == "бумага":
                        table[1]+=1
                    elif choice2 == "ножницы":
                        table[0]+=1
                    else:
                        return "error"
                elif choice1 == "бумага":
                    if choice2 == "ножницы":
                        table[1]+=1
                    elif choice2 == "камень":
                        table[0]+=1
                    else:
                        return "error"
                elif choice1 == "ножницы":
                    if choice2 == "камень":
                        table[1]+=1
                    elif choice2 == "бумага":
                        table[0]+=1
                    else:
                        return "error"
                else:
                    return "error"
        return table
    except:
        return "error"

def tryAdd(dictionary,key1,key2):
    try:
        dictionary[key1][key2]+=1
        return dictionary
    except:
        dictionary[key1]=dict()
        dictionary[key1]["wins"]=0
        dictionary[key1]["fails"]=0
        dictionary[key1]["draws"]=0
        dictionary[key1][key2]=1
        return dictionary



def makeFullTest():
    conn = sqlite3.connect('botTester.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM results")
    c.execute("DELETE FROM history")
    c.execute("SELECT * FROM players")
    players = c.fetchall()
    results = dict()
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            win = 0
            draw = 0
            fail = 0
            error_flag = False
            player1 = players[i]
            player2 = players[j]
            result = makeFight(player1[1], player2[1])
            if result=='error':
                continue
            win += result[0]
            fail += result[1]
            draw += result[2]
            print(player1[1]+" vs "+player2[1]+" success testing")
            c.execute('INSERT INTO history ("key1","key2","wins","draws","fails") VALUES ("'+
                      player1[1]+'","'+player2[1]+'",'+str(win)+','+str(draw)+','+str(fail)+')')
            c.execute('INSERT INTO history ("key1","key2","wins","draws","fails") VALUES ("'+
                      player2[1]+'","'+player1[1]+'",'+str(fail)+','+str(draw)+','+str(win)+')')
            if win == fail:
                results=tryAdd(results,i,"draws")
                results=tryAdd(results,j,"draws")
            if win>fail:
                results=tryAdd(results,i,"wins")
                results=tryAdd(results,j,"fails")
            if win<fail:
                results=tryAdd(results,j,"wins")
                results=tryAdd(results,i,"fails")
    for i in range(len(players)):
        try:
            total = results[i]["wins"]*3+results[i]["draws"]
            c.execute('INSERT INTO results ("key","wins","draws","fails","total") VALUES ("'+players[i][1]+'",'+str(results[i]['wins'])
                  +','+str(results[i]['draws'])+','+str(results[i]['fails'])+', '+str(total)+')')
        except:
            continue
    conn.commit()






class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html")
    def post(self):
        '''
        try:
            file = self.request.files['file'][0]
            conn = sqlite3.connect('botTester.sqlite')
            c = conn.cursor()
            c.execute("SELECT * FROM players WHERE key = '%s'"%self.get_argument("key"))
            player = c.fetchone()
            output_file = open("./bots/" + player[1]+".py", 'wb')
            output_file.write(file['body'])
            output_file.close()
            self.redirect("/results")
        except:
            self.write("<script>alert('Ошибка загрузки!');location.href=location.href;</script>")

        sys.path.append(os.path.dirname(__file__) + "/bots")
        makeFullTest()
        '''
        if self.get_argument("key")=="masterkey":
            sys.path.append(os.path.dirname(__file__) + "/bots")
            makeFullTest()
            self.redirect("/results")

class ResultsHandler(tornado.web.RequestHandler):
    def get(self):
        conn = sqlite3.connect('botTester.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM results ORDER BY total DESC")
        results = c.fetchall()
        table = '<html><head>' \
                '<!-- Latest compiled and minified CSS -->' \
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">' \
                '<!-- Optional theme -->' \
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">' \
                '<!-- Latest compiled and minified JavaScript -->' \
                '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>' \
                '</head><body><table class="table table-striped">'
        table+="<tr><th>#</th><th>Автор</th><th>Бот</th><th>Побед</th><th>Ничьи</th><th>Поражение</th><th>Очков</th></tr>"
        i=1
        for result in results:
            c.execute("SELECT * FROM players WHERE key = '"+result[1]+"'")
            try:
                botname = getattr(__import__(result[1], fromlist=["name"]), "name")
            except:
                botname = "Безымянный Петрович"
            name = c.fetchone()
            cclass=''
            if i<4:
                cclass="success"
            table+="<tr class='"+cclass+"'><td>"+str(i)+"</td><td>"+name[2]+"</td><td><a href='/history?key="+result[1]+"'>"+botname+"</a></td>" \
                                                         "<td>"+str(result[2])\
                   +"</td><td>"+str(result[3])\
                   +"</td><td>"+str(result[4])\
                   +"</td><td>"+str(result[5])+"</td></tr>"
            i+=1
        table+="</table></body>"
        self.write(table)


class HistoryHandler(tornado.web.RequestHandler):
    def get(self):
        bot = self.get_argument("key")
        conn = sqlite3.connect('botTester.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM history WHERE key1 = '"+bot+"'")
        results = c.fetchall()
        c.execute("SELECT * FROM players WHERE key = '"+bot+"'")
        mainname = c.fetchone()

        table = '<html><head>' \
                '<!-- Latest compiled and minified CSS -->' \
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">' \
                '<!-- Optional theme -->' \
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">' \
                '<!-- Latest compiled and minified JavaScript -->' \
                '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>' \
                '</head><body><h1>'+mainname[2]+'</h1><table class="table table-striped">'
        table+="<tr><th>#</th><th>Соперник</th><th>Побед</th><th>Ничьи</th><th>Поражение</th><th>Итог</th></tr>"
        i=1
        for result in results:
            c.execute("SELECT * FROM players WHERE key = '"+result[2]+"'")
            name = c.fetchone()
            table+="<tr><td>"+str(i)+"</td><td>"+name[2]+"</td>" \
                                                         "<td>"+str(result[3])\
                   +"</td><td>"+str(result[4])\
                   +"</td><td>"+str(result[5])\
                   +"</td>"
            if result[3]>result[5]:
                table+='<td><span class="label label-success">Победа</span></td>'
            if result[5]>result[3]:
                table+='<td><span class="label label-danger">Поражение</span></td>'
            if result[5]==result[3]:
                table+='<td><span class="label label-info">Ничья</span></td>'
            table+="</tr>"
            i+=1
        table+="</table><h3><a href='/results'>Турнирная таблица</a></h3></body>"
        self.write(table)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler),(r"/results", ResultsHandler),(r"/history", HistoryHandler)]
        settings = {"static_path": os.path.dirname(__file__)+"/bootstrap/"}
        super(Application, self).__init__(handlers, **settings)

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()