# TextInfoExtractor API

Welcome to the Word Info API, a service that provides information about words in a given text. This API analyzes the input text and returns various statistics, such as the number of words, the longest word, the smallest word, average word length, unique words, and word frequency.

## Technologies Used

- **Flask:** A lightweight web application framework for Python.
- **AWS Lambda:** Serverless computing platform for running the Word Info function.
- **AWS API Gateway:** Used to expose the Word Info function as an HTTP API.

## Base URL
The base URL for the API is:
https://2uxaqebw5j.execute-api.us-east-1.amazonaws.com/diverge/word-info/

## Endpoint
### POST /word-info ###
Analyze a text and retrieve word information.

#### Request ####
Method: POST.
URL: /word-info.
Content-Type: application/json.

**Request Body**
The request body should be a JSON object with a single field:
- **text** (string, required): The text to be analyzed.
  
Example:
{
  "text": "This is a sample text for analysis."
}


## Author
AJBAR ALAE
alae1ajbar@gmail.com
2024-02-03
