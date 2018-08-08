from flask import Flask, render_template,request
from textblob import TextBlob
from wtforms import Form,StringField,TextAreaField,validators



app = Flask(__name__)

class homepageForm(Form):
    sentiments = TextAreaField('Text', render_kw={"rows": 5, "cols": 11})

@app.route('/',methods=['GET','POST'])
def index():
    formx = homepageForm(request.form)
    senti = ''
    pol = ''
    if request.method == 'POST':
        sen = formx.sentiments.data
        x = TextBlob(sen)
        pol = x.sentiment.polarity
        if pol < 0 :
            senti = 'Given sentence have negative polarity'
        else:
            senti = 'Given sentence have positive polarity'
        return render_template('home.html',form=formx,sent=senti,pol=pol)
    else:
        return render_template('home.html',form=formx,sent=senti,pol=pol)





if __name__ == '__main__':
    app.run(debug=True)
