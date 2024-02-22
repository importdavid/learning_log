"""Interact with local Ollama server using python requests library."""

import requests, json, sys

def ollama_chat(model="llama2", prompt="Write a poem about Atlas the cat."):
    """
    Returns response from local Ollama server in chat mode.
    Parameters defaults:
    model="llama2"
    prompt="Write a poem about Atlas the cat."
    """

    # Replace these with your actual server details
    host = "localhost"
    port = 11434
    api_path = "/api/chat"

    # Define the data
    data = {
        "model": model,
        "messages": [
            { "role": "user", "content": prompt }
        ]
    }

    # Create the URL
    url = f"http://{host}:{port}{api_path}"

    # Send the POST request
    response = requests.post(url, json=data)

    # Check for successful response
    if response.status_code == 200:
        # Process the response
        response_text = response.text

        # Convert each line to json
        response_lines = response_text.splitlines()
        response_json = [json.loads(line) for line in response_lines]
        for line in response_json:
            # Print the response. No line break
            print(line["message"]["content"], end="")
    else:
        print(f"Error: API request failed with status code {response.status_code}")
    print()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ollama_chat(prompt=sys.argv[1])
    else:
        ollama_chat()