from flask import Flask,render_template,request,jsonify
import re
import logging

app = Flask(__name__)


def match_exists(regex,message):
    try:
        pattern = re.compile(r'%s'%(regex))
        print(pattern)

        matches = pattern.findall(message)

        if len(matches)>0:
            return matches
        else:
            return "No match found"
    except re.error as e:
        return jsonify({"error":str(e)}), 400


@app.route("/",methods=['POST','GET'])
def regex_template():
    if request.method == "POST":
        data = request.json

        regex = data.get('pattern','')
        message = data.get('text','')
        matches = match_exists(regex,message)

        return jsonify({"matches":matches})
        
    return render_template('regex.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)