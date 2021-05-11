---
## Por onde eu começo? - Entendendo o Problema
Este texto descreve brevemente os principais passos e pesquisas que se fizeram necessárias para realizar este projeto.

---
## Escolhendo a linguagem
Para realizar o desafio utilizei Python, já que tenho maior fluência nesta linguagem.

---
## Escolhendo o padrão a ser utilizado
Devido ao descritivo do problema, em específico na parte onde é grifado:

> Você deve implementar as seguintes regras, tendo em mente que novas regras aparecerão no futuro [...]

Decidi utilizar o padrão Strategy, pois com ele, tenho a vantagem de poder introduzir novas estratégias de validação
sem necessariamente alterar o contexto, isolando as lógicas de negócio que definem as classes `Account` e 
`Transaction` dos códigos que efetivamente validam as transações.

---
## Construção do CLI
Pensando na utilização da aplicação, decidi fazer um cli command `authorize` para que a aplicação fosse utilizada por ele.
De qualquer forma, ele se trata da mesma `main()` que encontramos em `./src/authorizer.py` e é equivalente a rodar:
```
python ./src/authorizer.py <local_do_arquivo>
```
É devido a este CLI que foram incluídas as definições encontradas em setup.py e a indicação de rodar a aplicação em um Virtualenv

---
## Testes 
Para a realização dos testes de unidade e de integração decidi utilizar a biblioteca unittest, pois ser nativa e de eficaz e rápida implementação.

---
## Desafios

---
## Aprendizados
