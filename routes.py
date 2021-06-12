from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Forbidden!'

@app.route('/save/<data>', methods = ['POST'])
def insert(data):
    f = open("data.txt", "a")
    f.write(data + "\n")
    f.close()
    return 'Data Saved Successfully!'
   
if __name__ == '__main__':
    app.run(host='0.0.0.0')