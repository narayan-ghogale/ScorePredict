from flask import Flask,render_template,request
from linear_regression import lin,sc,np
from percent import lin2,sc2
from pycricbuzz import Cricbuzz
import json


app = Flask(__name__)


@app.route('/')
def abc():
    c = Cricbuzz()
    matches = c.matches()
    x=[]
    #print (json.dumps(matches,indent=4))
    for match in json.loads(json.dumps(matches)):
        #print(match)
        if match['type']=='ODI':
            #print(match)
            x.append(match)
    #print(json.dumps(x,indent=4))
    return render_template('index.html',odis=x)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      print(request.form)
      print(request.form['runs'])
      print(type(int(request.form['runs'])))
      r=int(request.form["runs"])
      w=int(request.form['wickets'])
      o=int(request.form['overs'])
      sr=int(request.form['sruns'])
      nr=int(request.form['nruns'])
      result2=lin.predict(sc.transform(np.array([[r,w,o,sr,nr]])))
      return render_template("result.html",result = result2)

@app.route('/insert')
def somefunc():
    return render_template('insert.html')   

@app.route('/insert2')
def somefunc2():
    return render_template('insert2.html') 

@app.route('/dashboard',methods=['POST',"GET"])
def dashboard():
    if(request.method=='POST'):
        print(request.form["id"])
        c = Cricbuzz()
        score1=c.livescore(request.form["id"])
        s=json.loads(json.dumps(score1))
        print(s)
        r=int(s['batting']['score'][0]['runs'])
        w=int(s['batting']['score'][0]['wickets'])
        o=int(float(s['batting']['score'][0]['overs']))
        sr=int(s['batting']['batsman'][0]['runs'])
        nr=int(s['batting']['batsman'][0]['runs'])
        r2=int(s['bowling']['score'][0]['runs'])
        result2=lin.predict(sc.transform(np.array([[r,w,o,sr,nr]])))
        print(result2[0])
        print(score1)
        if(r2<=r):
            percent=100
        else:
            percent=lin2.predict_proba(sc2.transform(np.array([[r,w,o,sr,nr,r2]])))

    return render_template('dashboard.html',scorecard=score1,result=int(result2[0]),percent=int(percent))

if __name__ == '__main__':
   app.run(debug = True)