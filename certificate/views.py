from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from pop_backend.settings import COMPANY_AGENT_URL, ISSUER_AGENT_URL
from igrant_user.models import IGrantUser
from rest_framework.response import Response
from rest_framework import status
from .models import Certificates
import requests


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def get_certificates(request):
    certificates = Certificates.objects.filter(user=request.user).all()
    return Response({
        'certificates': certificates,
    }, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def request_certificates(request):
    url = "https://cloudagent.igrant.io/v1/624c025d7eff6f000164bb94/admin/issue-credential/send-offer"
    authorization = "ApiKey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2MjRjMDFlNzdlZmY2ZjAwMDE2NGJiOTIiLCJvcmdpZCI6IiIsImV4cCI6MTY4MDI1Mjk0Mn0.g6gCu7Mr1DompSXK8kQYhBUqRJ1PsOtahhxmB-klV10"
    payload = {
        "comment": "Certificate of registration and register extract",
        "auto_remove": False,
        "trace": False,
        "cred_def_id": "GsMTo44BktRxUFjRVxR1nL:3:CL:3601:default",
        "connection_id": "60666c83-c8cd-46c0-bae1-82760c0e3cd9",
        "credential_preview": {
            "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/1.0/credential-preview",
            "attributes": [
                {
                    "name": "name",
                    "value": "Bygg AB"
                },
                {
                    "name": "legalForm",
                    "value": "Aktiebolag"
                },
                {
                    "name": "activity",
                    "value": "Construction Industry"
                },
                {
                    "name": "registrationDate",
                    "value": "2005-10-08"
                },
                {
                    "name": "legalStatus",
                    "value": "ACTIVE"
                },
                {
                    "name": "registeredAddress.fullAddress",
                    "value": "Sveavägen 48, 111 34 Stockholm, Sweden"
                },
                {
                    "name": "registeredAddress.thoroughFare",
                    "value": "Sveavägen"
                },
                {
                    "name": "registeredAddress.locatorDesignator",
                    "value": "48"
                },
                {
                    "name": "registeredAddress.postCode",
                    "value": "111 34"
                },
                {
                    "name": "registeredAddress.postName",
                    "value": "Stockholm"
                },
                {
                    "name": "registeredAddress.adminUnitLevel1",
                    "value": "SE"
                }
            ]
        },
        "auto_issue": True
    }
    response = requests.post(url,
                             headers={'Authorization': authorization, 'content-type': 'application/json;charset=UTF-8'},
                             json=payload)
    if response.status_code == 200:
        instance = Certificates.objects.create(user=request.user,
                                               credential_exchange_id=response.json().get('credential_exchange_id'))
        instance.save()
        return Response(response.json(), status=response.status_code)
    else:
        return Response(response.text, status=response.status_code)


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def check_certificate(request):
    credential_exchange_id = request.GET['credential_exchange_id']
    url = f"https://cloudagent.igrant.io/v1/624c025d7eff6f000164bb94/admin/issue-credential/records/{credential_exchange_id}"
    authorization = "ApiKey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI2MjRjMDFlNzdlZmY2ZjAwMDE2NGJiOTIiLCJvcmdpZCI6IiIsImV4cCI6MTY4MDI1Mjk0Mn0.g6gCu7Mr1DompSXK8kQYhBUqRJ1PsOtahhxmB-klV10"
    response = requests.get(url,
                            headers={'Authorization': authorization, 'content-type': 'application/json;charset=UTF-8'})
    print(response)
    return Response(response.json(), status=response.status_code)