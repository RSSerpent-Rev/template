from typing import Any
from rsserpent_rev.models import Feed

path = "/{{ cookiecutter.plugin.removeprefix('rsserpent-plugin-') }}"


async def provider() -> Feed:
    """Define a basic example data provider function."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
