from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from pob_backend.settings import COMPANY_AGENT_URL, ISSUER_AGENT_URL
from igrant_user.models import IGrantUser
from rest_framework.response import Response
from rest_framework import status
from connections.models import Invitations
from django.views.decorators.csrf import csrf_exempt
from constance import config
import json
import base64

import requests


@csrf_exempt
@api_view(["GET"])
def get_default_wallet(request):
    organisation_id = config.BOLAGSVERKET_ORG_ID
    authorization = config.BOLAGSVERKET_API_KEY
    url = f"https://demo-api.igrant.io/v2/config/digital-wallet"
    response = requests.get(
        url,
        headers={
            "Authorization": authorization,
            "content-type": "application/json;charset=UTF-8",
        },
    )
    return Response(response.json(), status=response.status_code)


def get_endpoint(request):
    endpoint = ""
    if request.user.user_type == IGrantUser.UserType.COMPANY:
        endpoint = COMPANY_AGENT_URL
    else:
        endpoint = ISSUER_AGENT_URL
    print(endpoint)
    return endpoint


@csrf_exempt
@permission_classes([permissions.IsAuthenticated])
@api_view(["GET"])
def get_connections(request):
    url = "https://demo-api.igrant.io/v2/config/digital-wallet"
    authorization_header = config.BOLAGSVERKET_API_KEY
    response = requests.get(url, headers={"Authorization": authorization_header})
    return Response(response.json(), status=response.status_code)


@csrf_exempt
@permission_classes([permissions.IsAuthenticated])
@api_view(["POST"])
def accept_invitation(request):
    endpoint = get_endpoint(request)
    body = request.data
    print(body)
    connection_url = body.get("connection_url", None)
    if connection_url is not None:
        payload = {"connection_url": connection_url}
        response = requests.post(
            endpoint + "/v2/connections/receive-invitation?auto_accept=true",
            json=payload,
        )
        if response.status_code == status.HTTP_200_OK:
            connection = response.json()
            connection_id = connection.get("connection_id")
            connection_data = connection_url.split("c_i=")[-1]
            connection_data = str(base64.b64decode(connection_data))

            invitation, created = Invitations.objects.get_or_create(
                user=request.user, connection_id=connection_id
            )
            invitation.invitation_data = connection_data
            invitation.save()
            return Response(response.json(), status=response.status_code)
        else:
            return Response(response.content, status=response.status_code)
    else:
        return Response(" connection_url required", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@permission_classes([permissions.IsAuthenticated])
@api_view(["POST"])
def receive_invitation(request):
    organisation_id = config.PROCUREMENT_PORTAL_ORG_ID
    body = request.data
    connection_url = body.get("connection_url", None)
    if connection_url is not None:
        connection_data = connection_url.split("c_i=")[-1]
        connection_data = base64.b64decode(connection_data)
        connection_data = json.loads(connection_data)
        url = f"https://cloudagent.igrant.io/v1/{organisation_id}/admin/connections/receive-invitation?auto_accept=true"
        authorization_header = config.PROCUREMENT_PORTAL_API_KEY
        response = requests.post(url,json=connection_data, headers={"Authorization": authorization_header})
        response = json.loads(response.text)
        connection_id = response["connection_id"]
        connection_state = response["state"]
        user = request.user
        user.connection_id = connection_id
        user.connection_state = connection_state
        user.save()
        return Response(response)
    else:
        return Response(" connection_url required", status=status.HTTP_400_BAD_REQUEST)



@permission_classes([permissions.IsAuthenticated])
@api_view(["POST"])
def create_invitation(request):
    user = request.user
    organisation_id = config.BYGG_AB_ORG_ID
    url = f"https://cloudagent.igrant.io/v1/{organisation_id}/admin/v2/connections/create-invitation?multi_use=true"
    authorization_header = config.PROCUREMENT_PORTAL_API_KEY
    response = requests.post(url, headers={"Authorization": authorization_header})
    response = response.json()
    return Response(response)
    
    
        
