from ninja import NinjaAPI

api = NinjaAPI(
    title="API de Ejemplo",
    description="Esta es una API de ejemplo",
    version="1.0.0"
)

# http://127.0.0.1:8000/api/v1/examples
@api.get(path="examples/")
def get_examples(request):
    return { "id":1, "title":"Example" }