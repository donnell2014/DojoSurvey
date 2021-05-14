from flask import Flask, request
from flask import render_template
app=Flask(__name__)



@app.route('/')
def form():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])
def create_user():
    print(request.form)
    name_from_form = request.form['name']
    dojo_from_form = request.form['dojo']
    food_from_form = request.form['food']
    comment_from_form = request.form['comment']
    return render_template("post.html", name_on_template=name_from_form, dojo_on_template=dojo_from_form, food_on_template=food_from_form, comment_on_template=comment_from_form)
    # return render_template("post.html")










if __name__=="__main__":
    app.run(debug=True)