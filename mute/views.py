from django.contrib.auth.decorators import login_required

from rest_framework import views
from rest_framework.response import Response
from utils import *


@login_required
class ToggleView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.state.state:
            user.state.state = False
            user.state.save()
            send_state(False)
        else:
            user.state.state = True
            user.state.save()
            send_state(True)
        return Response({"success": False})
