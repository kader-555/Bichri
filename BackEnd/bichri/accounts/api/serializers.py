from rest_framework import serializers
from ..models import User,Rating
# from rest_framework.response import Response

class RatingSerializer(serializers.ModelSerializer):
    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all()
    )

    class Meta:
        model = Rating
        fields = '__all__'

    def validate(self, attrs):
        reviewer = attrs.get('reviewer_id',getattr(self.instance, 'reviewer_id',None))
        seller = attrs.get('seller_id',getattr(self.instance, 'seller_id',None))
        if reviewer is not None and reviewer == seller :
            raise serializers.ValidationError(
                {"seller_id": "لا يمكنك تقييم نفسك"}
            )
        
        return attrs

class UserSerializer(serializers.ModelSerializer):
    ratings_given = RatingSerializer(many = True,read_only = True)
    ratings_received = RatingSerializer(many = True,read_only = True)
    class Meta : 
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'whatsapp_number', 'date_joined', 'image','ratings_given','ratings_received']
