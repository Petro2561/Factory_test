from api.serizlizers import (
    StoreSerializer,
    VisitCreateSerializer,
    VisitResponseSerializer,
)
from api.utils import get_store_by_id, get_worker_by_phone
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from visits.models import Store, Visit


class StoreList(ListAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.filter(worker=get_worker_by_phone(self))


class VisitCreate(CreateAPIView):
    serializer_class = VisitCreateSerializer
    queryset = Visit.objects.all()

    def create(self, request, *args, **kwargs):
        store_id = request.data.get("store")
        # get_store_by_id(self)
        if not Store.objects.filter(
            id=store_id, worker=get_worker_by_phone(self).id
        ).exists():
            return Response(
                {
                    "detail": "Переданный номер телефона работника не привязан к указанной торговой точке"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        visit = serializer.save()
        return Response(
            VisitResponseSerializer(visit).data, status=status.HTTP_201_CREATED
        )
