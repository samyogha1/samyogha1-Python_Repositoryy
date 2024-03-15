"""
This module contains an example for how to send a API call to an LLM, as well
as a function at the bottom of the file marked TODO, where you will send a request to the
API yourself. It should be very similar to the provided example.
"""
import os
import requests

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
version = os.environ['OPENAI_API_VERSION']
"""
This function sends an HTTP request to an LLM which will prompt it for some
generic response. The function will return the response JSON. The URL used here has
been hidden via environment variables, but the general pattern is constructed as a POST to the following URL:
https://RESOURCE.openai.azure.com/openai/deployments/NAME/chat/completions?api-version=YEAR-MONTH-DAY

Let's also take a look at what else is provided here.
    - standard HTTP POST request, which sends a JSON body. We should receive a JSON body in the response.
    - an api key for accessing the provided URL is set in the header
    - the request body will contain an array of 'messages', which each identify if
        a piece of text originated from a human ('user') or the LLM's initial setup ('system'),
        or the LLM during conversation ('assistant')
    - the response body, apart from metadata for the chat message, contains the
        LLM's response under a 'content' field, which you can see by running the full script from
        app.py.
        
An API call to any other LLM may be slightly different.
"""
def sample() :
    res = requests.post(f"{base_url}/chat/completions?api-version={version}",
                        headers={
                            "Content-Type": "application/json",
                            "api-key": f"{api_key}"
                        },
                        json={
                            "messages": [
                                {"role": "system",
                                 "content":"The LLM recieves an array of message objects, containing the message's "
                                           "chat content and the actor who sent it."},
                                {"role": "user",
                                 "content":"Content from 'user' are effectively the prompts sent by the human."}],
                        })
    return res


"""
TODO: Within this function, send a request using the same URL & API key as above
where the user prompts the LLM to produce a hello world response, and return the resulting response. 
Test cases will verify that the LLM has actually produced some text containing "hello world".
"""
def lab() :
    return "todo"
