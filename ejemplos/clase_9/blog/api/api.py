from ninja import NinjaAPI, Path, Query
from django.http import Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Post
from .schemas import PostSchema

# Crea la API
app = NinjaAPI(
    title="API para el Blog",
    description="Aquí están todos los servicios que debe consumir la aplicacipón Blog",
    version="1.0.0"
)

# Manejadores de Errores
@app.exception_handler(Http404)
def error_404(request, ex):
    return app.create_response(request, 
                               {'response': 'No encontré nah'},
                               status=404)
    
@app.exception_handler(ValidationError)
def error_validacion(request, ex):
    return app.create_response(request,
                               {
                                   'response': 'Error de Formato de Entrada',
                                   'errores': ex.errors()
                               },
                               status=422)

# Servicios de la app
@app.get(path="posts/",
         summary="Lista de Artículos",
         description="Se obtienen todos los artículos en orden de publicación",
         tags=["Posts"])
def get_posts(request):
    all_posts = Post.objects.all().order_by('publish_date').values()
    return list(all_posts)

@app.get(path="posts/{post_id}",
         summary="Artículo Específico",
         description="Se obtiene los datos de un artículo específico", 
         tags=["Posts"], 
         response=PostSchema)
def get_post(request, post_id: int = Path(..., description="ID del artículo", gt=0, example=11)):
    post = get_object_or_404(Post, id=post_id)
    return post

@app.post(path="posts/", 
         summary="Agregar Artículo",
         description="Se envía un artículo al servidor para ser creado", 
         tags=["Posts"])
def add_post(request, data: PostSchema):
    post = Post.objects.create(**data.dict())
    return { "id": post.id, "title": post.title }

@app.put(path="posts/{post_id}", 
         summary="Modificar Artícxulo",
         description="Se envían los datos para modificar un artículo", 
         tags=["Posts"])
def update_post(request, post_id: int, data: PostSchema):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in data.dict().items():
        setattr(post, attr, value)
    post.save()
    return { "id": post.id, "title": post.title }

@app.patch(path="posts/{post_id}", 
         summary="Modificar partes Artículo",
         description="Se modifican atributos del artículo como no vigente.", 
         tags=["Posts"])
def patch_post(request, post_id: int):
    return {}

@app.delete(path="posts/{post_id}", 
         summary="Eliminar Artículo",
         description="Se marca el artículo como no vigente.", 
         tags=["Posts"])
def delete_post(request, post_id: int):
    return {}
