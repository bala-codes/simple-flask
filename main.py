from flask import Flask  
app = Flask(__name__)  

import routes.bala # When you have folders

@app.route('/')  
def main():
    return "Hello World" 

@app.route('/endpoint', methods=['GET', 'POST'])  
def func():
    return "Endpoint hit confirmed"   
  
if __name__ =="__main__":  
    app.run(port = 3000, debug = True)  