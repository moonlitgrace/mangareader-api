from rest_framework import serializers

class PopularMangaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rank = serializers.CharField()
    title = serializers.CharField()
    slug = serializers.SlugField()
    cover = serializers.URLField()
    rating = serializers.FloatField()
    langs = serializers.JSONField()
    chapters = serializers.SerializerMethodField()
    volumes = serializers.SerializerMethodField()

    def get_chapters(self, obj):
        return {
        	"total": float(obj["chapters"]["total"]),
        	"lang": str(obj["chapters"]["lang"])
        }

    def get_volumes(self, obj):
        return {
        	"total": float(obj["volumes"]["total"]),
        	"lang": str(obj["volumes"]["lang"])
        }