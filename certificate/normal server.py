from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    str1 = '<table border=1 align=center>'
    for i in range(1, 11):
        str1 += "<tr>"
        for j in range(1, 11):
            str1 += f"<td> {i * j} </td>"
        str1 += "</tr>"
    str1 += "</table>"
    return "<h1 style='direction:ltr; text-align:center'><u> Multiplication table !  </u></h1>" + str1


if __name__ == "__main__":
    app.run(host='localhost', port=5000)