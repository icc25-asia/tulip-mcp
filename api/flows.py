from typing import Optional

from .client import tulip_client
from .generic import get_services

def query_flows(
        service_name: Optional[str] = None,
        regex: Optional[str] = None,
        tags_include: Optional[list[str]] = None,
        tags_exclude: Optional[list[str]] = None
):
    service = None
    if service_name:
        services = get_services()
        for s in services:
            if s["name"] == service_name:
                service = s
                break

    query = {}
    if tags_include is not None or tags_exclude is not None:
        query["tags_include"] = tags_include or []
        query["tags_exclude"] = tags_exclude or []
        query['tag_intersection_mode'] = "OR"
    if regex is not None:
        query["regex_insensitive"] = regex
    if service is not None:
        query['ip_dst'] = service['ip']
        query['port_dst'] = service['port']
    if len(query) == 0:
        query = None
    response = tulip_client.post('/query', json=query).raise_for_status()
    return response.json()

def get_flow_by_id(flow_id: str):
    response = tulip_client.get(f"/flow/{flow_id}").raise_for_status()
    return response.json()
