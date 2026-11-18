# Global Solution Citizen Assist AI - Data Structures and Algorithms 

Projeto desenvolvido para a disciplina **Data Structures and Algorithms (DSA)** (*Global Solution | Citizen Tech*).

**Link**: [Evidências dos testes](TESTES.md)

**Integrantes**:
|Nome|RM|
|:---:|:---:|
|Andrei Henrique Santos|569440|
|Heitor Maxímus Mucha|571407|
<br>
---

## 1. Objetivo do Sistema

O **Citizen Assist AI** é um protótipo de sistema de gerenciamento e consulta de informações desenvolvido em Python. Seu objetivo é centralizar e organizar registros simulados de serviços e orientações de interesse público, como emissão de documentos, assistência social, educação, saúde e atendimento comunitário; permitindo que o usuário realize operações completas de cadastro, consulta, pesquisa por atributos, atualização, exclusão e ordenação por meio de um menu interativo em linha de comando (CLI), aplicando estruturas de dados e algoritmos próprios sem depender de listas nativas como estrutura principal de armazenamento.

---

## 2. Campos dos Registros (`Servico`)

Cada registro de serviço ou orientação é modelado pela classe `Servico` (definida em `classes.py`) e contém seis atributos obrigatórios, todos tratados como strings textuais após sanitização com `.strip()` na camada de interface:

| Campo / Atributo | Tipo | Obrigatoriedade | Descrição |
| :--- | :---: | :---: | :--- |
| `id_servico` | `str` | Obrigatório (Único) | Identificador único do serviço na base de dados, impedindo duplicidades no cadastro. |
| `titulo` | `str` | Obrigatório | Nome ou título resumido do serviço ou orientação ao cidadão. |
| `categoria` | `str` | Obrigatório | Área temática do serviço (ex.: Saúde, Educação, Assistência Social, Documentação). |
| `descricao` | `str` | Obrigatório | Detalhamento completo sobre o funcionamento, requisitos ou orientações do serviço. |
| `publico_alvo` | `str` | Obrigatório | Perfil ou grupo de cidadãos elegíveis para utilizar o serviço. |
| `canal` | `str` | Obrigatório | Canal digital, telefone ou local físico de atendimento ao cidadão. |

---

## 3. Descrição da Lista Encadeada

A estrutura principal de armazenamento é uma **Lista Simplesmente Encadeada** implementada manualmente por meio de duas classes em `classes.py`:

### Estrutura dos Nós (`No`)
Cada elemento da lista é encapsulado por uma instância da classe `No`, composta por dois atributos:
* `self.servico`: armazena a referência para a instância do objeto `Servico` (carga útil).
* `self.proximo`: ponteiro (referência explícita) que aponta para o próximo `No` da cadeia, ou `None` quando representa o último elemento da lista.

### Gerenciamento da Estrutura (`ListaEncadeada`)
A classe `ListaEncadeada` controla o encadeamento mantendo a referência inicial `self.head` (inicializada como `None`) e o contador de elementos `self.size` (inicializado em `0`). Suas operações estruturais funcionam da seguinte forma:
* **Inserção (`adicionar_servico`):** Percorre a lista a partir de `self.head` para validar que `id_servico` não existe; em seguida, cria um novo `No` e o encadeia ao final da lista (ajustando `self.head` caso a lista esteja vazia ou o ponteiro `.proximo` do último nó existente), incrementando `self.size`.
* **Percurso e Consulta (`consultar_registro`):** Navega sequencialmente através dos ponteiros `.proximo` a partir de `self.head` para listar todos os registros, localizar um nó específico por `id_servico` ou filtrar múltiplos registros por substring em `titulo` ou `categoria`.
* **Atualização (`atualizar_registro`):** Localiza o nó desejado por meio de `consultar_registro(id_servico)` e sobrescreve apenas os atributos do objeto `Servico` que receberam novos valores válidos (mantendo intactos os campos deixados em branco).
* **Remoção (`excluir_registro`):** Percorre a lista mantendo dois ponteiros (`no_atual` e `no_anterior`). Ao encontrar o `id_servico`, ajusta `self.head = no_atual.proximo` (se for o primeiro nó) ou `no_anterior.proximo = no_atual.proximo` (se estiver no meio ou fim), removendo o nó da cadeia e decrementando `self.size`.
* **Ordenação (`ordenar_registros`):** Executa o algoritmo *Bubble Sort* diretamente sobre os nós encadeados, comparando `titulo` ou `id_servico` (com `.casefold()`) e permutando as referências `no_atual.servico` entre nós adjacentes sem quebrar o encadeamento.

---

## 4. Organização do Código

O projeto é modularizado em dois arquivos Python no mesmo diretório, separando a camada de estrutura de dados/regras de negócio da camada de interação com o usuário:

```text
projeto_citizen_assist/
├── classes.py   # Camada de modelo de dados e estrutura encadeada
└── main.py      # Camada de apresentação, menu interativo e validação de entrada
```

* **`classes.py`:** Contém exclusivamente as definições das classes `Servico` (entidade de domínio), `No` (unidade de encadeamento) e `ListaEncadeada` (implementação das operações CRUD, busca linear e ordenação *Bubble Sort*).
* **`main.py`:** Importa `ListaEncadeada` e `Servico` de `classes.py`, instancia a lista vazia e executa a função `executar_menu(lista)`. Gerencia o laço principal da interface de terminal, captura as entradas do usuário, valida campos vazios ou opções inválidas e invoca os métodos correspondentes da lista encadeada.

---

## 5. Instruções de Uso e Execução

### Pré-requisitos
* Interpretador **Python 3.8 ou superior** instalado no sistema (necessário para suporte ao método `.casefold()` e à biblioteca padrão, sem dependências externas).
* Os arquivos `classes.py` e `main.py` salvos na mesma pasta.

### Como Executar
1. Abra o terminal (Prompt de Comando, PowerShell, Bash ou terminal da IDE).
2. Navegue até o diretório onde os arquivos do projeto estão salvos:
   ```bash
   cd caminho/para/pasta_do_projeto
   ```
3. Execute o arquivo principal `main.py`:
   ```bash
   python main.py
   ```

### Guia de Operação no Menu Interativo
Ao iniciar o sistema, será exibido o menu principal com 8 opções numeradas:

* **`1 - Cadastrar serviço`:** Solicita sequencialmente ID, Título, Categoria, Descrição, Público-alvo e Canal/local. Todos os campos são obrigatórios e o ID deve ser único.
* **`2 - Consultar todos os serviços`:** Exibe todos os registros cadastrados na ordem atual da lista encadeada ou informa caso a lista esteja vazia.
* **`3 - Consultar serviço por ID`:** Solicita um identificador e exibe os dados do registro correspondente, caso exista.
* **`4 - Pesquisar por título ou categoria`:** Permite escolher entre pesquisar por Título (`1`) ou Categoria (`2`) e solicita um termo de busca (não diferenciado por maiúsculas/minúsculas).
* **`5 - Atualizar serviço`:** Solicita o ID do serviço existente; caso encontrado, permite digitar novos valores para cada campo ou pressionar `Enter` (deixando vazio) para preservar o valor atual.
* **`6 - Excluir serviço`:** Solicita o ID do serviço e o remove da lista encadeada, religando os ponteiros vizinhos.
* **`7 - Ordenar serviços`:** Permite ordenar os registros por Título (`1`) ou Identificador (`2`) em ordem alfabética e exibe a lista já ordenada.
* **`0 - Sair`:** Encerra a execução do programa.

---

## 6. Estratégias de Busca e Ordenação

### 6.1. Estratégia de Busca: Busca Linear (Sequencial)
A busca é implementada no método `consultar_registro(self, id_servico=None, atributo=None, termo=None)` da classe `ListaEncadeada`. Como a estrutura de armazenamento é uma lista simplesmente encadeada (sem acesso direto por índice como em vetores), a estratégia percorre os nós sequencialmente a partir do ponteiro inicial `self.head` até alcançar o final da lista (`None`):

1. **Busca por Identificador Único (Caso 3):** O ponteiro `no_atual` inicia em `self.head` e avança nó a nó (`no_atual = no_atual.proximo`) comparando exatamente `no_atual.servico.id_servico == id_servico`. Assim que o registro correspondente é encontrado, o algoritmo imprime seus dados e interrompe a execução retornando o nó (`return no_atual`).
2. **Busca por Substring em Atributos Textuais (Caso 2):** Quando a pesquisa ocorre por `titulo` ou `categoria`, o método valida o atributo e o termo, inicializa uma lista auxiliar `resultados = []` e percorre **toda** a lista encadeada. Para cada nó, converte tanto o valor armazenado quanto o termo buscado com `.casefold()` (ignorando diferenças entre maiúsculas e minúsculas) e verifica a ocorrência parcial (`termo.casefold() in valor.casefold()`). Todos os serviços compatíveis são acumulados e retornados ao final do percurso.
3. **Varredura Completa (Caso 1):** Quando nenhum filtro é informado, o algoritmo apenas percorre todos os nós a partir de `self.head` exibindo cada registro.

### 6.2. Algoritmo de Ordenação: Bubble Sort Otimizado com Flag de Troca
A ordenação está implementada no método `ordenar_registros(self, criterio="titulo")` da classe `ListaEncadeada`:

1. **Validação e Casos Base:** O método verifica se o critério escolhido é `"titulo"` ou `"id_servico"`. Caso a lista esteja vazia (`self.head is None`) ou possua apenas um elemento (`self.head.proximo is None`), retorna `True` imediatamente, pois já está ordenada.
2. **Laço Externo (`while houve_troca`):** Utiliza uma variável booleana `houve_troca` como mecanismo de parada antecipada. Se durante uma passagem completa pela lista nenhuma troca for realizada, significa que todos os elementos já estão ordenados e o algoritmo encerra antes de executar passagens desnecessárias.
3. **Laço Interno e Troca de Carga Útil:** A cada passagem, `no_atual` parte de `self.head` e compara o atributo do nó atual com o do nó adjacente (`no_atual.proximo`) utilizando `str(...).casefold()` para ordenação alfabética *case-insensitive*. Quando `valor_atual > valor_proximo`, o algoritmo realiza a **troca direta das referências dos objetos `Servico` entre os nós** (`no_atual.servico, no_atual.proximo.servico = no_atual.proximo.servico, no_atual.servico`), mantendo intactos os ponteiros `.proximo` da estrutura encadeada.

---

## 7. Análise de Complexidade (Notação Big-O)

### Hipóteses Adotadas
* **$n$:** Representa o número total de nós (serviços cadastrados) armazenados na `ListaEncadeada` (`self.size`).
* **Estrutura de Dados:** Trata-se de uma lista simplesmente encadeada que mantém apenas a referência para o início (`self.head`), **não** possuindo ponteiro para o último nó (`tail`).
* **Custo das Operações Básicas:** Comparações de igualdade, atribuições de ponteiros e acesso a atributos de objetos são considerados operações de tempo constante, $\mathcal{O}(1)$. Para a análise assintótica em função de $n$, o tamanho das strings dos atributos (`id_servico`, `titulo`, `categoria`) é tratado como limitado por uma constante.

### Tabela Resumo de Complexidade Temporal

| Operação | Melhor Caso | Caso Médio | Pior Caso | Justificativa Baseada no Código |
| :--- | :---: | :---: | :---: | :--- |
| **Inserção** (`adicionar_servico`) | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Verificação de ID duplicado + inserção no final sem ponteiro `tail`. |
| **Busca por ID** (`consultar_registro`) | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Parada antecipada ao encontrar o ID (`return no_atual`). |
| **Busca por Atributo** (`consultar_registro`) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Percorre obrigatoriamente todos os $n$ nós para coletar todas as ocorrências. |
| **Exclusão** (`excluir_registro`) | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Busca linear pelo ID antes de religar os ponteiros `no_anterior.proximo`. |
| **Ordenação** (`ordenar_registros`) | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | Bubble Sort com flag `houve_troca` operando sobre nós adjacentes. |

### Detalhamento por Operação

#### 1. Inserção - `adicionar_servico(self, servico)`
* **Complexidade:** **$\mathcal{O}(n)$** no pior caso e caso médio; **$\mathcal{O}(1)$** apenas se a lista estiver vazia (`self.head is None`).
* **Análise:** Embora a inserção em si de um nó em lista encadeada possa ser $\mathcal{O}(1)$, o código implementado realiza duas travessias lineares sequenciais:
  1. Um primeiro laço `while no_atual is not None` percorre toda a lista para garantir que o `id_servico` não esteja duplicado.
  2. Um segundo laço `while atual.proximo is not None` percorre novamente até o último nó para inserir o `novo_no` no final da lista (já que não há ponteiro `tail`).
  * O custo total é proporcional a $n + n = 2n$, o que assintoticamente resulta em **$\mathcal{O}(n)$**.

#### 2. Busca - `consultar_registro(...)`
* **Busca por ID (Caso 3):**
  * **Melhor Caso - $\mathcal{O}(1)$:** O serviço procurado está armazenado no primeiro nó (`self.head`), retornando na primeira iteração.
  * **Caso Médio e Pior Caso - $\mathcal{O}(n)$:** O registro está na metade da lista ($n/2$ comparações), na última posição ou é inexistente, exigindo o percurso de todos os $n$ nós.
* **Busca por Título ou Categoria (Caso 2):**
  * **Todos os Casos - $\mathcal{O}(n)$:** Como múltiplos serviços podem conter o mesmo termo pesquisado (ex.: categoria `"Saúde"`), o laço não possui parada antecipada e percorre integralmente os $n$ nós da lista do início ao fim.

#### 3. Exclusão - `excluir_registro(self, id_servico)`
* **Melhor Caso - $\mathcal{O}(1)$:** O registro a ser removido é o primeiro nó da lista (`no_anterior is None`). Basta atualizar `self.head = no_atual.proximo` na primeira iteração.
* **Caso Médio e Pior Caso - $\mathcal{O}(n)$:** O código precisa localizar o nó correspondente ao `id_servico` mantendo a referência de `no_anterior`. Se o elemento estiver no final da lista ou não existir, serão necessárias $n$ iterações. A religação do ponteiro (`no_anterior.proximo = no_atual.proximo`) custa $\mathcal{O}(1)$, mantendo o custo total dominado pela busca em **$\mathcal{O}(n)$**. *(Nota: a operação `atualizar_registro` segue exatamente o mesmo comportamento, pois depende internamente de `consultar_registro(id_servico)` em $\mathcal{O}(n)$ e altera atributos em $\mathcal{O}(1)$).*

#### 4. Ordenação - `ordenar_registros(self, criterio)`
* **Melhor Caso - $\mathcal{O}(n)$:** Ocorre quando a lista já está completamente ordenada (ou possui $0$ ou $1$ elemento, caso em que é $\mathcal{O}(1)$). O laço interno executa $n - 1$ comparações na primeira passagem, nenhuma troca ocorre (`houve_troca` permanece `False`) e o laço externo é encerrado imediatamente.
* **Caso Médio e Pior Caso - $\mathcal{O}(n^2)$:** O pior caso ocorre quando a lista está ordenada de forma inversamente proporcional ao critério desejado. O algoritmo executará $n - 1$ passagens completas no laço externo, realizando $(n - 1) + (n - 2) + \dots + 1 = \frac{n(n - 1)}{2}$ comparações e trocas. Expandindo o polinômio $\frac{n^2 - n}{2}$ e descartando constantes e termos de menor ordem, a complexidade assintótica é **$\mathcal{O}(n^2)$**.