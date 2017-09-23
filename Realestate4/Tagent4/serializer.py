from rest_framework import serializers
from . models import *
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields =['agent_id','first_name', 'last_name', 'age', 'education', 'company_name', 'specialization','agent_notes',
              'mobile_number','phone_number','email_id','media_name','media_path','property_type']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ="__all__"
class AgentReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentReferal
        fields ="__all__"
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields ="__all__"
class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields ="__all__"