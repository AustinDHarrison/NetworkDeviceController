from flask import Flask, request, abort, render_template
import webhook_decoder
import ctypes
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/', methods=['POST'])
    
def webhook():
    
    if request.method == 'POST':
        print("Incoming Data", request.json)
        #Send the data to the decoder - formating - webhook_decoder.py
        webhook_decoder.formatIncData(request.json)
        return 'hey', 200
    else:
        abort(400)
    
@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html'), 405

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug= True)
    ctypes.windll.user32.MessageBoxW(0, "Flask Server.", "Server Closed Successfully", 0)
    

