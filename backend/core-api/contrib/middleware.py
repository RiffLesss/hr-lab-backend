import json
import logging

from rest_framework import status as response_status
from rest_framework.utils import encoders


class LoggingMiddleware:
    MAX_LEN = 4000

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        try:
            self.log_request(request)
        except Exception as e:
            logging.exception(e)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        try:
            self.log_response(response)
        except Exception as e:
            logging.exception(e)

        return response

    @classmethod
    def log_request(cls, request):
        methods_with_data = ("POST", "PATCH", "PUT")

        multipart_content_type = "multipart/form-data"
        if multipart_content_type in request.META.get("CONTENT_TYPE", ""):
            logging.info("Multipart data.")
            return

        if request.method in methods_with_data:
            data = request.body
            logging.info("Request: {}".format(data))

    @classmethod
    def log_response(cls, response):
        data = getattr(response, "data", {}) or {}
        status = response.status_code

        if response_status.is_redirect(status):
            logging.warning("Redirect to {}".format(response.get("Location", "None")))

        data = json.dumps(data, cls=encoders.JSONEncoder, ensure_ascii=False, allow_nan=False)

        if response_status.is_success(status):
            logging.warning("Success. Data: {}".format(data))
        if response_status.is_client_error(status):
            logging.warning("Client error. Data: {}".format(data))
        if response_status.is_server_error(status):
            logging.warning("Server error. Data: {}".format(data))
