from __main__ import app

@app.route('/bala', methods=['GET'])
def bala():
    return 'Hitting from BALA'
