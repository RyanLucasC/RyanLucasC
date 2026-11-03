<!--
  Ryan Lucas Cardoso · github.com/RyanLucasC
  Paleta (dark): fundo #0d1117 · superfície #161b22 · borda #30363d
                 texto #e6edf3 / #c9d1d9 / #8b949e · acento #ab7df8 (uso pontual)
-->

<div align="center">

<img src="assets/hero-v7.gif" width="100%" alt="Ryan Lucas Cardoso — Engenharia de Software, Dados e Inteligência Artificial"/>

<p>Estudante de Engenharia de Software na UEM, construindo carreira em <b>Engenharia de Dados</b>.</p>

<p>
<img src="https://img.shields.io/badge/FOCO-Engenharia_de_Dados-ab7df8?style=flat-square&labelColor=161b22"/>
<img src="https://img.shields.io/badge/BASE-Maring%C3%A1%2C_PR-30363d?style=flat-square&labelColor=161b22&logo=googlemaps&logoColor=c9d1d9"/>
<a href="https://www.linkedin.com/in/ryanlucascardoso/"><img src="https://img.shields.io/badge/LinkedIn-ryanlucascardoso-30363d?style=flat-square&labelColor=161b22&logo=linkedin&logoColor=c9d1d9"/></a>
<a href="https://ryanlucascardoso.pages.dev"><img src="https://img.shields.io/badge/Portf%C3%B3lio-ryanlucascardoso.pages.dev-ab7df8?style=flat-square&labelColor=161b22&logo=cloudflare&logoColor=c9d1d9" alt="Portfólio"/></a>
</p>

<p>
<a href="#sobre">Sobre</a> &nbsp;·&nbsp;
<a href="#tech-stack">Tech Stack</a> &nbsp;·&nbsp;
<a href="#projetos">Projetos</a> &nbsp;·&nbsp;
<a href="#objetivos-2027">Objetivos</a> &nbsp;·&nbsp;
<a href="#roadmap-de-certificações">Certificações</a> &nbsp;·&nbsp;
<a href="#estatísticas">Estatísticas</a> &nbsp;·&nbsp;
<a href="#contato">Contato</a>
</p>

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## Sobre

Graduando em **Engenharia de Software na UEM**, com foco no desenvolvimento de soluções de software e na análise de dados. Uno a visão técnica da tecnologia à aplicação prática em negócios e gestão de projetos.

Na **MAIN Empresa Júnior**, atuo na área Comercial e como Assistente de Projetos, cobrindo o ciclo de um serviço de tecnologia: da prospecção e negociação de contratos ao levantamento de requisitos e ao acompanhamento da entrega.

Na **RR Transportes e Terraplanagem**, aplico design de software e arquitetura web em sistemas internos e dashboards de gestão para fretes, abastecimento e custos operacionais.

Busco desafios que exijam pensamento analítico e conectem tecnologia a resultados reais.

## Tech Stack

<table>
<tr>
<td width="170"><sub><b>LINGUAGENS</b></sub></td>
<td>
<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&logo=javascript&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/C-161b22?style=flat-square&logo=c&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/HTML_%2F_CSS-161b22?style=flat-square&logo=html5&logoColor=c9d1d9"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>DADOS E BACKEND</b></sub></td>
<td>
<img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/SQLite-161b22?style=flat-square&logo=sqlite&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/PostgreSQL-161b22?style=flat-square&logo=postgresql&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Data_Engineering-161b22?style=flat-square&logo=apacheairflow&logoColor=c9d1d9"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>WEB E DESIGN</b></sub></td>
<td>
<img src="https://img.shields.io/badge/React-161b22?style=flat-square&logo=react&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-161b22?style=flat-square&logo=tailwindcss&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Figma-161b22?style=flat-square&logo=figma&logoColor=c9d1d9"/>
</td>
</tr>
<tr>
<td width="170"><sub><b>CLOUD E FERRAMENTAS</b></sub></td>
<td>
<img src="https://img.shields.io/badge/AWS-161b22?style=flat-square&logo=amazonwebservices&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Linux-161b22?style=flat-square&logo=linux&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Git-161b22?style=flat-square&logo=git&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/GitHub-161b22?style=flat-square&logo=github&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Claude_AI-161b22?style=flat-square&logo=anthropic&logoColor=c9d1d9"/>
</td>
</tr>
</table>

## Projetos

<table>
<tr>
<td width="50%" valign="top">

**ERP Logístico**
<br/><sub>RR TRANSPORTES E TERRAPLANAGEM</sub>

Sistema de gestão de frota e operação de transporte: API em FastAPI com SQLite e migrações, painel web para o gestor e app PWA para o motorista, que funciona sem sinal.

- Viagens com conferência do gestor, DRE, comissões e custos de combustível, manutenção e gastos avulsos com foto de recibo
- Frete comparado ao piso mínimo da ANTT, com tabelas versionadas e atualizadas pela calculadora oficial
- Alertas de vencimento e de manutenção por km, com notificações push
- Auditoria de alterações, backup diário cifrado e teste semanal de restauração
- Segurança: senhas com scrypt, sessões revogáveis, bloqueio por tentativas e CSP restritiva
- Testes automatizados (pytest e Playwright) e CI no GitHub Actions, com verificação de dependências
- Em produção em VPS Linux, com Caddy (HTTPS) e systemd

<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/FastAPI-161b22?style=flat-square&logo=fastapi&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/SQLite-161b22?style=flat-square&logo=sqlite&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Alembic-161b22?style=flat-square"/>
<img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&logo=javascript&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-161b22?style=flat-square&logo=tailwindcss&logoColor=c9d1d9"/>
<br/>
<img src="https://img.shields.io/badge/%E2%97%8F_CONCLU%C3%8DDO-ab7df8?style=flat-square&labelColor=161b22"/>

</td>
<td width="50%" valign="top">

**MAIN Empresa Júnior**
<br/><sub>COMERCIAL E PROJETOS · UEM</sub>

Atuação dupla na área Comercial e como Assistente de Projetos, cobrindo o ciclo de um serviço de tecnologia, da prospecção à entrega.

- Prospecção de clientes e negociação de contratos
- Levantamento e estruturação de requisitos
- Planejamento e acompanhamento da execução dos projetos

<img src="https://img.shields.io/badge/Gest%C3%A3o_de_projetos-161b22?style=flat-square"/>
<img src="https://img.shields.io/badge/Comercial-161b22?style=flat-square"/>
<img src="https://img.shields.io/badge/Prospec%C3%A7%C3%A3o-161b22?style=flat-square"/>
<img src="https://img.shields.io/badge/Negocia%C3%A7%C3%A3o-161b22?style=flat-square"/>
<img src="https://img.shields.io/badge/Requisitos-161b22?style=flat-square"/>
<br/>
<img src="https://img.shields.io/badge/%E2%97%8F_ATIVO-ab7df8?style=flat-square&labelColor=161b22"/>

</td>
</tr>
<tr>
<td colspan="2" valign="top">

**Próximos projetos**
<br/><sub>EM PREPARAÇÃO</sub>

Pipelines de dados, IA aplicada e cloud na AWS. Os repositórios públicos serão listados aqui conforme forem publicados.

<img src="https://img.shields.io/badge/AWS-161b22?style=flat-square&logo=amazonwebservices&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&logo=python&logoColor=c9d1d9"/>
<img src="https://img.shields.io/badge/HTML_%C2%B7_CSS_%C2%B7_JS-161b22?style=flat-square&logo=javascript&logoColor=c9d1d9"/>
<br/>
<img src="https://img.shields.io/badge/%E2%97%8B_EM_BREVE-8b949e?style=flat-square&labelColor=161b22"/>

</td>
</tr>
</table>

## Objetivos 2027

<table>
<tr><td>Colocar o ERP logístico da RR Transportes em produção</td><td align="right"><img src="https://img.shields.io/badge/CONCLU%C3%8DDO-ab7df8?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td>Certificação AWS Cloud Practitioner</td><td align="right"><img src="https://img.shields.io/badge/ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td>Fundamentos de IA e Machine Learning</td><td align="right"><img src="https://img.shields.io/badge/ANDAMENTO-c9d1d9?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td>Primeiros pipelines de Engenharia de Dados</td><td align="right"><img src="https://img.shields.io/badge/NA_FILA-30363d?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td>Comunidade tech de cloud na UEM</td><td align="right"><img src="https://img.shields.io/badge/NA_FILA-30363d?style=flat-square&labelColor=161b22"/></td></tr>
<tr><td>Projetos open source no GitHub</td><td align="right"><img src="https://img.shields.io/badge/NA_FILA-30363d?style=flat-square&labelColor=161b22"/></td></tr>
</table>

## Roadmap de certificações

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

## Estatísticas

<div align="center">

<img width="340" src="cards/stats.svg" alt="Estatísticas do GitHub"/>

</div>

## Contato

<div align="center">

<a href="https://ryanlucascardoso.pages.dev"><img src="https://img.shields.io/badge/Portf%C3%B3lio-ryanlucascardoso.pages.dev-ab7df8?style=for-the-badge&labelColor=161b22&logo=cloudflare&logoColor=c9d1d9" alt="Portfólio"/></a>
<a href="https://www.linkedin.com/in/ryanlucascardoso/"><img src="https://img.shields.io/badge/LinkedIn-ryanlucascardoso-30363d?style=for-the-badge&logo=linkedin&logoColor=c9d1d9&labelColor=161b22"/></a>
<a href="https://github.com/RyanLucasC"><img src="https://img.shields.io/badge/GitHub-RyanLucasC-30363d?style=for-the-badge&logo=github&logoColor=c9d1d9&labelColor=161b22"/></a>

<sub>Aberto a projetos, estágios e colaborações.</sub>

<img src="assets/divider.svg" width="100%" alt=""/>

<sub>UEM &nbsp;·&nbsp; Maringá, PR &nbsp;·&nbsp; Engenharia de Software</sub>

</div>
