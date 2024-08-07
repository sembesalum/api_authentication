import requests

url = "http://localhost:8000/o/token/"
data = {
    "grant_type": "refresh_token",
    "refresh_token": "GyVVgFhgZSgN5xGBYZbNYTusjX3HPN",
    "client_id": "5NdnsgzBlTYdEIAfPrDAINFFRE4GbpOoJXVLMW8i",
    "client_secret": "I2IySJvHBaVHahC6mpvkhF62aW9Nvb7jwRnSp8mMrbvfsWaBTff2uA1J1vGij8PwvcALdczkG3mOmnPxuXKHdVLHt6j8hUCUDXihlGHhVVoXKZWoHqfsK96paVDuFTTL"
}

response = requests.post(url, data=data)
print(response.json())
print(response.json())