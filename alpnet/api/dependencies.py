from functools import lru_cache

from alpnet.config.settings import Settings, get_settings
from alpnet.services.graph_service import GraphService
from alpnet.services.search_service import SearchService


@lru_cache()
def get_graph_service() -> GraphService:
    return GraphService(get_settings())


def get_search_service(settings: Settings = get_settings()) -> SearchService:
    return SearchService(settings)
