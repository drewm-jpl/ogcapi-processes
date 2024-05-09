# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from unity_sps_ogc_processes_api.apis.landing_page_api_base import BaseLandingPageApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from unity_sps_ogc_processes_api.models.extra_models import TokenModel  # noqa: F401
from unity_sps_ogc_processes_api.models.exception import Exception
from unity_sps_ogc_processes_api.models.landing_page import LandingPage


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/",
    responses={
        200: {"model": LandingPage, "description": "The landing page provides links to the API definition (link relation &#x60;service-desc&#x60;, in this case path &#x60;/api&#x60;), to the Conformance declaration (path &#x60;/conformance&#x60;, link relation &#x60;http://www.opengis.net/def/rel/ogc/1.0/conformance&#x60;), and to other resources."},
        500: {"model": Exception, "description": "A server error occurred."},
    },
    tags=["Capabilities"],
    summary="Retrieve the OGC API landing page for this service.",
    response_model_by_alias=True,
)
async def get_landing_page() -> LandingPage:
    ...
