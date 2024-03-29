from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_cvs(data):
    with open('database.csv', newline='',mode='a') as database:
        email = data["email"]
        subject=data["subject"]
        message=data["message"] 
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])
        # Add a newline after writing each row
        # database.write('\n')

        

@app.route('/submit_form', methods=['POST', 'GET'])
def submint_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_cvs(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        print   ('something went wrong')

