import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8000/o/token/"
data = {
    "grant_type": "password",
    "username": "admin",
    "password": "1234"
}
auth = HTTPBasicAuth("5NdnsgzBlTYdEIAfPrDAINFFRE4GbpOoJXVLMW8i", "I2IySJvHBaVHahC6mpvkhF62aW9Nvb7jwRnSp8mMrbvfsWaBTff2uA1J1vGij8PwvcALdczkG3mOmnPxuXKHdVLHt6j8hUCUDXihlGHhVVoXKZWoHqfsK96paVDuFTTL")

response = requests.post(url, data=data, auth=auth)
print(response.json()) 