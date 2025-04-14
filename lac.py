usuario = input('digite o login: ')
senha = input('digite a senha: ')

if usuario == ('joao') and senha == ('2828'):
    print('acesso permitido')

elif senha != ('2828'):
  print('senha ou usuario incorreto')
else:
  print('acesso negado')


filmes = input('digite o genero do filme')
if filmes == 'terror':
    print('invocação do mal')
elif filmes == 'comedia':
    print('gente grande')
elif filmes == 'ação':
    print('tropa de elite')
elif filmes == 'suspense':
    print('fuja')
elif filmes == 'romance':
    print('a cinco passos de voce')
else:
    print('filmes não encontrados')


    pontos = 0
    resposta = input("quem escreveu dom quixote? ")
    if resposta.lower() == "cervantes":
        pontos += 10

