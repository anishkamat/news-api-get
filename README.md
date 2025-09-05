# News API Python Script with Error Handling

A robust Python script that fetches and displays news articles based on user input using the NewsAPI, with comprehensive error handling and debugging features.

## Description

This improved news fetcher script allows users to search for news articles by entering a topic of interest. It includes proper error handling, response validation, and debugging information to ensure reliable operation.

## Features

- 🔍 Interactive user input for news topics
- 📰 Fetches articles from NewsAPI.org
- 🛡️ Comprehensive error handling for network issues
- 📊 Response status and result count display
- 🔗 Shows article titles, descriptions, and URLs
- 📅 Filters articles from August 5, 2025 onwards
- ⚡ Sorts articles by publication date
- 🐛 Built-in debugging information

## Requirements

- Python 3.x
- `requests` library
- `json` library (built-in)
- NewsAPI.org API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/improved-news-api-script.git
cd improved-news-api-script
```

2. Install required dependencies:
```bash
pip install requests
```

3. Get your free API key from [NewsAPI.org](https://newsapi.org/register)

4. Replace the API key in the script with your own key

## Usage

1. Run the script:
```bash
python main.py
```

2. When prompted, enter the type of news you're interested in (e.g., "technology", "sports", "politics", "climate change")

3. The script will display:
   - API response status
   - Total number of results found
   - Article details (title, description, URL)

## Example Output

```
What type of news are you interested in? technology
API Response status: ok
Total results: 847

Found 20 articles:

Title: Latest AI Breakthrough in Medical Research
Description: Scientists develop new AI system for early disease detection...
URL: https://example.com/ai-medical-breakthrough
--------------------------------------
Title: Quantum Computing Advances
Description: New quantum processor achieves unprecedented performance...
URL: https://example.com/quantum-computing-news
--------------------------------------
```

## Error Handling

The script handles various error scenarios:

### Network Errors
```
Request failed: HTTPSConnectionPool(host='newsapi.org', port=443): Max retries exceeded
```

### API Errors
```
API Response status: error
Error message: Your API key is invalid or incorrect.
```

### No Results
```
API Response status: ok
Total results: 0
No articles found or invalid response
```

## Code Structure

```python
import requests
import json

# User input
query = input("What type of news are you interested in? ")

# API configuration
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-05&sortBy=publishedAt&apiKey=YOUR_API_KEY"

# Error-handled API request
try:
    r = requests.get(url)
    r.raise_for_status()
    news = r.json()
    
    # Response validation and display
    # ... (error handling and article display logic)
    
except requests.exceptions.RequestException as e:
    # Network error handling
except json.JSONDecodeError as e:
    # JSON parsing error handling
except KeyError as e:
    # Missing data error handling
```

## API Configuration

- **Endpoint**: `https://newsapi.org/v2/everything`
- **Parameters**:
  - `q`: Search query (user input)
  - `from`: Start date (2025-08-05)
  - `sortBy`: Publication date (newest first)
  - `apiKey`: Your NewsAPI key

## Error Types Handled

| Error Type | Description | Solution |
|------------|-------------|----------|
| `RequestException` | Network connectivity issues | Check internet connection |
| `JSONDecodeError` | Invalid API response format | Check API endpoint and parameters |
| `KeyError` | Missing expected data fields | Verify API response structure |
| `HTTPError` | HTTP status errors (4xx, 5xx) | Check API key and request parameters |

## Security Considerations

⚠️ **Important**: This script contains an API key in plain text. For production use:

1. Use environment variables:
```python
import os
api_key = os.getenv('NEWS_API_KEY')
```

2. Create a `.env` file:
```
NEWS_API_KEY=your_api_key_here
```

3. Add `.env` to your `.gitignore` file

## Troubleshooting

### Common Issues

1. **"Invalid API Key" error**:
   - Verify your API key at [NewsAPI.org](https://newsapi.org/)
   - Check for typos in the key

2. **"No articles found"**:
   - Try different search terms
   - Check the date range (articles from 2025-08-05 onwards)

3. **Rate limiting**:
   - Free accounts have 1000 requests per day
   - Upgrade to paid plan for higher limits

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -am 'Add enhancement'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Create a Pull Request

## Future Improvements

- [ ] Add configuration file support
- [ ] Implement caching for repeated queries
- [ ] Add article content extraction
- [ ] Include sentiment analysis
- [ ] Add export functionality (CSV, JSON)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## API Reference

- [NewsAPI Documentation](https://newsapi.org/docs/endpoints/everything)
- [Get API Key](https://newsapi.org/register)
- [API Error Codes](https://newsapi.org/docs/errors)

## Author

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/improved-news-api-script](https://github.com/yourusername/improved-news-api-script)

---

**⭐ If you found this project helpful, please consider giving it a star!**
