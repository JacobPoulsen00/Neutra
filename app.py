from webapp.routes import app
import webbrowser

def analyze():
    url = request.form['news_url']
    try:
        # Fetch and preprocess the article
        article_text = fetch_with_retries(url)
        preprocessed_text = preprocess_text(article_text)
        
        # Predict sentiment
        sentiment = predict_sentiment(preprocessed_text)

        # Send result to the user
        flash(f"Sentiment of the article: {sentiment}", "success")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")

    return redirect(url_for('index'))


if __name__ == "__main__":
    # Open the default web browser and navigate to the Flask app URL
    webbrowser.open("http://127.0.0.1:5000/", new=2)  # new=2 means open in a new tab, if possible
    app.run(debug=True)