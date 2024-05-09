# coding: utf-8

"""
    OGC API - Processes

    Example API Definition for OGC API - Processes

    The version of the OpenAPI document: 0.1
    Contact: info@ogc.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GeoJSONMultiPolygon(BaseModel):
    """
    GeoJSONMultiPolygon
    """ # noqa: E501
    type: StrictStr
    coordinates: List[List[Annotated[List[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=2)]], Field(min_length=4)]]]
    bbox: Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=4)]] = None
    __properties: ClassVar[List[str]] = ["type", "coordinates", "bbox"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MultiPolygon'):
            raise ValueError("must be one of enum values ('MultiPolygon')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GeoJSONMultiPolygon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GeoJSONMultiPolygon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "coordinates": obj.get("coordinates"),
            "bbox": obj.get("bbox")
        })
        return _obj


