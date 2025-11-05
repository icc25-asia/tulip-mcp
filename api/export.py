from .client import tulip_client


def export_to_pwntools(flow_id: str) -> str:
    response = tulip_client.get(f"/to_pwn/{flow_id}").raise_for_status()
    return response.text


def export_to_python_requests(flow_id: str) -> str:
    response = tulip_client.get(f"/to_python_request/{flow_id}").raise_for_status()
    return response.text
