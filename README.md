# Google Search Program

This is a simple Python program that utilizes the Google Custom Search JSON API to perform searches on Google. The program allows users to input their search query and retrieves a list of search results.

## Prerequisites

Before running the program, you need to obtain an API key and a Search Engine ID from Google Custom Search JSON API. You can follow the instructions on the [Google Custom Search JSON API documentation](https://developers.google.com/custom-search/v1/overview) to obtain these credentials.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/google-search-program.git
    ```

2. Navigate to the project directory:

    ```bash
    cd google-search-program
    ```

3. Create a file named `API_KEY` and paste your Google Custom Search API key into it.
4. Create a file named `SEARCH_ENGINE_ID` and paste your Search Engine ID into it.

## Usage

Run the program by executing the following command in your terminal:

```bash
python search.py
```

Follow the on-screen prompts to input your search query. The program will then fetch the search results from Google and display the links.

## Example

```bash
What is your query? Artificial Intelligence
```

Output:

```
https://en.wikipedia.org/wiki/Artificial_intelligence
https://www.britannica.com/technology/artificial-intelligence
https://www.ibm.com/cloud/learn/what-is-artificial-intelligence
...
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to open an issue or create a pull request.

---

Feel free to customize the README file further to suit your preferences and provide any additional information you think would be helpful for users of your program.
