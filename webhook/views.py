from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from igrant_user.models import IGrantUser
from buyer.models import Tender, Requirement
from seller.models import Responses
from constance import config
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
@require_POST
def receive_invitation(request):
    
    response = request.body
    response = json.loads(response)
    connection_id = response["data"]["connection"]["connectionId"]
    connection_state = response["data"]["connection"]["state"]
    user = get_object_or_404(IGrantUser,connection_id = connection_id)
    if user.connection_state == "active":
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        user.connection_state = connection_state
        user.save()
        return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
@require_POST
def verify_certificate(request):
    response = request.body
    response = json.loads(response)
    presentation_exchange_id = response["data"]["presentation"]["presentationExchangeId"]
    presentation_state = response["data"]["presentation"]["state"]
    presentation_record = response["data"]["presentation"]
    try:
        user = IGrantUser.objects.get(presentation_exchange_id = presentation_exchange_id)
    except IGrantUser.DoesNotExist:
        user = None
    if not user:
        try:
            responses = Responses.objects.get(presentation_exchange_id = presentation_exchange_id)
        except Responses.DoesNotExist:
            responses = None
        if responses:
            if responses.presentation_state != "verified":
                responses.presentation_state = presentation_state
                responses.presentation_record = presentation_record
                responses.save()
    if user:
        if user.presentation_state != "verified":
            user.presentation_state = presentation_state
            user.presentation_record = presentation_record
            user.save()
            if presentation_state == "verified":
                user.org_verification_status = "VERIFIED"
                user.save()
                if user.user_type == "SELLER":
                    tender = Tender.objects.first()
                    if tender:
                        requirements = Requirement.objects.filter(tender_id=tender.id)
                        data_agreement_id = config.USER_VERIFICATION_DATA_AGREEMENT_ID
                        for requirement in requirements:
                            if requirement.data_agreement_id == data_agreement_id:
                                (responses, _) = Responses.objects.get_or_create(tender=tender,requirements=requirement,supplier=user)
                                responses.presentation_exchange_id = presentation_exchange_id
                                responses.presentation_state = presentation_state
                                responses.presentation_record = presentation_record
                                responses.save()
    return HttpResponse(status=status.HTTP_200_OK)
