import pytest
from app.services.crawler_service import crawl_url

@pytest.mark.asyncio
async def test_crawl_example():
    data = await crawl_url("https://example.com")

    assert "title" in data
    assert "h1_count" in data
    assert "images_missing_alt" in data
