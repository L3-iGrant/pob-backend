from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import Tender
from django.http import JsonResponse


# Create your views here.
@permission_classes([permissions.IsAuthenticated])
@api_view(["GET","POST"])
def publish_tender(request, tender_id):
    if request.method == "POST":
        tender = get_object_or_404(Tender, pk=tender_id)
        tender.status = "PUBLISHED"
        tender.save()
        requirement_1 = tender.requirement_1
        requirement_2 = tender.requirement_2
        requirement = [{'id':requirement_1.id, "category": requirement_1.category,'requirement_header': requirement_1.requirement_header,'requirement_description': requirement_1.requirement_description,'requirement_category': requirement_1.requirement_category},
        {'id':requirement_2.id, "category": requirement_2.category,'requirement_header': requirement_2.requirement_header,'requirement_description': requirement_2.requirement_description,'requirement_category': requirement_2.requirement_category}]
        result = { "name": tender.name, "status":tender.status, "msg": "tender published","id": tender.id,"requirement":requirement}
        return JsonResponse(result)

    elif request.method == "GET":
        tender = get_object_or_404(Tender, pk=tender_id)
        requirement_1 = tender.requirement_1
        requirement_2 = tender.requirement_2
        requirement = [{'id':requirement_1.id, "category": requirement_1.category,'requirement_header': requirement_1.requirement_header,'requirement_description': requirement_1.requirement_description,'requirement_category': requirement_1.requirement_category},
        {'id':requirement_2.id, "category": requirement_2.category,'requirement_header': requirement_2.requirement_header,'requirement_description': requirement_2.requirement_description,'requirement_category': requirement_2.requirement_category}]
        result = { "name": tender.name, "status":tender.status,"id": tender.id,"requirement":requirement}
        return JsonResponse(result)

