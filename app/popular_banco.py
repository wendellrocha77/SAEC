from app.models import *

# ==========================================
# PRODUTOR
# ==========================================

Produtor.objects.create(
    nome="João Carlos Silva",
    cpf="12345678901",
    email="joao@josif.com",
    telefone="35999990001"
)

Produtor.objects.create(
    nome="Marcos Oliveira",
    cpf="12345678902",
    email="marcos@josif.com",
    telefone="35999990002"
)

Produtor.objects.create(
    nome="Fernanda Souza",
    cpf="12345678903",
    email="fernanda@josif.com",
    telefone="35999990003"
)

Produtor.objects.create(
    nome="Ricardo Almeida",
    cpf="12345678904",
    email="ricardo@josif.com",
    telefone="35999990004"
)

Produtor.objects.create(
    nome="Patrícia Gomes",
    cpf="12345678905",
    email="patricia@josif.com",
    telefone="35999990005"
)


# ==========================================
# PROPRIEDADE
# ==========================================

Propriedade.objects.create(
    nome="Fazenda Boa Esperança",
    localizacao="Muzambinho - MG",
    tamanho_area=120.5,
    produtor_id=1
)

Propriedade.objects.create(
    nome="Sítio Santa Clara",
    localizacao="Guaxupé - MG",
    tamanho_area=80.0,
    produtor_id=2
)

Propriedade.objects.create(
    nome="Fazenda Ouro Verde",
    localizacao="Alfenas - MG",
    tamanho_area=150.2,
    produtor_id=3
)

Propriedade.objects.create(
    nome="Sítio Monte Alto",
    localizacao="Juruaia - MG",
    tamanho_area=65.7,
    produtor_id=4
)

Propriedade.objects.create(
    nome="Fazenda Primavera",
    localizacao="Cabo Verde - MG",
    tamanho_area=210.9,
    produtor_id=5
)


# ==========================================
# SAFRA
# ==========================================

Safra.objects.create(
    ano=2024,
    produtividade=320,
    area_plantada=100,
    propriedade_id=1
)

Safra.objects.create(
    ano=2024,
    produtividade=250,
    area_plantada=70,
    propriedade_id=2
)

Safra.objects.create(
    ano=2025,
    produtividade=410,
    area_plantada=140,
    propriedade_id=3
)

Safra.objects.create(
    ano=2025,
    produtividade=190,
    area_plantada=50,
    propriedade_id=4
)

Safra.objects.create(
    ano=2024,
    produtividade=520,
    area_plantada=180,
    propriedade_id=5
)


# ==========================================
# TIPO CUSTO
# ==========================================

TipoCusto.objects.create(nome="Mão de obra")
TipoCusto.objects.create(nome="Insumos")
TipoCusto.objects.create(nome="Logística")
TipoCusto.objects.create(nome="Maquinário")
TipoCusto.objects.create(nome="Irrigação")


# ==========================================
# CUSTO PRODUÇÃO
# ==========================================

CustoProducao.objects.create(
    tipo_id=1,
    valor=15000,
    data="2025-01-10",
    safra_id=1
)

CustoProducao.objects.create(
    tipo_id=2,
    valor=12000,
    data="2025-01-15",
    safra_id=2
)

CustoProducao.objects.create(
    tipo_id=3,
    valor=8000,
    data="2025-02-01",
    safra_id=3
)

CustoProducao.objects.create(
    tipo_id=4,
    valor=22000,
    data="2025-02-18",
    safra_id=4
)

CustoProducao.objects.create(
    tipo_id=5,
    valor=18000,
    data="2025-03-02",
    safra_id=5
)


# ==========================================
# INSUMO
# ==========================================

Insumo.objects.create(
    nome="Fertilizante NPK",
    custo_unitario=250,
    quantidade=50
)

Insumo.objects.create(
    nome="Herbicida Premium",
    custo_unitario=180,
    quantidade=30
)

Insumo.objects.create(
    nome="Calcário Agrícola",
    custo_unitario=90,
    quantidade=100
)

Insumo.objects.create(
    nome="Adubo Orgânico",
    custo_unitario=140,
    quantidade=45
)

Insumo.objects.create(
    nome="Inseticida Café Forte",
    custo_unitario=210,
    quantidade=25
)


# ==========================================
# DADO CLIMÁTICO
# ==========================================

DadoClimatico.objects.create(
    temperatura=28,
    chuva=12,
    data="2025-01-05",
    propriedade_id=1
)

DadoClimatico.objects.create(
    temperatura=25,
    chuva=20,
    data="2025-01-08",
    propriedade_id=2
)

DadoClimatico.objects.create(
    temperatura=30,
    chuva=5,
    data="2025-01-11",
    propriedade_id=3
)

DadoClimatico.objects.create(
    temperatura=22,
    chuva=35,
    data="2025-01-13",
    propriedade_id=4
)

DadoClimatico.objects.create(
    temperatura=27,
    chuva=18,
    data="2025-01-16",
    propriedade_id=5
)


# ==========================================
# PREÇO CAFÉ
# ==========================================

PrecoCafe.objects.create(
    valor_saca=980,
    data="2025-01-01",
    mercado="Cooxupé"
)

PrecoCafe.objects.create(
    valor_saca=1020,
    data="2025-01-10",
    mercado="BM&F"
)

PrecoCafe.objects.create(
    valor_saca=995,
    data="2025-01-20",
    mercado="Mercado Livre Café"
)

PrecoCafe.objects.create(
    valor_saca=1100,
    data="2025-02-01",
    mercado="Cooperativa SulMineira"
)

PrecoCafe.objects.create(
    valor_saca=1085,
    data="2025-02-15",
    mercado="Bolsa Internacional"
)


# ==========================================
# PROJEÇÃO LUCRO
# ==========================================

ProjecaoLucro.objects.create(
    custo_total=50000,
    receita_estimada=85000,
    lucro_estimado=35000,
    safra_id=1
)

ProjecaoLucro.objects.create(
    custo_total=42000,
    receita_estimada=70000,
    lucro_estimado=28000,
    safra_id=2
)

ProjecaoLucro.objects.create(
    custo_total=63000,
    receita_estimada=110000,
    lucro_estimado=47000,
    safra_id=3
)

ProjecaoLucro.objects.create(
    custo_total=39000,
    receita_estimada=62000,
    lucro_estimado=23000,
    safra_id=4
)

ProjecaoLucro.objects.create(
    custo_total=90000,
    receita_estimada=150000,
    lucro_estimado=60000,
    safra_id=5
)


# ==========================================
# CENÁRIO
# ==========================================

Cenario.objects.create(
    tipo="Otimista",
    projecao_lucro_id=1
)

Cenario.objects.create(
    tipo="Realista",
    projecao_lucro_id=2
)

Cenario.objects.create(
    tipo="Pessimista",
    projecao_lucro_id=3
)

Cenario.objects.create(
    tipo="Otimista",
    projecao_lucro_id=4
)

Cenario.objects.create(
    tipo="Realista",
    projecao_lucro_id=5
)


# ==========================================
# RELATÓRIO
# ==========================================

Relatorio.objects.create(
    data_geracao="2025-03-01",
    descricao="Relatório financeiro trimestral",
    propriedade_id=1
)

Relatorio.objects.create(
    data_geracao="2025-03-02",
    descricao="Análise climática da safra",
    propriedade_id=2
)

Relatorio.objects.create(
    data_geracao="2025-03-03",
    descricao="Relatório de produtividade",
    propriedade_id=3
)

Relatorio.objects.create(
    data_geracao="2025-03-04",
    descricao="Relatório de custos",
    propriedade_id=4
)

Relatorio.objects.create(
    data_geracao="2025-03-05",
    descricao="Relatório anual completo",
    propriedade_id=5
)