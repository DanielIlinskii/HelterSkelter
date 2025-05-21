class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        status_code = self.get_response(request).status_code
        print(
            f"log: {request.method} - {request.path} - ip: {request.META['REMOTE_ADDR']} - user_id: {request.user.id} -> {status_code}"
        )
        response = self.get_response(request)
        return response
