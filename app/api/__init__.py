import json
import re
from datetime import datetime

from flask import Response
from flask.wrappers import Request


class CustomResponse(Response):  # pylint: disable=too-many-ancestors
    """
        This class wraps FlasK/Werkzeug Response to handle Json
    """

    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, (dict, list)):
            rv = Response(
                json.dumps(cls._format_response(rv)), content_type="application/json"
            )
        return super(CustomResponse, cls).force_type(rv, environ)

    @classmethod
    def _format_response(cls, obj):
        """
            Convert a snake_cased obj to a camelCase one
            :param obj obj: The obj to convert
            :rtype: obj
            :returns: the converted obj
        """
        if isinstance(obj, dict):
            new_dict = {}

            for key, value in obj.items():
                if isinstance(value, dict):
                    value = cls._format_response(value)

                elif isinstance(value, list):
                    value = [cls._format_response(i) for i in value]

                elif isinstance(value, datetime):
                    value = value.strftime("%Y-%m-%dT%H:%M:%SZ")

                new_key_name = cls._to_camel_case(key)
                new_dict[new_key_name] = value

            return new_dict

        if isinstance(obj, list):
            return [cls._format_response(i) for i in obj]

        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%SZ")

        return obj

    @classmethod
    def _to_camel_case(cls, string):
        """Give the camelCase representation of a snake_case string."""
        return re.sub(r"_(\w)", lambda x: x.group(1).upper(), string)


class ExtendedRequest(Request):
    @property
    def json(self):
        return self.get_json(force=True)
