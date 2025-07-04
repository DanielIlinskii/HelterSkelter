from django_user_agents.utils import get_user_agent


class TypeDeviceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            request.type_device = "mobile"
        elif user_agent.is_pc:
            request.type_device = "pc"
        elif user_agent.is_tablet:
            request.type_device = "tablet"

        response = self.get_response(request)

        return response
