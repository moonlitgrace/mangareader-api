from rest_framework.response import Response
from rest_framework.views import APIView
# scrapers
from .scrapers.popular import PopularScraper

class PopularMangasView(APIView):
	def get(self, request):
		response = PopularScraper().parse()
		return Response(response)