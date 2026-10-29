# Changelog e Release com GitHub Actions

Trabalho 1 de DevOps Avançado — UniALFA

## Integrantes

- Mihari Barbosa da Silva (RA 260266
- Aline Eduarda Morais de Rezende (RA 250279)

## Sobre o projeto

Repositório que demonstra o uso de GitHub Actions para documentar alterações e publicar versões do projeto. Contém uma página HTML simples e duas automações independentes.

## Action de changelog (`changelog.yml`)

A cada push na branch `main`, a Action lê o histórico do Git (`git log`) e reescreve a seção de changelog deste README, listando cada commit com hash, mensagem, autor e data. A seção fica entre os marcadores `CHANGELOG:START` e `CHANGELOG:END`. Depois, a própria Action faz um commit com o README atualizado.

### Explicação do workflow — Release automática

| Nº | Trecho | O que faz |
|---|---|---|
| 1 | `name: Release` | Define o nome do workflow exibido na aba Actions do GitHub. |
| 2 | `on: push` | Configura a execução automática quando alterações são enviadas ao repositório e atendem aos filtros definidos. |
| 3 | `branches: [main]` | Restringe a execução aos pushes na branch `main`. |
| 4 | `paths-ignore: ["README.md"]` | Ignora alterações exclusivas no `README.md`. Se outros arquivos também forem modificados, o workflow poderá ser executado. |
| 5 | `permissions: contents: write` | Concede ao `GITHUB_TOKEN` permissão de escrita no conteúdo do repositório, necessária para publicar releases. |
| 6 | `jobs: release` | Define o job responsável pelo processo de publicação. |
| 7 | `runs-on: ubuntu-latest` | Executa o job em um ambiente Linux disponibilizado pelo GitHub Actions. |
| 8 | `actions/checkout@v4` | Baixa os arquivos do repositório para o ambiente de execução. |
| 9 | `Definir versao` | Gera uma versão no formato `v1.0.N`, usando `github.run_number` como número sequencial da execução. |
| 10 | `$GITHUB_ENV` | Armazena a variável `VERSION` para que ela possa ser usada pelas etapas seguintes do mesmo job. |
| 11 | `Gerar pacote` | Executa `zip -r pacote.zip .` para compactar recursivamente os arquivos do diretório atual. |
| 12 | `-x ".git/*" ".github/*"` | Exclui do pacote os diretórios `.git` e `.github`, evitando incluir o histórico Git e os arquivos dos workflows. |
| 13 | `softprops/action-gh-release@v2` | Usa uma Action externa para criar e publicar uma release no GitHub. |
| 14 | `tag_name: ${{ env.VERSION }}` | Define a tag da release com a versão gerada, como `v1.0.15`. |
| 15 | `name: ${{ env.VERSION }}` | Usa a mesma versão como nome visível da release. |
| 16 | `target_commitish: ${{ github.sha }}` | Associa a release ao commit que acionou o workflow. |
| 17 | `files: pacote.zip` | Anexa o arquivo compactado à release publicada. |
| 18 | `generate_release_notes: true` | Solicita ao GitHub a geração automática das notas da release, com base no histórico de alterações e nas configurações do repositório. |

### Pontos de atenção

- **Versionamento:** o número da execução permite gerar versões sequenciais, mas não garante que elas representem a versão real do software.
- **Tags duplicadas:** se a tag gerada já existir, a publicação poderá falhar.
- **Conteúdo do pacote:** o comando compacta os arquivos do diretório atual, exceto os padrões especificados. Outros arquivos desnecessários ou sensíveis podem ser incluídos.
- **Permissões:** `contents: write` permite operações de escrita no conteúdo do repositório, incluindo a publicação de releases.
- **Filtro do README:** evita executar o workflow quando somente a documentação é alterada.
- **Notas automáticas:** o resultado depende do histórico de commits, das tags e das configurações do repositório.

**Resultado:** a cada push elegível na branch `main`, o workflow gera uma versão, compacta os arquivos do projeto e publica uma release no GitHub com o pacote anexado e notas de versão automáticas.

## Action de release (`release.yml`)

A cada push na branch `main`, a Action gera automaticamente um número de versão (`v1.0.N`, onde N é o número da execução), cria a tag no commit da alteração, empacota o projeto em um arquivo `pacote.zip` e publica a versão na seção Releases do GitHub, com notas de versão geradas automaticamente. Não é necessário criar tags manualmente: cada alteração enviada gera uma nova versão.
### Explicação do código — Release automática no GitHub

| Nº | Trecho | O que faz |
|---|---|---|
| 1 | `name: Release` | Define o nome do workflow, exibido na aba Actions do GitHub. |
| 2 | `on: push` | Executa o workflow quando houver um push que corresponda aos filtros definidos. |
| 3 | `branches: [main]` | Executa somente para alterações enviadas à branch `main`. |
| 4 | `paths-ignore: ["README.md"]` | Ignora pushes em que as alterações são exclusivamente no `README.md`. Se outros arquivos também forem alterados, o workflow ainda pode ser executado. |
| 5 | `permissions: contents: write` | Concede ao `GITHUB_TOKEN` permissão de escrita no conteúdo do repositório, necessária para publicar a release. |
| 6 | `jobs: release` | Define o job responsável pelas etapas de publicação. |
| 7 | `runs-on: ubuntu-latest` | Executa o job em uma máquina virtual com a versão estável mais recente do Ubuntu disponibilizada pelo GitHub Actions. |
| 8 | `actions/checkout@v4` | Baixa o conteúdo do repositório para o ambiente de execução, permitindo acessar os arquivos e o commit atual. |
| 9 | `Definir versao` | Cria a variável de ambiente `VERSION` no formato `v1.0.N`, em que `N` é o número da execução do workflow (`github.run_number`). |
| 10 | `$GITHUB_ENV` | Disponibiliza a variável `VERSION` para as etapas seguintes do mesmo job. |
| 11 | `Gerar pacote` | Executa `zip -r pacote.zip .` para compactar recursivamente os arquivos do diretório atual em `pacote.zip`. |
| 12 | `-x ".git/*" ".github/*"` | Exclui do pacote as pastas `.git` e `.github`, evitando incluir o histórico Git e os arquivos de configuração dos workflows. |
| 13 | `softprops/action-gh-release@v2` | Usa uma Action externa para criar e publicar uma release no GitHub. |
| 14 | `tag_name: ${{ env.VERSION }}` | Define a tag da release com a versão gerada anteriormente, como `v1.0.15`. |
| 15 | `name: ${{ env.VERSION }}` | Usa a mesma versão como nome visível da release. |
| 16 | `target_commitish: ${{ github.sha }}` | Indica o commit associado à release, usando o hash do commit que acionou o workflow. |
| 17 | `files: pacote.zip` | Anexa o arquivo compactado à release publicada. |
| 18 | `generate_release_notes: true` | Solicita ao GitHub a geração automática das notas da release, com base no histórico de alterações e nas configurações do repositório. |

### Pontos importantes

- **Versionamento:** o número da execução gera versões sequenciais dentro do workflow, mas não representa necessariamente a versão real do software.
- **Tags existentes:** se a tag gerada já existir, a publicação pode falhar; a estratégia de versionamento deve evitar duplicações.
- **Conteúdo do pacote:** o comando compacta todos os arquivos do diretório atual, exceto os padrões indicados. Arquivos desnecessários ou sensíveis podem acabar incluídos.
- **Permissões:** `contents: write` permite que o token publique releases e faça outras operações de escrita no conteúdo do repositório.
- **README:** ignorar alterações exclusivas no README evita que atualizações da documentação acionem uma nova release desnecessariamente.
- **Notas automáticas:** `generate_release_notes: true` gera as notas a partir dos dados disponíveis no GitHub, mas a qualidade depende do histórico de commits, das tags e das configurações do repositório.

## Changelog

<!-- CHANGELOG:START -->
- `718cfac` Fix title typo in index.html — Mihari barbosa da silva (2026-10-29)
- `1407d28` Fix header formatting in README.md — Mihari barbosa da silva (2026-10-29)
- `40df7c8` Fix header formatting in README.md — Mihari barbosa da silva (2026-10-29)
- `48c02c2` Revise release Action description in README — Mihari barbosa da silva (2026-10-29)
- `e5a765a` Update release.yml — Mihari barbosa da silva (2026-10-29)
- `a3ca496` Delete .github/workflows/release1.yml — Mihari barbosa da silva (2026-10-29)
- `8d75737` Add GitHub Actions workflow for release process — Mihari barbosa da silva (2026-10-29)
- `a2fda1c` Update changelog commit message format — Mihari barbosa da silva (2026-10-25)
- `25dc75b` Add GitHub Actions workflow for release process — Mihari barbosa da silva (2026-10-25)
- `5b11532` Delete .github/workflows/.github/workflows directory — Mihari barbosa da silva (2026-10-25)
- `5ce3088` Add GitHub Actions workflow for releases — Mihari barbosa da silva (2026-10-25)
- `2f4f506` Update title in index.html for Trabalho 1 — Mihari barbosa da silva (2026-10-25)
- `c33df95` Add initial CSS styles for layout and typography — Mihari barbosa da silva (2026-10-25)
- `6f94fdc` Add initial HTML structure for DevOps Actions page — Mihari barbosa da silva (2026-10-25)
- `41f76b0` Enhance README with project information and actions — Mihari barbosa da silva (2026-10-25)
- `bd315fe` Add GitHub Actions workflow for automatic changelog — Mihari barbosa da silva (2026-10-25)
- `7e95a58` Delete .github/workflows/devops.yml — Mihari barbosa da silva (2026-10-25)
- `0c7e390` Add DevOps workflow for commits and release package — Mihari barbosa da silva (2026-10-22)
- `accd22c` Initial commit — Mihari barbosa da silva (2026-10-22)
<!-- CHANGELOG:END -->
