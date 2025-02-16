from ninja import Router

# Importa o objeto Router para definir rotas no aplicativo
users_router = Router()

# Define uma rota POST na raiz do users_router ('/')
# A resposta esperada tem status 200 e retorna um dicionário
@users_router.post('/', response={200: dict})
def create_user(request):
    # Retorna um dicionário com a chave 'ok' (possível erro, pois 'ok' não foi definido)
    return {'ok': 'ok'}  # Isso pode gerar um NameError se 'ok' não estiver definido