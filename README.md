# Changelog e Release com GitHub Actions

Trabalho 1 de DevOps Avançado — UniALFA

## Integrantes

- Mihari Barbosa da Silva (RA 260266
- Aline Eduarda Morais de Rezende (RA 250279)

## Sobre o projeto

Repositório que demonstra o uso de GitHub Actions para documentar alterações e publicar versões do projeto. Contém uma página HTML simples e duas automações independentes.

## Action de changelog (`changelog.yml`)

A cada push na branch `main`, a Action lê o histórico do Git (`git log`) e reescreve a seção de changelog deste README, listando cada commit com hash, mensagem, autor e data. A seção fica entre os marcadores `CHANGELOG:START` e `CHANGELOG:END`. Depois, a própria Action faz um commit com o README atualizado.

## Action de release (`release.yml`)

Quando uma tag de versão (por exemplo `v1.0.0`) é enviada ao repositório, a Action gera um arquivo `pacote.zip` com o conteúdo do projeto e o publica na seção Releases do GitHub, com notas de versão geradas automaticamente. Para publicar uma versão: `git tag v1.0.0 && git push origin v1.0.0`, ou criar a tag pelo site do GitHub.

## Changelog

<!-- CHANGELOG:START -->
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
