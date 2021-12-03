from rest_framework import viewsets, serializers, routers

from main_app.models import Food, Order, FoodItem


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'image', 'name', 'ingredients', 'price']


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ['food', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        saved_food_items = []
        for food_item_data in validated_data['food_items']:
            food_item = FoodItem.objects.create(**food_item_data)
            saved_food_items.append(food_item)
        order = Order.objects.create()
        order.food_items.set(saved_food_items)
        return order

    food_items = FoodItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'food_items']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'orders', OrderViewSet)