# TextInfoExtractor API

Welcome to the Word Info API, a service that provides information about words in a given text. This API analyzes the input text and returns various statistics, such as the number of words, the longest word, the smallest word, average word length, unique words, and word frequency.

## Technologies Used

- **Flask:** A lightweight web application framework for Python
- **AWS Lambda:** Serverless computing platform for running the Word Info function
- **AWS API Gateway:** Used to expose the Word Info function as an HTTP API

## Base URL
The base URL for the API is:
https://2uxaqebw5j.execute-api.us-east-1.amazonaws.com/diverge/

## Endpoint ##
### POST /word-info ###
Analyze a text and retrieve word information.

#### Request ####
- **Method:** POST
- **URL:** /word-info
- **Content-Type:** application/json

#### Request Body ####
The request body should be a JSON object with a single field:
- **text** (string, required): The text to be analyzed
  
Example:
```json
{
  "text": "This is a sample text for analysis."
}
```

#### Success Response ####
- **Status Code:** 200 OK
- **Content-Type:** application/json

The successful response includes information about the words in the text. For Example:
```json
{
  "num_words": 7,
  "longest_word": "analysis",
  "smallest_word": "a",
  "average_word_length": 6.142857142857143,
  "unique_words": ["this", "is", "a", "sample", "text", "for", "analysis"],
  "word_frequency": {
    "this": 1,
    "is": 1,
    "a": 1,
    "sample": 1,
    "text": 1,
    "for": 1,
    "analysis": 1
  }
}
```
#### Example Usage ####
**cURL**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a sample text for analysis."}' https://2uxaqebw5j.execute-api.us-east-1.amazonaws.com/diverge/word-info
```

**Python**
```python
import requests

url = "https://2uxaqebw5j.execute-api.us-east-1.amazonaws.com/diverge/word-info"
data = {"text": "This is a sample text for analysis."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

## Notes ##
- This API performs a basic analysis and may not handle all edge cases.
- Ensure that the input text is within the supported length limits.

## Conclusion ##
Thank you for using the TextInfoExtractor API! If you have any questions or issues, please contact alae1ajbar@gmail.com

## Author ##
AJBAR ALAE
alae1ajbar@gmail.com
2024-01-25
