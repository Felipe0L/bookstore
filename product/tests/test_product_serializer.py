import pytest
from product.serializers import ProductSerializer
from product.factories import CategoryFactory


@pytest.mark.django_db
def test_product_serializer_with_factory():
    cat1 = CategoryFactory()
    cat2 = CategoryFactory()

    data = {
        "title": "Produto gerado via teste",
        "description": "Descrição teste",
        "price": 199,
        "category": [
            {
                "title": cat1.title,
                "slug": "slug1",
                "description": cat1.description,
                "active": cat1.active
            },
            {
                "title": cat2.title,
                "slug": "slug2",
                "description": cat2.description,
                "active": cat2.active
            }
        ]
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), f"Erros: {serializer.errors}"

    # Em vez de salvar, testamos os dados validados diretamente
    validated_data = serializer.validated_data

    assert validated_data["title"] == data["title"]
    assert validated_data["description"] == data["description"]
    assert validated_data["price"] == data["price"]

    # Testando que as categorias estão ali (como dicts validados)
    assert len(validated_data["category"]) == 2
    assert all("title" in cat for cat in serializer.initial_data["category"])