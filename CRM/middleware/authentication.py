from django.shortcuts import redirect


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'login' in request.path:
            return self.get_response(request)

        if request.user.is_authenticated:
            return self.get_response(request)
        else:
            return redirect(f"users/login")

        return self.get_response(request)
