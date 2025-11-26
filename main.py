from typing import Optional
from fastmcp import FastMCP

from api.generic import get_services, get_tags

mcp = FastMCP("Tulip")


@mcp.tool()
def list_services():
    """List available services in Tulip."""
    return get_services()


@mcp.tool()
def list_tags():
    """List available tags in Tulip."""
    return get_tags()


@mcp.tool()
def query_flows(
    service_name: Optional[str],
    regex: Optional[str] = None,
    tags_include: Optional[list[str]] = None,
    tags_exclude: Optional[list[str]] = None,
    cursor: Optional[str] = None,
):
    """
    List flows for a given service in Tulip.
    Optionally filter by regex and/or tags.
    """
    from api.flows import query_flows

    return query_flows(
        service_name,
        regex=regex,
        tags_include=tags_include,
        tags_exclude=tags_exclude,
        cursor=cursor,
    )


@mcp.tool()
def get_flow(flow_id: str):
    """Get flow details by flow ID in Tulip."""
    from api.flows import get_flow_by_id

    return get_flow_by_id(flow_id)


@mcp.tool()
def export_flow_to_pwntools(flow_id: str) -> str:
    """Export a flow to pwntools format."""
    from api.export import export_to_pwntools

    return export_to_pwntools(flow_id)


@mcp.tool()
def export_flow_to_python_requests(flow_id: str) -> str:
    """Export a flow to python-requests format."""
    from api.export import export_to_python_requests

    return export_to_python_requests(flow_id)


if __name__ == "__main__":
    import os

    mcp.run(transport="http", host=os.getenv("HOST", "0.0.0.0"))
