import requests
from langchain_tavily import TavilySearch
import os
import json

class TavilyPlaceSearchTool:
    def __init__(self):
        self._client = TavilySearch(topic="general", include_answer="advanced")

    def _search(self, query: str) -> dict:
        result = self._client.invoke({"query": query})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_attractions(self, place: str) -> dict:
        return self._search(f"top attractive places in and around {place}")

    def tavily_search_restaurants(self, place: str) -> dict:
        return self._search(f"what are the top 10 restaurants and eateries in and around {place}")

    def tavily_search_activity(self, place: str) -> dict:
        return self._search(f"activities in and around {place}")

    def tavily_search_transportation(self, place: str) -> dict:
        return self._search(f"What are the different modes of transportations available in {place}")

class FoursquarePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.foursquare.com/v3/places/search"
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}

    def foursquare_search_attractions(self, place: str) -> str:
        """
        Searches for attractions in the specified place using Foursquare API.
        """
        params = {"near": place, "query": "tourist attraction", "limit": 10}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            attractions = [r["name"] for r in results]
            return ", ".join(attractions) if attractions else "No attractions found."
        else:
            raise Exception(f"Foursquare API error: {response.status_code}")

    def foursquare_search_restaurants(self, place: str) -> str:
        """
        Searches for available restaurants in the specified place using Foursquare API.
        """
        params = {"near": place, "query": "restaurant", "limit": 10}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            restaurants = [r["name"] for r in results]
            return ", ".join(restaurants) if restaurants else "No restaurants found."
        else:
            raise Exception(f"Foursquare API error: {response.status_code}")

    def foursquare_search_activity(self, place: str) -> str:
        """
        Searches for popular activities in the specified place using Foursquare API.
        """
        params = {"near": place, "query": "activity", "limit": 10}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            activities = [r["name"] for r in results]
            return ", ".join(activities) if activities else "No activities found."
        else:
            raise Exception(f"Foursquare API error: {response.status_code}")

    def foursquare_search_transportation(self, place: str) -> str:
        """
        Searches for available modes of transportation in the specified place using Foursquare API.
        """
        params = {"near": place, "query": "transportation", "limit": 10}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            transportation = [r["name"] for r in results]
            return ", ".join(transportation) if transportation else "No transportation options found."
        else:
            raise Exception(f"Foursquare API error: {response.status_code}")

