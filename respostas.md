
## Ex1

### a) 

1. Texto vazio
2. Uma palavra
3. Duas palavras
4. Palavras repetidas
5. Maiúsculas e minúsculas
6. Espaços múltiplos
7. Quebra de linha
8. Palavra com hífen
9. Pontuação com ponto e exclamação
10. Vírgula e ponto e vírgula
11. Dois-pontos e interrogação
12. Apenas pontuação

Escolhi o texto vazio primeiro porque é o caso mais básico. Depois coloquei uma palavra só, para testar se a função consegue fazer uma contagem simples. Os outros testes vão adicionando mais situações

### b)

A função usa `split()` para separar as palavras, `lower()` para deixar tudo minúsculo e `strip()` para remover a pontuação.

Os testes foram organizados do mais simples para o mais complexo, seguindo a ideia de testar antes de implementar.

### c)

13cb1a0 (HEAD -> main) RED: tratar pontuacao nas palavras
dc8aced GREEN: normalizar letras
418670f RED: ignorar maiusculas
cd9bd1f GREEN: somar ocorrencias
d4510b3 RED: contar palavras repetidas
73e2eaa GREEN: separar palavras
b47914e RED: contar duas palavras
132443a GREEN: contar uma palavra
4bb15ec RED: contar uma palavra
3f5c956 RED: contar uma palavra
f74b1be GREEN: retornar dicionario vazio
90e4ce8 RED: texto vazio retorna dicionario vazio
2d2fe47 (origin/main, origin/HEAD) Initial commit

### d) 

Alguns testes podem passar de primeira porque o código feito para um teste anterior já resolve outros casos.

Mesmo assim, eles ficam na suíte porque ajudam a garantir que essas situações continuem funcionando.

### e) 

Resultados obtidos:

- 12 testes passaram
- Cobertura: 100%
- 15 mutantes gerados
- 13 mutantes eliminados
- 2 mutantes sobreviveram
- Escore de mutação: 86,67%

Mesmo com 100% de cobertura, dois mutantes sobreviveram. Isso mostra que ter cobertura total não significa necessariamente que todos os casos foram bem testados.


## Ex2

historico git 

78e0ca1 (HEAD -> main, origin/main, origin/HEAD) GREEN: validar tipo de senha
8b604dd RED: rejeitar tipo invalido
9946c90 GREEN: implementar senhas prioritarias
d52fdb0 RED: emitir senhas prioritarias
d8d7dd0 GREEN: implementar fila normal
45b7d11 RED: emitir e chamar senhas normais
4eebf17 GREEN: tratar fila vazia
6d17ed8 RED: chamar fila vazia gera erro
64446ee GREEN: inicializar fila vazia
91b5081 RED: fila comeca vazia


### a) 

1. Fila começa vazia
2. Chamar fila vazia gera erro
3. Senhas normais são numeradas corretamente
4. Senhas prioritárias são numeradas corretamente
5. Tipo inválido gera erro
6. Numeração normal e prioritária é independente
7. Prioritária passa na frente da normal
8. Depois de duas prioritárias chama uma normal

### b) 

Criei a classe `Fila` usando duas filas, uma normal e outra prioritária.

Também usei um contador para controlar quantas prioritárias foram chamadas seguidas.

A ideia do TDD é criar o teste, ver ele falhar e depois implementar o necessário para passar.

### c) Qual teste obrigou a contar e zerar as prioritárias?

O `test_limite_duas_prioritarias` obrigou a contar, porque a sequência precisa ser:

`P1, P2, N1, P3`

O `test_zerar_contagem` verifica se o contador volta para zero depois de chamar uma normal.

### d) Qual teste mostra que o limite não vale sem normais?

O `test_sem_normal_nao_limita`.

Nesse teste, a fila chama `P1, P2, P3, P4`, porque não tem nenhuma senha normal esperando.

### e) Resultado do mutmut



---

## Ex3

### a) Quais testes antigos precisam mudar?

Os testes antigos aplicavam o cupom DEZ mesmo em compras abaixo de 10000.

Agora o desconto só funciona a partir desse valor, então os testes precisam ser atualizados antes de mudar o código.

Por exemplo, uma compra de 5000 com o cupom DEZ agora continua com total de 5000, e não 4500.

### b) Implementação com TDD

As regras implementadas foram:

- DEZ dá 10% a partir de 10000
- VINTE dá 20% a partir de 30000
- Abaixo do mínimo não tem desconto
- Um cupom novo substitui o anterior
- A quantidade precisa ser um inteiro maior ou igual a 1

Os testes verificam essas regras e os valores próximos dos limites.

### c) Refactor dos cupons

Os cupons ficaram assim:

```python
CUPONS = {
    "DEZ": (10, 10000),
    "VINTE": (20, 30000)
}
```

Assim fica mais fácil guardar o desconto e o valor mínimo juntos.

Se todos os testes continuam passando depois da mudança, significa que o comportamento não foi alterado.

### d) Valores de quantidade testados

Testei:

- `1` e `3`: quantidades válidas
- `0` e `-1`: valores inválidos
- `1.5`: número não inteiro
- `"2"`: texto em vez de número
- `None`: valor inválido
- `True`: booleano, que também não deve ser aceito

Esses testes servem para verificar se o carrinho aceita apenas quantidades inteiras a partir de 1.