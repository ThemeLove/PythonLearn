from django.http import HttpResponse
import logging

class myMiddleWare:

    def __init__(self):
        logging.info("myMiddleWare----->init")

    def process_request(self, request):
        logging.info("myMiddleWare----->process_request")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        logging.info("myMiddleWare----->process_view")

    def process_response(self, request, response):
        logging.info("myMiddleWare----->process_response")

    def process_exception(self, request, exception):
        logging.info("myMiddleWare----->process_exception")
        return HttpResponse("exception")
