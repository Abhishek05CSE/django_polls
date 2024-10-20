# class LogRequestMiddleware:

class CustomHeaderMiddleware:
    def __init__(self,get_response):
        print('CustomHeader __init__')
        self.get_response= get_response
    
    def __call__(self,request):
        print('CustomHeader __call__')
        response = self.get_response(request)
        response['X-Custom-Header'] = 'My Custom Value'
        return response
