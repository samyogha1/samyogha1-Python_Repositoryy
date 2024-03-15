import requests

from src.main.lab import sample
from src.main.lab import lab
"""
This file will contain some sample code to send the output of the functions in lab.py to the 
console. You may modify this file in any way, it will not affect the test results.
"""
def main():
    print("Here's the present output of the provided sample API call to the LLM, in the sample() function.")
    result1 = sample()
    print(result1.json())
    print("Here the present output of your API call containing the 'hello world' response, in the lab() function")
    result2 = lab()
    if(type(result2)==requests.Response):
        if(result2.status_code==200):
            print(result2.json())
        else:
            print(f"the lab() function produced an error HTTP response: {result2.status_code}, {result2.content}")
    else:
        print("the lab() function did not produce an HTTP response.")


if __name__ == '__main__':
    main()
