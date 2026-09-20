<div align="center">

# 💧 Consumo de Água – Classificador de Perfil

**Script em Python para classificar o consumo de água dos imóveis e emitir alertas educativos aos moradores.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Sustentabilidade](https://img.shields.io/badge/Meio%20Ambiente-Água%20%F0%9F%8C%8E-0077BE?style=for-the-badge)
![Licença](https://img.shields.io/badge/Uso-Educacional-orange?style=for-the-badge)

</div>

---

## 🎯 Objetivo

A companhia de saneamento da cidade lançou uma **campanha de conscientização ambiental**. Este sistema recebe o **tipo de imóvel** e o **consumo mensal de água (m³)** e exibe uma mensagem educativa de acordo com o perfil de consumo, incentivando o uso consciente da água. 🌱

## 🛠️ Tecnologias

| Ícone | Tecnologia | Uso |
|:---:|---|---|
| 🐍 | Python 3 | Linguagem do programa |
| 🐙 | Git / GitHub | Versionamento e publicação |
| 💧 | Tema: Saneamento | Conscientização ambiental |

## 📏 Regras de Negócio

| # | Condição | Mensagem exibida |
|:---:|---|---|
| 1 | Imóvel **comercial** | 🏢 *Tarifa comercial aplicada – consulte o plano corporativo.* |
| 2 | **Apartamento** com consumo **< 10 m³** | 🌿 *Consumo econômico – excelente controle de água!* |
| 3 | **Apartamento** ou **casa** com consumo **até 25 m³** | 🏠 *Consumo moderado – dentro do padrão residencial.* |
| 4 | Qualquer outro caso | 🚨 *Consumo excessivo – adote medidas de economia e verifique vazamentos.* |

> As regras são avaliadas **nessa ordem**.

## ▶️ Como executar

**Pré-requisito:** ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

# 2. Entre na pasta do projeto
cd SEU-REPOSITORIO/consumo-agua

# 3. Execute o programa
python app.py
```

## 🖥️ Exemplo de uso

```text
=======================================================
💧 CLASSIFICADOR DE CONSUMO DE ÁGUA 💧
=======================================================
Tipo de imóvel (comercial / casa / apartamento): apartamento
Consumo mensal de água (m³): 8.5

📋 Resultado da análise:
Consumo econômico – excelente controle de água!
```

## ✅ Casos de teste

| Tipo | Consumo (m³) | Resultado |
|---|:---:|---|
| comercial | 100 | Tarifa comercial aplicada |
| apartamento | 8 | Consumo econômico |
| apartamento | 18 | Consumo moderado |
| casa | 25 | Consumo moderado |
| casa | 40 | Consumo excessivo |
| apartamento | 30 | Consumo excessivo |

## 📁 Estrutura

```text
consumo-agua/
├── app.py       # Código-fonte do programa
└── README.md    # Documentação do projeto
```

## 👩‍💻 Autor

Desenvolvido por **SEU NOME** como atividade da Agenda 7 – Desenvolvimento de Sistemas.

<div align="center">💙 Cada gota conta! Use a água com consciência. 💙</div>
