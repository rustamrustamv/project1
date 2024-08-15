import requests
import json

def parse_swagger(url):
    response = requests.get(url)
    swagger_json = response.json()
    
    endpoints = []
    for path in swagger_json['paths']:
        endpoints.append(path)
    
    return endpoints

def main():
    swagger_url = "https://petstore.swagger.io/v2/swagger.json"
    endpoints = parse_swagger(swagger_url)
    
    print("Endpoints in the Swagger JSON:")
    for endpoint in endpoints:
        print(endpoint)

if __name__ == "__main__":
    main()
