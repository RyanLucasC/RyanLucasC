<!--
  Ryan Lucas Cardoso · github.com/RyanLucasC
  Paleta (dark): fundo #0d1117 · superfície #161b22 · borda #30363d
                 texto #e6edf3 / #c9d1d9 / #8b949e · acento #ab7df8 (uso pontual)
-->

<div align="center">

<img src="assets/hero-v10.gif" width="100%" alt="Ryan Lucas Cardoso — Engenharia de Software, Dados e Inteligência Artificial"/>

<p>Estudante de Engenharia de Software na UEM, com foco em <b>Engenharia de Dados</b>, cloud e IA.<br/>Desenvolvi e coloquei em produção o ERP de frota de uma transportadora.</p>

<p>
<img src="https://img.shields.io/badge/FOCO-Engenharia_de_Dados-ab7df8?style=flat-square&labelColor=161b22" alt="Foco: Engenharia de Dados"/>
<img src="https://img.shields.io/badge/BASE-Maring%C3%A1%2C_PR-30363d?style=flat-square&labelColor=161b22&logo=googlemaps&logoColor=c9d1d9" alt="Base: Maringá, PR"/>
<img src="https://img.shields.io/badge/EST%C3%81GIO-Aberto_a_oportunidades-30363d?style=flat-square&labelColor=161b22" alt="Aberto a oportunidades de estágio"/>
<br/>
<a href="https://ryanlucascardoso.pages.dev"><img src="https://img.shields.io/badge/Portf%C3%B3lio-ryanlucascardoso.pages.dev-ab7df8?style=flat-square&labelColor=161b22&logo=cloudflare&logoColor=c9d1d9" alt="Portfólio"/></a>
<a href="https://www.linkedin.com/in/ryanlucascardoso/"><img src="https://img.shields.io/badge/LinkedIn-ryanlucascardoso-30363d?style=flat-square&labelColor=161b22&logo=linkedin&logoColor=c9d1d9" alt="LinkedIn"/></a>
</p>

<p>
<a href="#sobre">Sobre</a> &nbsp;·&nbsp;
<a href="#experiência">Experiência</a> &nbsp;·&nbsp;
<a href="#projetos">Projetos</a> &nbsp;·&nbsp;
<a href="#tech-stack">Tech Stack</a> &nbsp;·&nbsp;
<a href="#próximos-passos">Próximos passos</a> &nbsp;·&nbsp;
<a href="#contato">Contato</a>
</p>

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## Sobre

Graduando em **Engenharia de Software na UEM** (2º ano), construindo carreira em Engenharia de Dados. Gosto de levar um sistema do requisito até a produção: meu principal projeto é um ERP de frota em uso diário por um cliente real. Além do código, tenho vivência comercial e de gestão de projetos, faço iniciação científica e co-organizo uma comunidade de cloud em Maringá.

## Experiência

<table>
<tr>
<td width="240" valign="top"><b>RR Transportes e Terraplanagem</b><br/><sub>DESENVOLVEDOR</sub></td>
<td valign="top">ERP de gestão de frota, do levantamento com o gestor ao sistema em produção em VPS Linux: viagens, fretes, abastecimento, manutenção e custos. <a href="https://ryanlucascardoso.pages.dev/erp/">Ver as telas</a></td>
</tr>
<tr>
<td width="240" valign="top"><b>Main - Soluções em Software</b><br/><sub>ESTÁGIO · COMERCIAL E PROJETOS</sub></td>
<td valign="top">Área Comercial e Assistente de Projetos: prospecção, negociação de contratos, levantamento de requisitos e acompanhamento das entregas.</td>
</tr>
<tr>
<td width="240" valign="top"><b>PIBIC · UEM</b><br/><sub>INICIAÇÃO CIENTÍFICA</sub></td>
<td valign="top">Pesquisa com Teoria de Resposta ao Item (TRI) aplicada a novas áreas, com apoio de IA.</td>
</tr>
<tr>
<td width="240" valign="top"><b>Cloud Native Maringá</b><br/><sub>CO-ORGANIZADOR · CNCF</sub></td>
<td valign="top">Co-organização do capítulo local da CNCF; trouxe os eventos da comunidade para a UEM.</td>
</tr>
</table>

## Projetos

### ERP Logístico

<sub>RR TRANSPORTES E TERRAPLANAGEM &nbsp;·&nbsp; EM PRODUÇÃO</sub>

<a href="https://ryanlucascardoso.pages.dev/erp/"><img src="https://ryanlucascardoso.pages.dev/erp/visao-geral-escuro-1568.webp" width="100%" alt="Painel do gestor do ERP Logístico, com o resultado do mês (dados fictícios de demonstração)"/></a>

Sistema de gestão de frota e operação de transporte: API em FastAPI com SQLite, painel web para o gestor e app PWA para o motorista, que funciona sem sinal.

- **Operação e financeiro:** viagens com conferência do gestor, DRE, comissões e custos de combustível, manutenção e despesas com foto do recibo
- **Regra de negócio real:** frete comparado ao piso mínimo da ANTT, alertas de vencimento e de manutenção por km, com notificações push
- **Confiabilidade:** auditoria de alterações, backup diário, teste semanal de restauração, testes automatizados (pytest e Playwright) e CI no GitHub Actions
- **Segurança:** senhas com scrypt, sessões revogáveis, bloqueio por tentativas e CSP restritiva
- **Produção:** VPS Linux com nginx, HTTPS (Let's Encrypt) e serviços isolados pelo systemd

**[Ver as telas do sistema](https://ryanlucascardoso.pages.dev/erp/)** &nbsp;·&nbsp; painel do gestor e app do motorista, com dados fictícios de demonstração

<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=c9d1d9" alt="Python"/>
<img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=c9d1d9" alt="FastAPI"/>
<img src="https://img.shields.io/badge/SQLite-161b22?style=flat-square&logo=sqlite&logoColor=c9d1d9" alt="SQLite"/>
<img src="https://img.shields.io/badge/Alembic-161b22?style=flat-square" alt="Alembic"/>
<img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&logo=javascript&logoColor=c9d1d9" alt="JavaScript"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-161b22?style=flat-square&logo=tailwindcss&logoColor=c9d1d9" alt="Tailwind CSS"/>
<img src="https://img.shields.io/badge/pytest-161b22?style=flat-square&logo=pytest&logoColor=c9d1d9" alt="pytest"/>
<img src="https://img.shields.io/badge/GitHub_Actions-161b22?style=flat-square&logo=githubactions&logoColor=c9d1d9" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/nginx-161b22?style=flat-square&logo=nginx&logoColor=c9d1d9" alt="nginx"/>

### Portfólio

<sub>RESUME AS CODE &nbsp;·&nbsp; ATIVO</sub>

Site bilíngue e currículo em PDF gerados a partir de um único arquivo de dados por idioma. Atualizar o portfólio é editar esse arquivo: o build valida o conteúdo e gera todo o resto.

- Validação no build: dados pessoais, credenciais e links sem HTTPS impedem a publicação
- Currículo em PDF gerado automaticamente, com prévia sempre atualizada no site
- Sem JavaScript no site, com CSP rígida e nota 100 no Lighthouse em desempenho, acessibilidade, boas práticas e SEO

**[Ver o site](https://ryanlucascardoso.pages.dev)** &nbsp;·&nbsp; [Ver o código](https://github.com/RyanLucasC/ryanlucas-portfolio)

<img src="https://img.shields.io/badge/Astro-161b22?style=flat-square&logo=astro&logoColor=c9d1d9" alt="Astro"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-161b22?style=flat-square&logo=tailwindcss&logoColor=c9d1d9" alt="Tailwind CSS"/>
<img src="https://img.shields.io/badge/Node.js-161b22?style=flat-square&logo=nodedotjs&logoColor=c9d1d9" alt="Node.js"/>
<img src="https://img.shields.io/badge/Cloudflare_Pages-161b22?style=flat-square&logo=cloudflarepages&logoColor=c9d1d9" alt="Cloudflare Pages"/>

## Tech Stack

<table>
<tr>
<td width="170"><sub><b>LINGUAGENS</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=c9d1d9" alt="Python"/>
<img src="https://img.shields.io/badge/SQL-161b22?style=flat-square" alt="SQL"/>
<img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&logo=javascript&logoColor=c9d1d9" alt="JavaScript"/>
<img src="https://img.shields.io/badge/HTML_%2F_CSS-161b22?style=flat-square&logo=html5&logoColor=c9d1d9" alt="HTML / CSS"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>DADOS E BACKEND</b></sub></td>
<td>
<img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=c9d1d9" alt="FastAPI"/>
<img src="https://img.shields.io/badge/SQLite-161b22?style=flat-square&logo=sqlite&logoColor=c9d1d9" alt="SQLite"/>
<img src="https://img.shields.io/badge/Dashboards_web-161b22?style=flat-square" alt="Dashboards web"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>INFRA</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Linux-161b22?style=flat-square&logo=linux&logoColor=c9d1d9" alt="Linux"/>
<img src="https://img.shields.io/badge/Git-161b22?style=flat-square&logo=git&logoColor=c9d1d9" alt="Git"/>
<img src="https://img.shields.io/badge/Deploy_em_VPS-161b22?style=flat-square" alt="Deploy em VPS"/>
<img src="https://img.shields.io/badge/nginx-161b22?style=flat-square&logo=nginx&logoColor=c9d1d9" alt="nginx"/>
<img src="https://img.shields.io/badge/GitHub_Actions-161b22?style=flat-square&logo=githubactions&logoColor=c9d1d9" alt="GitHub Actions"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>WEB</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Astro-161b22?style=flat-square&logo=astro&logoColor=c9d1d9" alt="Astro"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-161b22?style=flat-square&logo=tailwindcss&logoColor=c9d1d9" alt="Tailwind CSS"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>IA</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Integra%C3%A7%C3%A3o_com_LLMs-161b22?style=flat-square" alt="Integração com LLMs"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>ESTUDANDO</b></sub></td>
<td>
<img src="https://img.shields.io/badge/AWS-161b22?style=flat-square" alt="AWS"/>
<img src="https://img.shields.io/badge/Engenharia_de_Dados-161b22?style=flat-square" alt="Engenharia de Dados"/>
</td>
</tr>
</table>

## Próximos passos

<table>
<tr><td>AWS Certified Cloud Practitioner</td><td align="right"><img src="https://img.shields.io/badge/ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22" alt="Em andamento"/></td></tr>
<tr><td>Fundamentos de IA e Machine Learning</td><td align="right"><img src="https://img.shields.io/badge/ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22" alt="Em andamento"/></td></tr>
<tr><td>Primeiros pipelines de Engenharia de Dados</td><td align="right"><img src="https://img.shields.io/badge/NA_FILA-30363d?style=flat-square&labelColor=161b22" alt="Na fila"/></td></tr>
<tr><td>Projetos open source no GitHub</td><td align="right"><img src="https://img.shields.io/badge/NA_FILA-30363d?style=flat-square&labelColor=161b22" alt="Na fila"/></td></tr>
</table>

<details>
<summary><b>Roadmap completo de certificações</b></summary>
<br/>

**Certificações-alvo (AWS)**

<table>
<tr><td><b>AWS Certified Cloud Practitioner</b></td><td align="right"><img src="https://img.shields.io/badge/%E2%97%8F_EM_ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td><b>AWS Certified AI Practitioner</b></td><td align="right"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td><b>AWS Certified Data Engineer – Associate</b></td><td align="right"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td><b>AWS Certified Solutions Architect – Associate</b></td><td align="right"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td></tr>
</table>

**Trilha de estudos**

<table>
<tr>
<td width="170" valign="top"><b>Fase 01</b><br/><sub>Linux, Cloud e IA</sub></td>
<td valign="top">LFS101 Linux · AWS Cloud Practitioner Essentials · SimuLearn Cloud Practitioner · Claude Academy</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8F_EM_ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22"/></td>
</tr>
<tr>
<td width="170" valign="top"><b>Fase 02</b><br/><sub>Fundamentos AWS</sub></td>
<td valign="top">Cloud Essentials Knowledge Badge</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td>
</tr>
<tr>
<td width="170" valign="top"><b>Fase 03</b><br/><sub>Dados</sub></td>
<td valign="top">Databricks Fundamentals · dbt Fundamentals · Cisco Data Analytics Essentials</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td>
</tr>
<tr>
<td width="170" valign="top"><b>Fase 04</b><br/><sub>Inteligência Artificial</sub></td>
<td valign="top">SimuLearn AI Practitioner · Databricks Generative AI · Databricks AI Agent</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td>
</tr>
<tr>
<td width="170" valign="top"><b>Fase 05</b><br/><sub>DevOps e Segurança</sub></td>
<td valign="top">LFS158 Kubernetes · LFS162 DevOps e SRE · Cisco Cybersecurity</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td>
</tr>
<tr>
<td width="170" valign="top"><b>Fase 06</b><br/><sub>Treino AWS</sub></td>
<td valign="top">Cloud Quest Cloud Practitioner · Cloud Quest Gen AI Practitioner</td>
<td align="right" valign="top"><img src="https://img.shields.io/badge/%E2%97%8B_NA_FILA-8b949e?style=flat-square&labelColor=161b22"/></td>
</tr>
</table>

</details>

## Contato

<div align="center">

<a href="https://ryanlucascardoso.pages.dev"><img src="https://img.shields.io/badge/Portf%C3%B3lio-ryanlucascardoso.pages.dev-ab7df8?style=for-the-badge&labelColor=161b22&logo=cloudflare&logoColor=c9d1d9" alt="Portfólio"/></a>
<a href="https://www.linkedin.com/in/ryanlucascardoso/"><img src="https://img.shields.io/badge/LinkedIn-ryanlucascardoso-30363d?style=for-the-badge&logo=linkedin&logoColor=c9d1d9&labelColor=161b22" alt="LinkedIn"/></a>
<a href="https://www.instagram.com/ryanlucas.dev/"><img src="https://img.shields.io/badge/Instagram-ryanlucas.dev-30363d?style=for-the-badge&logo=instagram&logoColor=c9d1d9&labelColor=161b22" alt="Instagram"/></a>

<sub>Aberto a oportunidades de estágio, projetos e colaborações.</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

<sub>UEM &nbsp;·&nbsp; Maringá, PR &nbsp;·&nbsp; Engenharia de Software</sub>

</div>
