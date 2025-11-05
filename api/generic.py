from .client import tulip_client

def get_services():
    response = tulip_client.get("/services").raise_for_status()
    return response.json()

def get_tags():
    response = tulip_client.get("/tags").raise_for_status()
    return response.json()
