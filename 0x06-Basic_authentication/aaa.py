#!/usr/bin/python3
""" Check response
"""
import requests

if __name__ == "__main__":
    r = requests.get('http://0.0.0.0:3456/api/v1/unauthorized/')
    if r.status_code != 401:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    if r.headers.get('content-type') != "application/json":
        print("Wrong content type: {}".format(r.headers.get('content-type')))
        exit(1)
    
    try:
        r_json = r.json()
        
        if len(r_json.keys()) != 1:
            print("Not the right number of element in the JSON: {}".format(r_json))
            exit(1)
        
        status_value = r_json.get('error')
        if status_value is None:
            print("Missing 'error' key in the JSON: {}".format(r_json))
            exit(1)
        if status_value != "Unauthorized":
            print("'error' doesn't have the right value: {}".format(status_value))
            exit(1)
            
        print("OK", end="")
    except:
        print("Error, not a JSON")
