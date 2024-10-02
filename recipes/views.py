from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from opensearchpy import OpenSearch

class RecipeSearchView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = OpenSearch(
            hosts=[{'host': 'localhost', 'port': 9200}],
            http_auth=('admin', 'admin')
        )
        self.index_name = 'epirecipes'

    def get(self, request):
        search_query = request.query_params.get('query', None)
        fields = request.query_params.getlist('fields', None)  

        if not search_query:
            return Response({"error": "No search query provided."}, status=status.HTTP_400_BAD_REQUEST)

        search_body = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"title": search_query}},
                        {"match": {"tags": search_query}}
                    ]
                }
            }
        }

        try:
            response = self.client.search(index=self.index_name, body=search_body)
            results = response['hits']['hits']

            recipes = []
            for hit in results:
                recipe_data = hit["_source"]

                recipe_response = {
                    "title": recipe_data.get("title"),
                    "id": hit["_id"]
                }

                if fields:
                    for field in fields:
                        if field in recipe_data and field != 'title': 
                            recipe_response[field] = recipe_data[field]
                else:
                    recipe_response.update({k: v for k, v in recipe_data.items() if k != 'title'})
                
                recipes.append(recipe_response)

            return Response(recipes, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



