# Boas-vindas ao repositório do Traduzo

Atente-se a cada passo descrito a seguir pois eles lhe ajudarão a realizar o projeto! #vqv 🚀

![Tela](src/views/static/images/traduzo.png)

A partir deste repositório você encontra os detalhes de como estruturar o desenvolvimento do seu projeto.

<details>
<summary>📃 Termos e acordos</summary>

- Ao iniciar este projeto, você concorda com as diretrizes do [Código de Conduta e do Manual da Pessoa Estudante da Trybe](https://app.betrybe.com/learn/student-manual/codigo-de-conduta-da-pessoa-estudante).

</details>

----

## Entregáveis

<details>
<summary>🧑‍💻 O que deverá ser desenvolvido</summary>

- Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Back-end irá fornecer a camada View, para a pessoa usuária.

</details>

<details>
  <summary>📝 Habilidades a serem trabalhadas </summary>

Neste projeto, verificamos se você é capaz de:

- Implementar uma API utilizando arquitetura em camadas MVC;
- Utilizar o Docker para projetos Python;
- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints;
- Interagir com um banco de dados não relacional MongoDB;
- Desenvolver páginas web Server Side.

</details>

<details>
<summary>🕊️ Como entregar</summary>

- Crie um _Pull Request_ deste repositório para realizar a entrega do projeto.

- Quando preciso, consulte:
  - Nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/fc998c60-386e-46bc-83ca-4269beb17e17/section/fe827a71-3222-4b4d-a66f-ed98e09961af/day/35e03d5e-6341-4a8c-84d1-b4308b2887ef/lesson/573db55d-f451-455d-bdb5-66545668f436);
  - Nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/).

</details>

----

## Preparando Ambiente

<details>

<summary>🐳 Subindo a aplicação</summary>

**[1]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[2]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**[3 - Opção A]** Suba o projeto pelo Docker

```bash
docker compose up translate
```

- Recomendado: Dockerfile e Docker-compose já estão prontos para uso, para subir o MongoDB e o Flask.

**[3 - Opção B]** Caso queira subir somente o banco MongoDB pelo Docker

```bash
docker compose up -d mongodb

python3 src/app.py
```

**[4]** Comece seu desenvolvimento, podendo inclusive já acessar a aplicação pelo navegador na rota <http://127.0.0.1:8000/> caso utilize a padrão do projeto.

- Em primeiro momento, praticamente nada funcionará, então vamos já para programação.

**[5]** 💡Dica: O projeto utilizará a Pymongo, mas se preocupe pouco com o Mongodb, pois assim como no conteúdo, você precisará penas herdar a classe abstrata [abstract_model](src/models/abstract_model.py) em sua model, para que tenha acesso aos principais métodos de manipulação do banco.

**[6]** 💡Dica: Ao rodar a aplicação via docker, algumas variáveis de ambiente estão configuradas. O banco de dados populado ao rodar a aplicação localmente será diferente. Se encontrar alguma divergência, consulte o arquivo [db.py](src/database/db.py) e certifique-se de que está executando os comados no ambiente escolhido, local ou docker.

</details>

----

## Executando os Testes

<details>
<summary>🛠 Pytest pelo ambiente virtual (Recomendado) </summary>

Por uma melhor integração com o Vscode, e devido o ambiente virtual ser mais leve que um container, ainda é uma boa recomendação.

**[1]** Crie o ambiente virtual, e instale as dependências, suba o banco, conforme seção preparando ambiente

**[2]** Execute os testes

```bash
python3 -m pytest
```

</details>

<details>
<summary>🗳️ Pytest pelo Container Docker </summary>

**[1]** Execute o projeto conforme seção preparando ambiente

**[2]** Execute os testes diretamente, ou após acessar o sh do container

```bash
docker compose exec -it translate pytest
```

```bash
docker compose exec -it translate sh
```

- Atente-se a realizar um novo Build, sempre que alterar a instalação do container.

</details>

----

## Requisitos

### 1 - MODEL - Instanciando idiomas

- Use a classe `LanguageModel` em [language_model.py](src/models/language_model.py)
- `LanguageModel` deve herdar a `AbstractModel` de [abstract_model.py](src/models/abstract_model.py)
- Defina uma coleção chamada `languages` para a classe `LanguageModel` através de um atributo de classe chamado `_collection`. Você pode usar como exemplo a implementação em [user_model.py](src/models/user_model.py)
- Crie o método **init** para a classe chamada `LanguageModel`, ele deve receber um dicionário como argumento que você deve passar como parâmetro para o construtor da classe herdada. Ela já cuidará de persistir em um atributo de instância chamado de `data`.
Exemplo de como o construtor receberá um dicionário (estilo JSON) como argumento:

```JSON
{"name": "afrikaans", "acronym": "af"}
```

<details>
<summary>O que será testado:</summary>

- Se o método `save()` da classe `AbstractModel` já pode ser utilizado por uma instância da classe ``LanguageModel`` (este método já está implementado).
- Se após salvar, já teremos uma ID do mongoDB, para a `Language`.

</details>

💡 Dica: Com tudo certo até aqui, você pode popular o banco de dados com as `seeds` que já estão prontas com mais de 130 idiomas, basta executar:

```bash
# caso esteja usando o ambiente virtual local
python3 src/run_seeds.py

# ou, caso esteja rodando a aplicação via docker
docker compose exec -it translate python3 src/run_seeds.py
```

## 2 - MODEL - Conversão atributo self.data para Dicionário

O retorno padrão do MongoDB é um Objeto Serializado em Binário (formato conhecido por BSON), seu funcionamento é próximo de um dicionário, porém, precisaremos do formato de dicionário para facilitar a futura conversão para JSON.

- Implemente o método `to_dict()` da classe `LanguageModel`. Ele deve retornar um novo dicionário contendo os atributos `name` e `acronym`.
- Os dados para a conversão, devem estar dentro da variável `self.data`.

<details>
<summary>O que será testado:</summary>

- Se uma instância de `LanguageModel`, consegue retornar um dicionário através do método `to_dict()`.

</details>

## 3 - MODEL -  Listagem de Idiomas como Dicionários

Retornaremos todos os idiomas como uma lista iterável.

- Implemente o método de classe `list_dicts()` para a classe `LanguageModel`.
- O método `list_dicts()` deve buscar através de um `find()` todas os idiomas cadastrados.
- Converta cada idioma do retorno para um dicionário e adicione em uma lista, que deverá ser o retorno final do método.

<details>
    <summary>O que será testado:</summary>

- Que é possível acessar o método `list_dicts()` através da notação `LanguageModel.list_dicts()`;
- O retorno deverá ser a lista com todos os idiomas cadastrados.

</details>

## 4 - CONTROLLER & VIEW -  Endpoint Tradutor, renderizando variáveis do Back-end - GET

Para renderizar variáveis em uma template, o Back-end (Controller) deve as enviar como parâmetros do método `render_template`. Os parâmetros que devem ser incluídos são:

- languages: Todos os idiomas disponíveis, que devem ser obtidos utilizando o método `LanguageModel.find()`;
- text_to_translate: A string "O que deseja traduzir?";
- translate_from: O acrônimo do idioma de origem da tradução, padronizado como `pt`;
- translate_to: O acrônimo do idioma de destino da tradução, padronizado como `en`;
- translated: A string "What do you want to translate?".

O valor de `text_to_translate` deve ser inserido no `input` de origem, e o valor de `translated` deve ser inserido no `input` de destino.

Para este requisito, implemente a função `index()` que já existe no arquivo `src/controllers/translate_controller.py`. Essa função já possui uma implementação básica para a rota `/`.

Além disso, será também necessário atualizar o *template* `src/views/templates/index.html` com as variáveis do Back-end. Os nomes das linguagens devem aparecer em maiúsculo no template.

- Adicione as variáveis no Front-end, dando sentido à navegação. Por exemplo, todos os idiomas devem ser inseridos como `Options` no `select` que está vazio.

```html
   <select name="translate-from">
   </select>
```

- Você também precisa implementar a lógica no template para adicionar a flag `selected`, no idioma que equivaler ao acrônimo que o Back-end enviou.

💡 Dica: `Jinja2` permite criar um `if`, de dentro da declaração de uma <option ...if...> </option>

<details>
<summary>O que será testado:</summary>

- A página deve exibir o texto "O que deseja traduzir?" no input de origem.
- A página deve exibir a palavra "What do you want to translate?" no input de destino.
- A página deve exibir todas as opções de idioma, no Select Options do template onde cada opção corresponde a um idioma existente no sistema.
- As opções de idioma devem estar todas em letras maiúsculas.

</details>

## 5 - CONTROLLER - Tradução de Texto - POST

Chegou a hora de traduzir o texto, para isso, a rota POST `/` deve receber os seguintes parâmetros no corpo da solicitação:

- `text_to_translate`: Uma string contendo o texto a ser traduzido;
- `translate_from`: Uma string contendo o idioma de origem do texto;
- `translate_to`: Uma string contendo o idioma de destino da tradução;

  Ao receber a solicitação, você deve realizar a tradução do texto usando os idiomas e a lógica de tradução adequados.

  💡 Dica: use o objeto `request` para conseguir resgatar os parâmetros enviados na solicitação. Lembre-se que as chaves dos parâmetros são definidas de acordo com o atributo `name` dos elementos HTML.

<details>
  <summary>O que será testado:</summary>

- Se ao enviar `text_to_translate` como "Hello, I like videogame", `translated` será "Olá, eu gosto de videogame".
- Se na requisição, `translate_from` está selecionado `en` e se `translate_to` está selecionado `pt`.

</details>

💡 Dica: A biblioteca da API do `GoogleTranslator` já está instalada. O arquivo `example.py`, na raiz do projeto, possui um código de exemplo e você pode usar para compreender seu funcionamento. Para isso, execute `python3 example.py`.

💡 Dica 2: Não temos histórico da API do `GoogleTranslator` parar de funcionar, mas, caso ocorra, você pode optar pela estratégia de traduzir manualmente *strings* pré definidas por você e pelo teste, para seguir normalmente com o desenvolvimento.

## 6 - CONTROLLER - Tradução Reversa - POST

Se você acessou a aplicação, deve ter visto no Front-end um botão para inverter a linguagem. Vamos implementar sua funcionalidade agora.

- Implemente a função `reverse()` que será responsável por uma nova rota chamada `/reverse` com o método POST. Ela deve renderizar o mesmo template (`index.html`) e também deve receber os mesmos parâmetros que a rota principal:
  - `text_to_translate`: Uma string contendo o texto a ser traduzido.
  - `translate_from`: Uma string contendo o idioma de origem do texto.
  - `translate_to`: Uma string contendo o idioma de destino da tradução.

- Faça a tradução assim como na rota principal, porém, com uma diferença: Ao renderizar o template, você deverá inverter os idiomas de origem `translate_from` e destino `translate_to` e também inverter o texto traduzido `translated` e o texto original `text_to_translate`.

Não se esqueça que, sempre que renderizar novamente o template, passar os seguintes parâmetros:

- languages: A lista de idiomas existentes, obtidos usando o método `LanguageModel.find()`;
- text_to_translate: O texto traduzido;
- translated: O texto original antes da tradução;
- translate_from: O idioma de destino;
- translate_to: O idioma de origem.

<details>
  <summary>O que será testado:</summary>

- Se ao enviar `text_to_translate` como "Hello, I like videogame", `translated` ficará com texto "Hello, I like videogame" e `text_to_translate` passa a ser sua tradução "Olá, eu gosto de videogame".
- Se na requisição, `translate_from` está selecionado `pt` e se `translate_to` está selecionado `en`.


</details>

## 7 - TESTE - Histórico de Traduções

Em dias atuais, analisar dados pode gerar muitos aprendizados. Por hora, vamos armazenar o histórico de traduções.

A classe `HistoryModel`, já foi implementada pela equipe inicial, porém foi utilizada uma classe auxiliar `BSONToJSON`, que não deixou o time tão confiante, principalmente porque foi criada sem testes. Nossa missão aqui será criar um teste para verificar se o método `list_as_json()` funciona adequadamente. Este método é responsável por retornar um JSON que contém os históricos salvos.

- Crie o teste no arquivo `tests/models/history/test_history_model.py`
- Carregue no teste os JSONs de `HistoryModel.list_as_json()`
- Confira se o conteúdo do JSON apresenta o conteúdo da fixture `prepare_base()`, implementada em `tests/models/history/conftest.py`.

💡 Dica: Lembre que para carregar os dados de um JSON em Python é possível usar a biblioteca `JSON`.

<details>
  <summary>O que será testado:</summary>

- Aqui entram os testes de seu teste, que serão executados pelo arquivo `tests/models/history/test_to_test_history_model.py`. Este arquivo **NÃO** deverá ser alterado.

</details>

## 8 - Endpoint de Listagem de Histórico de Traduções - API GET

O objetivo aqui é criar um *endpoint* que permita a listagem dos registros de histórico de traduções.

- Crie um novo arquivo para a *controller* do *endpoint*, use as controllers já implementadas como referência.
- A nova *controller* responderá a um `GET` em `http://localhost:8000/history`.
- Registre a `Blueprint` da controller no `app.py`.
- Ao receber uma requisição `GET` na rota, o *endpoint* deve retornar os registros de histórico de traduções em formato JSON.
- O *endpoint* deve retornar uma resposta HTTP com status `200 (OK)` e o conteúdo JSON contendo os registros de histórico.
- Garanta que ao realizar uma tradução na rota `POST` `http://localhost:8000/` (`src/controllers/translate_controller.py`), também seja criado o histórico. 

## 9 - TESTE - Exclusão de Histórico de Traduções - DELETE

Será preciso fornecer a equipe de administração do sistema a possibilidade de excluir um histórico por meio do endpoint `DELETE` na rota `/admin/history/<id>`. Esse endpoint necessita de um token que irá autorizar a requisição.

O código desta funcionalidade já foi implementado em [src/controllers/admin_controller.py](src/controllers/admin_controller.py), porém, para esta tarefa ser considerada como concluída, será necessário que esse código seja testado.

- Crie um teste automatizado para verificar a funcionalidade de exclusão do histórico de traduções.
- O teste deve ser escrito em `tests/controllers/admin/test_admin_controller.py`.
- O teste `test_history_delete` deve simular a exclusão de um registro específico do histórico e verificar se subtraiu um da base de dados usada.
- Você precisará salvar no banco um objeto `UserModel` para a autenticação e objetos `HistoryModel` para testar a exclusão.
- `app_test` é uma fixture definida no `conftest.py`. Você pode usá-la no teste, para chamar a requisição delete.
- 

Veja um exemplo de como passar um header para uma requisição:

```python
 app_test.delete(f"/admin/history/{id}", headers={
      "Authorization": "um token",
      "User": "um nome",
  })
```

💡 Dica: Para compreender a criação de um `user` e a geração de seu token, veja a implementação do arquivo `src/models/user_model.py`.

----

<details>
<summary>🗣 Nos dê feedbacks sobre o projeto!</summary>

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário.
**Leva menos de 3 minutos!**

[Formulário de avaliação do projeto](https://be-trybe.typeform.com/to/ZTeR4IbH#cohort_hidden=CH1&template=betrybe/python-0x-projeto-traduzo)

</details>
  
<details>
<summary>🗂 Compartilhe seu portfólio!</summary>

Você sabia que o LinkedIn é a principal rede social profissional e compartilhar o seu aprendizado lá é muito importante para quem deseja construir uma carreira de sucesso? Compartilhe esse projeto no seu LinkedIn, marque o perfil da Trybe (@trybe) e mostre para a sua rede toda a sua evolução.

</details>
