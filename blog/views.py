from django.shortcuts import render

posts = [
    {
        'id': 1,
        'titulo': 'Meu Primeiro Post',
        'conteudo': 'Este é o conteúdo do meu primeiro post no blog.',
        'autor': 'Vinicius',
    },
    {
        'id': 2,
        'titulo': 'Outro Post Interessante',
        'conteudo': 'Mais conteúdo fascinante para você ler.',
        'autor': 'Vinicius',
    }
]

def index(request):
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render(request, 'blog/post.html', {'post': post})
    else:
        return render(request, 'blog/404.html', {'message': 'Post não encontrado'})

def not_found(request):
    return render(request, 'blog/404.html', {'message': 'Página não encontrada'})