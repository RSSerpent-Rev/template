from typing import Any

path = "/{{ cookiecutter.plugin.removeprefix('rsserpent-plugin-') }}"


async def provider() -> dict[str, Any]:
    """Define a basic example data provider function."""
    return {
        "title": "Example",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
