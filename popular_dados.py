from app.models import *


# ==========================================
# LIMPAR DADOS ANTIGOS
# ==========================================

HistoricoAnalise.objects.all().delete()
IndicadorEconomico.objects.all().delete()
Produtividade.objects.all().delete()
Relatorio.objects.all().delete()
Cenario.objects.all().delete()
ProjecaoLucro.objects.all().delete()
PrecoCafe.objects.all().delete()
DadoClimatico.objects.all().delete()
Insumo.objects.all().delete()
CustoProducao.objects.all().delete()
TipoCusto.objects.all().delete()
Safra.objects.all().delete()
Propriedade.objects.all().delete()
Usuario.objects.all().delete()
Produtor.objects.all().delete()


# ==========================================
# PRODUTOR
# ==========================================

p1 = Produtor.objects.create(
    nome="João Carlos Silva",
    cpf="12345678901",
    email="joao@josif.com",
    telefone="35999990001"
)

p2 = Produtor.objects.create(
    nome="Marcos Oliveira",
    cpf="12345678902",
    email="marcos@josif.com",
    telefone="35999990002"
)

p3 = Produtor.objects.create(
    nome="Fernanda Souza",
    cpf="12345678903",
    email="fernanda@josif.com",
    telefone="35999990003"
)

p4 = Produtor.objects.create(
    nome="Ricardo Almeida",
    cpf="12345678904",
    email="ricardo@josif.com",
    telefone="35999990004"
)

p5 = Produtor.objects.create(
    nome="Patrícia Gomes",
    cpf="12345678905",
    email="patricia@josif.com",
    telefone="35999990005"
)


# ==========================================
# PROPRIEDADE
# ==========================================

prop1 = Propriedade.objects.create(
    nome="Fazenda Boa Esperança",
    localizacao="Muzambinho - MG",
    tamanho_area=120.5,
    produtor=p1
)

prop2 = Propriedade.objects.create(
    nome="Sítio Santa Clara",
    localizacao="Guaxupé - MG",
    tamanho_area=80.0,
    produtor=p2
)

prop3 = Propriedade.objects.create(
    nome="Fazenda Ouro Verde",
    localizacao="Alfenas - MG",
    tamanho_area=150.2,
    produtor=p3
)

prop4 = Propriedade.objects.create(
    nome="Sítio Monte Alto",
    localizacao="Juruaia - MG",
    tamanho_area=65.7,
    produtor=p4
)

prop5 = Propriedade.objects.create(
    nome="Fazenda Primavera",
    localizacao="Cabo Verde - MG",
    tamanho_area=210.9,
    produtor=p5
)


# ==========================================
# SAFRA
# ==========================================

s1 = Safra.objects.create(
    ano=2024,
    produtividade=320,
    area_plantada=100,
    propriedade=prop1
)

s2 = Safra.objects.create(
    ano=2024,
    produtividade=250,
    area_plantada=70,
    propriedade=prop2
)

s3 = Safra.objects.create(
    ano=2025,
    produtividade=410,
    area_plantada=140,
    propriedade=prop3
)

s4 = Safra.objects.create(
    ano=2025,
    produtividade=190,
    area_plantada=50,
    propriedade=prop4
)

s5 = Safra.objects.create(
    ano=2024,
    produtividade=520,
    area_plantada=180,
    propriedade=prop5
)


# ==========================================
# TIPO CUSTO
# ==========================================

t1 = TipoCusto.objects.create(nome="Mão de obra")
t2 = TipoCusto.objects.create(nome="Insumos")
t3 = TipoCusto.objects.create(nome="Logística")
t4 = TipoCusto.objects.create(nome="Maquinário")
t5 = TipoCusto.objects.create(nome="Irrigação")


# ==========================================
# CUSTO PRODUÇÃO
# ==========================================

CustoProducao.objects.create(
    tipo=t1,
    valor=15000,
    data="2025-01-10",
    safra=s1
)

CustoProducao.objects.create(
    tipo=t2,
    valor=12000,
    data="2025-01-15",
    safra=s2
)

CustoProducao.objects.create(
    tipo=t3,
    valor=8000,
    data="2025-02-01",
    safra=s3
)

CustoProducao.objects.create(
    tipo=t4,
    valor=22000,
    data="2025-02-18",
    safra=s4
)

CustoProducao.objects.create(
    tipo=t5,
    valor=18000,
    data="2025-03-02",
    safra=s5
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
    propriedade=prop1
)

DadoClimatico.objects.create(
    temperatura=25,
    chuva=20,
    data="2025-01-08",
    propriedade=prop2
)

DadoClimatico.objects.create(
    temperatura=30,
    chuva=5,
    data="2025-01-11",
    propriedade=prop3
)

DadoClimatico.objects.create(
    temperatura=22,
    chuva=35,
    data="2025-01-13",
    propriedade=prop4
)

DadoClimatico.objects.create(
    temperatura=27,
    chuva=18,
    data="2025-01-16",
    propriedade=prop5
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
    mercado="Cooperativa Sul Mineira"
)

PrecoCafe.objects.create(
    valor_saca=1085,
    data="2025-02-15",
    mercado="Bolsa Internacional"
)


# ==========================================
# PROJEÇÃO LUCRO
# ==========================================

pl1 = ProjecaoLucro.objects.create(
    custo_total=50000,
    receita_estimada=85000,
    lucro_estimado=35000,
    safra=s1
)

pl2 = ProjecaoLucro.objects.create(
    custo_total=42000,
    receita_estimada=70000,
    lucro_estimado=28000,
    safra=s2
)

pl3 = ProjecaoLucro.objects.create(
    custo_total=63000,
    receita_estimada=110000,
    lucro_estimado=47000,
    safra=s3
)

pl4 = ProjecaoLucro.objects.create(
    custo_total=39000,
    receita_estimada=62000,
    lucro_estimado=23000,
    safra=s4
)

pl5 = ProjecaoLucro.objects.create(
    custo_total=90000,
    receita_estimada=150000,
    lucro_estimado=60000,
    safra=s5
)


# ==========================================
# CENÁRIO
# ==========================================

Cenario.objects.create(
    tipo="Otimista",
    projecao_lucro=pl1
)

Cenario.objects.create(
    tipo="Realista",
    projecao_lucro=pl2
)

Cenario.objects.create(
    tipo="Pessimista",
    projecao_lucro=pl3
)

Cenario.objects.create(
    tipo="Otimista",
    projecao_lucro=pl4
)

Cenario.objects.create(
    tipo="Realista",
    projecao_lucro=pl5
)


# ==========================================
# RELATÓRIO
# ==========================================

Relatorio.objects.create(
    data_geracao="2025-03-01",
    descricao="Relatório financeiro trimestral",
    propriedade=prop1
)

Relatorio.objects.create(
    data_geracao="2025-03-02",
    descricao="Análise climática da safra",
    propriedade=prop2
)

Relatorio.objects.create(
    data_geracao="2025-03-03",
    descricao="Relatório de produtividade",
    propriedade=prop3
)

Relatorio.objects.create(
    data_geracao="2025-03-04",
    descricao="Relatório de custos",
    propriedade=prop4
)

Relatorio.objects.create(
    data_geracao="2025-03-05",
    descricao="Relatório anual completo",
    propriedade=prop5
)


# ==========================================
# USUÁRIO
# ==========================================

u1 = Usuario.objects.create(
    nome="Administrador",
    email="admin@josif.com",
    senha="123456"
)

u2 = Usuario.objects.create(
    nome="Carlos Mendes",
    email="carlos@josif.com",
    senha="123456"
)

u3 = Usuario.objects.create(
    nome="Juliana Rocha",
    email="juliana@josif.com",
    senha="123456"
)

u4 = Usuario.objects.create(
    nome="Ana Paula",
    email="ana@josif.com",
    senha="123456"
)

u5 = Usuario.objects.create(
    nome="Rafael Costa",
    email="rafael@josif.com",
    senha="123456"
)


# ==========================================
# HISTÓRICO ANÁLISE
# ==========================================

HistoricoAnalise.objects.create(
    data="2025-04-01",
    resultado="Foi identificado aumento da rentabilidade nas propriedades com irrigação automatizada.",
    usuario=u1
)

HistoricoAnalise.objects.create(
    data="2025-04-02",
    resultado="A produtividade apresentou queda devido à baixa incidência de chuvas.",
    usuario=u2
)

HistoricoAnalise.objects.create(
    data="2025-04-03",
    resultado="Os custos com fertilizantes aumentaram 12% em relação ao mês anterior.",
    usuario=u3
)

HistoricoAnalise.objects.create(
    data="2025-04-04",
    resultado="Foi detectada melhora significativa na produtividade da safra 2025.",
    usuario=u4
)

HistoricoAnalise.objects.create(
    data="2025-04-05",
    resultado="O cenário otimista apresentou maior margem de lucro estimada.",
    usuario=u5
)


# ==========================================
# PRODUTIVIDADE
# ==========================================

Produtividade.objects.create(
    quantidade_colhida=350,
    area=100,
    safra=s1
)

Produtividade.objects.create(
    quantidade_colhida=280,
    area=70,
    safra=s2
)

Produtividade.objects.create(
    quantidade_colhida=450,
    area=140,
    safra=s3
)

Produtividade.objects.create(
    quantidade_colhida=210,
    area=50,
    safra=s4
)

Produtividade.objects.create(
    quantidade_colhida=600,
    area=180,
    safra=s5
)


# ==========================================
# INDICADOR ECONÔMICO
# ==========================================

IndicadorEconomico.objects.create(
    nome="Inflação Agrícola",
    valor=5.20,
    data="2025-03-01"
)

IndicadorEconomico.objects.create(
    nome="Cotação do Café",
    valor=1085.00,
    data="2025-03-02"
)

IndicadorEconomico.objects.create(
    nome="Taxa Selic",
    valor=10.75,
    data="2025-03-03"
)

IndicadorEconomico.objects.create(
    nome="Custo Médio de Produção",
    valor=42000.00,
    data="2025-03-04"
)

IndicadorEconomico.objects.create(
    nome="Preço Médio da Saca",
    valor=1020.00,
    data="2025-03-05"
)


print("Dados inseridos com sucesso!")