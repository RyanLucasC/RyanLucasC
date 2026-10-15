# Salve este arquivo em: .github/workflows/snake.yml
# (dentro do repositório SEU_USUARIO/SEU_USUARIO)

name: Generate Snake Animation

on:
  schedule:
    - cron: "0 */12 * * *"   # atualiza a cada 12 horas
  workflow_dispatch:          # permite rodar manualmente
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Generate snake SVGs
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark&color_snake=#00f0ff&color_dots=#0a0f1f,#0d3b4f,#007a8a,#00b8cc,#00f0ff

      - name: Push to output branch
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
