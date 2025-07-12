from ninja import NinjaAPI, Schema
from .utils import generar_token, JWTAuth
from django.contrib.auth import authenticate

api = NinjaAPI(
    title="API de Ejemplo",
    description="Esta es una API de ejemplo",
    version="1.0.0"
)

auth = JWTAuth()

class AuthRequest(Schema):
    username: str
    password: str

@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return api.create_response(request, 
                                   {'response': 'Error de autenticación'},
                                   status=401)
    token = generar_token(user)
    return { "token": token }
    
@api.get(path="example1/", auth=auth, tags=["Private"])
def get_examples(request):
    return { "id":1, "title":"Example" }

@api.get(path="example2/", tags=["Public"])
def get_examples(request):
    return { "id":1, "title":"Example" }