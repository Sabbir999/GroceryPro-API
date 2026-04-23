import os

from django.contrib.admin.views.decorators import staff_member_required

from ninja import NinjaAPI
from ninja.errors import ValidationError
import sentry_sdk

#from warehousing.api import router as warehousing_router


async def api_key_auth(request):
    try:
        api_key = request.headers["X-API-KEY"]
        if api_key == os.environ.get("GATEWAY_API_KEY"):
            return True
        return False

    except KeyError:
        return False


api = NinjaAPI(
    docs_decorator=staff_member_required,
    openapi_extra={
        "info": {
            "title": "GroceryPro-API",
            "version": "1.0.0",
            "description": "GroceryPro-API is a backend service that provide real-time grocery prices,"
        },
    },
    title="GroceryPro API",
    description="Publishes Events for GroceryPro Azure Event Grid",
    auth=api_key_auth,
)


def validation_exception_handler(request, exc):
    sentry_sdk.capture_exception(exc)
    sentry_sdk.capture_message(
        "Request body: %s", request.body.decode("utf-8", errors="ignore")
    )
    return api.create_response(request, {"detail": exc.errors}, status=422)


api.add_exception_handler(ValidationError, validation_exception_handler)

#api.add_router("/warehousing/", warehousing_router, tags=["Warehousing"])