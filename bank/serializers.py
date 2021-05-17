from rest_framework import serializers 
from bank.models import Bank
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Bank
        fields = ('id',
                  'ifsc',
                  'bank_id',
                  'branch',
                  'address',
                  'city',
                  'district',
                  'state',
                  'bank_name')