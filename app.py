from flask import Flask,redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']
        print(email, password)
        if email == 'bua0409@gmail.com' and password == '123':
            return redirect('/homepage')
        else:
            print('login failed')
            return render_template('login.html')    
@app.route('/homepage')
def go_to_homepage():
    return render_template('homepage.html')
@app.route('/intell',methods=['GET','POST'])
def go_to_intell():
    if request.method == 'GET':
        return render_template('intell.html')
    elif request.method == 'POST':
        form = request.form
        ngonngu = form['ngonngu']

        logic=form['logic']

        khonggian=form['khonggian']

        vandong=form['vandong']

        amnhac=form['amnhac']

        giaotiep=form['giaotiep']

        noitam=form['noitam']

        thiennhien=form['thiennhien']
        print(ngonngu,logic,khonggian,vandong,amnhac,giaotiep,noitam,thiennhien)    
        return render_template('talk_about_types_of_intelligence.html')
@app.route('/ourteam')
def go_to_ourteam():
    return render_template('ourteam.html')
@app.route('/talk_about_types_of_intelligence')
def go_to_talk_about_types_of_intelligence():
    return render_template('talk_about_types_of_intelligence.html')
@app.route('/uni')
def go_to_uni():
    return render_template('uni.html')
if __name__ == '__main__':
    app.run()    

