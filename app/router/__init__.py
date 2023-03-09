"""
Root of API routers
"""
from fastapi import APIRouter, Response
from httpx import AsyncClient

router = APIRouter()


@router.get("/media")
async def request_proxy(url: str, method="get"):
    """
    CORS proxy
    """
    async with AsyncClient(http2=True) as client:
        resp = await client.request(method=method, url=url)
        return Response(resp.content, resp.status_code, resp.headers)
