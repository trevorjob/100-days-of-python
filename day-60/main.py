from flask import Flask, render_template, request
import requests
import smtplib

my_email = 'redeks123456@gmail.com'
to_email = 'jobkumdan@gmail.com'
password = "mqwsczyzlmhtbltd"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Hello\n\nnamehhhhhhhhhh")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Hello\n\nname: {request['name']}\nemail: {request['email']}\nphone: {request['phone']}\nmessage {request['message']}")
            connection.close()
        return render_template("contact.html", data='MESSAGE SENT SUCCESFULLY')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route('/form-entry', methods=['POST'])
# def recieve():
#     return '<h1>message succesfull</h1>'
    

if __name__ == "__main__":
    app.run(debug=True, port=5001)
