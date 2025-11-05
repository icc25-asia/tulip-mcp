import os
import httpx

tulip_client = httpx.Client(base_url=os.getenv("TULIP_API_BASE_URL", "http://localhost:3000/api"))
