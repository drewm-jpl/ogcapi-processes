# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from unity_sps_ogc_processes_api.apis.conformance_api_base import BaseConformanceApi
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
from unity_sps_ogc_processes_api.models.conf_classes import ConfClasses
from unity_sps_ogc_processes_api.models.exception import Exception


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/conformance",
    responses={
        200: {"model": ConfClasses, "description": "The URIs of all conformance classes supported by the server  To support \&quot;generic\&quot; clients that want to access multiple OGC API - Processes implementations - and not \&quot;just\&quot; a specific API / server, the server declares the conformance classes it implements and conforms to."},
        500: {"model": Exception, "description": "A server error occurred."},
    },
    tags=["ConformanceDeclaration"],
    summary="Retrieve the set of OGC API conformance classes that are supported by this service.",
    response_model_by_alias=True,
)
async def get_conformance() -> ConfClasses:
    ...
