from ninja import NinjaAPI
from users.api import users_router

# Cria uma instância da API Ninja
api = NinjaAPI()

# Adiciona o roteador de usuários na rota '/user'
api.add_router('/users', users_router)