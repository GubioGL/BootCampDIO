from flask import Flask, render_template
# import json

app = Flask(__name__)
# Template


@app.route('/')
def home_page():
    # Read file JSON
    data = {'Name': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
            'Age': [20, 25, 30, 35, 40],
            'City': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Florianópolis'],
            'Country': ['Brasil', 'Brasil', 'Brasil', 'Brasil', 'Brasil']
            }
    return render_template("home_page.html", data=data)


# Put the website in on
if __name__ == "__main__":
    app.run(debug=True)
