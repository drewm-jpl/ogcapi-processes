# coding: utf-8

from fastapi.testclient import TestClient


from unity_sps_ogc_processes_api.models.exception import Exception  # noqa: F401
from unity_sps_ogc_processes_api.models.execute import Execute  # noqa: F401
from unity_sps_ogc_processes_api.models.execute200_response import Execute200Response  # noqa: F401
from unity_sps_ogc_processes_api.models.execute200_response1 import Execute200Response1  # noqa: F401
from unity_sps_ogc_processes_api.models.process import Process  # noqa: F401
from unity_sps_ogc_processes_api.models.process_list import ProcessList  # noqa: F401
from unity_sps_ogc_processes_api.models.processes_list import ProcessesList  # noqa: F401
from unity_sps_ogc_processes_api.models.status_info import StatusInfo  # noqa: F401


def test_execute(client: TestClient):
    """Test case for execute

    execute a process.
    """
    execute = unity_sps_ogc_processes_api.Execute()

    headers = {
        "prefer": 'prefer_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/processes/{processId}/execution".format(processId=unity_sps_ogc_processes_api.ProcessesList()),
    #    headers=headers,
    #    json=execute,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_process_description(client: TestClient):
    """Test case for get_process_description

    retrieve a process description
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/processes/{processId}".format(processId=unity_sps_ogc_processes_api.ProcessesList()),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_processes(client: TestClient):
    """Test case for get_processes

    retrieve the list of available processes
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/processes",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

