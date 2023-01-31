import flask, json, random
app = flask.Flask(__name__)

@app.route("/")
def main():
    return  f"""<!DOCTYPE html>
                <html>
                    <head>
                        <title>Random quote</title>
                    </head>
                    <body>
                        {random.choice(json.load(open("quotes.json")))}
                    </body>
                </html>
            """

if __name__ == "__main__":
    import waitress
    waitress.serve(app, host="0.0.0.0", port="8081")