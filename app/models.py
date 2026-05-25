from django.db import models


class Produtor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do produtor")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produtor"
        verbose_name_plural = "Produtores"


class Propriedade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da propriedade")
    localizacao = models.CharField(max_length=200, verbose_name="Localização")
    tamanho_area = models.FloatField(verbose_name="Tamanho da área")
    produtor = models.ForeignKey(
        Produtor,
        on_delete=models.CASCADE,
        verbose_name="Produtor"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Propriedade"
        verbose_name_plural = "Propriedades"


class Safra(models.Model):
    ano = models.IntegerField(verbose_name="Ano da safra")
    produtividade = models.FloatField(verbose_name="Produtividade")
    area_plantada = models.FloatField(verbose_name="Área plantada")
    propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        verbose_name="Propriedade"
    )

    def __str__(self):
        return f"Safra {self.ano}"

    class Meta:
        verbose_name = "Safra"
        verbose_name_plural = "Safras"


class TipoCusto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de custo")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de custo"
        verbose_name_plural = "Tipos de custos"


class CustoProducao(models.Model):
    tipo = models.ForeignKey(
        TipoCusto,
        on_delete=models.CASCADE,
        verbose_name="Tipo de custo"
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Valor")
    data = models.DateField(verbose_name="Data")
    safra = models.ForeignKey(
        Safra,
        on_delete=models.CASCADE,
        verbose_name="Safra"
    )

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor}"

    class Meta:
        verbose_name = "Custo de produção"
        verbose_name_plural = "Custos de produção"


class Insumo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do insumo")
    custo_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Custo unitário"
    )
    quantidade = models.IntegerField(verbose_name="Quantidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"


class DadoClimatico(models.Model):
    temperatura = models.FloatField(verbose_name="Temperatura")
    chuva = models.FloatField(verbose_name="Quantidade de chuva")
    data = models.DateField(verbose_name="Data")
    propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        verbose_name="Propriedade"
    )

    def __str__(self):
        return f"{self.data} - {self.temperatura}°C"

    class Meta:
        verbose_name = "Dado climático"
        verbose_name_plural = "Dados climáticos"


class PrecoCafe(models.Model):
    valor_saca = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor da saca"
    )
    data = models.DateField(verbose_name="Data")
    mercado = models.CharField(max_length=100, verbose_name="Mercado")

    def __str__(self):
        return f"R$ {self.valor_saca}"

    class Meta:
        verbose_name = "Preço do café"
        verbose_name_plural = "Preços do café"


class ProjecaoLucro(models.Model):
    custo_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Custo total"
    )
    receita_estimada = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Receita estimada"
    )
    lucro_estimado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Lucro estimado"
    )
    safra = models.ForeignKey(
        Safra,
        on_delete=models.CASCADE,
        verbose_name="Safra"
    )

    def __str__(self):
        return f"Lucro estimado: R$ {self.lucro_estimado}"

    class Meta:
        verbose_name = "Projeção de lucro"
        verbose_name_plural = "Projeções de lucro"


class Cenario(models.Model):
    TIPO_CENARIO = (
        ("Otimista", "Otimista"),
        ("Realista", "Realista"),
        ("Pessimista", "Pessimista"),
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CENARIO,
        verbose_name="Tipo de cenário"
    )

    projecao_lucro = models.ForeignKey(
        ProjecaoLucro,
        on_delete=models.CASCADE,
        verbose_name="Projeção de lucro"
    )

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Cenário"
        verbose_name_plural = "Cenários"


class Relatorio(models.Model):
    data_geracao = models.DateField(verbose_name="Data de geração")
    descricao = models.TextField(verbose_name="Descrição")
    propriedade = models.ForeignKey(
        Propriedade,
        on_delete=models.CASCADE,
        verbose_name="Propriedade"
    )

    def __str__(self):
        return f"Relatório {self.data_geracao}"

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"


class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class HistoricoAnalise(models.Model):
    data = models.DateField(verbose_name="Data")
    resultado = models.TextField(verbose_name="Resultado")
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return f"Análise {self.data}"

    class Meta:
        verbose_name = "Histórico de análise"
        verbose_name_plural = "Históricos de análises"


class Produtividade(models.Model):
    quantidade_colhida = models.FloatField(
        verbose_name="Quantidade colhida"
    )
    area = models.FloatField(verbose_name="Área")
    safra = models.ForeignKey(
        Safra,
        on_delete=models.CASCADE,
        related_name="produtividades",
        verbose_name="Safra"
)
    def __str__(self):
        return f"{self.quantidade_colhida} sacas"

    class Meta:
        verbose_name = "Produtividade"
        verbose_name_plural = "Produtividades"


class IndicadorEconomico(models.Model):
    nome = models.CharField(max_length=100,
                            verbose_name="Nome do indicador")

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor"
    )

    data = models.DateField(verbose_name="Data")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Indicador econômico"
        verbose_name_plural = "Indicadores econômicos"

