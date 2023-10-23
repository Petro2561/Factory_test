from rest_framework.exceptions import ValidationError
from visits.models import Store, Worker


def get_worker_by_phone(self):
    phone_number = self.kwargs.get("worker__phone_number")
    try:
        return Worker.objects.get(phone_number=phone_number)
    except Worker.DoesNotExist:
        raise ValidationError("Работника с таким номером не существует")
