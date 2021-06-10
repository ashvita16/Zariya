from flask import Flask, request, render_template,jsonify
import audtoges
import textaud
import recognise
app = Flask(__name__)

#Flask(source code) is a Python web framework built with small core other framewrk Django
#it is web application framework written in python provides useful tools and features

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/Entertainment.html')
#def entertainment():
    #return render_template('Entertainment.html')

@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

@app.route('/instructions.html')
def instructions():
    return render_template('instructions.html')    

@app.route('/see', methods=['GET','POST'])
def see():
    text1 = request.form['text1']
    combine = audtoges.ges(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
    
   
@app.route('/listen', methods=['GET','POST'])
def listen():
    combine = audtoges.func()
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/camera', methods=['GET','POST'])
def camera():
    combine = recognise.Video()
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

# audio fxn for p1
@app.route('/audio', methods=['GET','POST'])
def audio():
    text2 = request.form['text2']
    combine = textaud.audio_feature(text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
   
    







if __name__ == '__main__':
    app.run(debug=True)

