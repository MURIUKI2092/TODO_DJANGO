from rest_framework import serializers
from authentication.models import User
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta():
        password = serializers.CharField(max_length =128,write_only =True)
        model=User
        fields =('username','email','password')
        
    def create_new_user(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user