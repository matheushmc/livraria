from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Autor, Livro



class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1