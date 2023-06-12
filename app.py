from flask import Flask, render_template, request
import spacy

app = Flask(__name__, static_folder='static')
nlp = spacy.load('en_core_web_trf')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def ner():
    input_text = request.form['text']
    doc = nlp(input_text)
    #print("/ner>>>",doc.ents)

    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    #print("after loop /ner",entities)

    return render_template('ner.html', text=input_text, entities=entities)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
