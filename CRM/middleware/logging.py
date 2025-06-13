class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(
            f"log: {request.method} - {request.path} - ip: {request.META['REMOTE_ADDR']} - user_id: {request.user.id} -> {response.status_code}"
        )

        return response
