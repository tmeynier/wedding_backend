from rest_framework import serializers
from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    """
    Serializer for the Guest model.

    This serializer converts Guest model instances into JSON representations
    and validates incoming data to create or update Guest records.

    Attributes:
        Meta (class): Metadata options for the GuestSerializer.
    """

    class Meta:
        """
        Metadata for GuestSerializer.

        Attributes:
            model (Guest): The model class being serialized.
            fields (list): The list of fields to be included in the
                serialized output.
        """
        model = Guest
        fields = ['first_name', 'last_name', 'transport']
