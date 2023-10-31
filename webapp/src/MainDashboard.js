import React, { useState } from 'react';
import './MainDashboard.css';

function MainDashboard() {
  const [articleURL, setArticleURL] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: articleURL }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      setSentiment(result.data);
    } catch (error) {
      setSentiment('Error analyzing the article. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="main-dashboard">
      <h1>News Sentiment Dashboard</h1>
      <div className="news-url-form">
        <h2>Analyze News Article</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="url"
            value={articleURL}
            name="newsURL"
            onChange={(e) => setArticleURL(e.target.value)}
            placeholder="Enter news article URL"
            required
          />
          <button type="submit">{loading ? 'Loading...' : 'Analyze'}</button>
        </form>
        {sentiment && <div className="result">{sentiment}</div>}
      </div>
    </div>
  );
}

export default MainDashboard;
