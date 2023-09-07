from rest_framework.response import Response
from rest_framework.views import APIView
# scrapers
from .scrapers.popular import PopularScraper
from .scrapers.topten import TopTenScraper
from .scrapers.most_viewed import MostViewedScraper
from .scrapers.manga import MangaScraper
# serialzers
from .serializers.popular_manga import PopularMangaSerializer

class PopularMangasView(APIView):
	def get(self, request):
		response = PopularScraper().parse()
		serializer = PopularMangaSerializer(response, many=True)
		return Response(serializer.data)

class TopTenMangasView(APIView):
	def get(self, request):
		response = TopTenScraper().parse()
		return Response(response)

class MostViewedMangasView(APIView):
	def get(self, request, chart):
		response = MostViewedScraper().parse(chart)
		return Response(response)

class MangaView(APIView):
	def get(self, request, slug):
		response = MangaScraper(slug).parse()
		return Response(response)