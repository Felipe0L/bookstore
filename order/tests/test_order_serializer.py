import pytest
from order.serializers import OrderSerializer
from order.factories import OrderFactory, ProductFactory

@pytest.mark.django_db
def test_order_serializer_serialization():
    # Cria produtos
    product1 = ProductFactory(price=100)
    product2 = ProductFactory(price=200)

    # Cria pedido com produtos
    order = OrderFactory(product=[product1, product2])

    # Serializa
    serializer = OrderSerializer(order)
    data = serializer.data

    # Verifica os campos serializados
    assert "product" in data
    assert len(data["product"]) == 2
    assert data["total"] == 300
