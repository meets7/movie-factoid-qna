from flask import Flask, render_template, request, jsonify
import qna
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/getInfo/", methods=['POST'])
def getInfo():
    query = request.args.get('query')
    answer, link = qna.getAnswer(query)
    d = {
        'query': query,
        'answer': answer,
        'link': link
    }
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
