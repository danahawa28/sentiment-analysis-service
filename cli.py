import requests

def predict(text):
    url = "http://localhost:8080/predict"
    response = requests.post(url, json={"text": text})
    print("Prediction:", response.json())

if __name__ == "__main__":
    user_input = input("Enter text: ")
    predict(user_input)