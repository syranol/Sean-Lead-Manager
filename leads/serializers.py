from rest_framework import serializers
from leads.models import Lead

# Create serializers
# allows complex data such as query sets and model instances
# to be converted to native Python datatypes that can be then
# be easily rendered into JSON, XML or other type.


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        # Which means all, make sure to include __ on each side
