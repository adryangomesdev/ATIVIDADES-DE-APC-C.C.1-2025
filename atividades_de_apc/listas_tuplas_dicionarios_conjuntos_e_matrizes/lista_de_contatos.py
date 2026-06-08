quantidade_cadastro = int(input())
cardapio = {}
valor = 0 

for i in range(quantidade_cadastro):
    numero_identificacao = int(input())
    descricao_produto = input()
    preco = float(input())
    cardapio[numero_identificacao] = preco

while True:
    pedido_codigo = int(input())
    if pedido_codigo == 0:
        break
    quantidade_pedido = int(input())
    
    if pedido_codigo not in cardapio:
        continue
    if quantidade_pedido <= 0:
        continue
    
    if pedido_codigo in cardapio:
        valor += cardapio[pedido_codigo] * quantidade_pedido

print(f"{valor:.2f}")