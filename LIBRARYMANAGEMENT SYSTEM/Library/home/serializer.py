from rest_framework import serializers
from .models import AddBook

class AddBookSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    #bookid=serializers.CharField(max_length=10)
    #bookname=serializers.CharField(max_length=50)
    #subject=serializers.CharField(max_length=20)
    #category= serializers.CharField(max_length = 10)
    #product_name = serializers.CharField(max_length=200)
    #product_price = serializers.FloatField()
    #product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = AddBook
        fields = ('bookid','bookname','subject','category')