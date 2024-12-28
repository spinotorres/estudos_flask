# Primeiro Projeto em Flask

## Objetivos
Aprender e exercitar os conceitos elementais do framework flask.

## Elementos Apresentados

- Definição e rotas e seus conceitos a partir da uma função decorator `@app.route`.
- Execução da aplicação a partir `app.run()` podendo utilizar o `app.run(debug=True)` para atualizar em tempo real o código.
- Método `POST` para utilização de formulários do HTML.
- Método `redirect()` utilizado para redirecionar o navegador para outra URL.
- Função `url_for()` utilizado para direcionar para URLs dentro do próprio HTML, utiliza template do Jinja2.
- Objeto `session` um recurso do flask que permite armazenar dados temporários no próprio cookie do navegador. Necessário utilizar `app.secret_key = 'alguma_senha'` para evitar usuários maliciosos.