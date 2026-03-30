from django.db import models


class Guest(models.Model):
    """
    Represents a guest entry in the system.

    Attributes:
        first_name (str): The guest's given name.
        last_name (str): The guest's family name.
        transport (str): The mode of transportation used by the guest.
        created_at (datetime): The timestamp when the record was created.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    transport = models.CharField(max_length=100, default="Unknown")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the Guest.

        Returns:
            str: The full name of the guest.
        """
        return f"{self.first_name} {self.last_name}"
