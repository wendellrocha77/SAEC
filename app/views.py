from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View


# ==========================================
# INDEX
# ==========================================

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# ==========================================
# PRODUTOR
# ==========================================

class ProdutoresView(View):

    def get(self, request, *args, **kwargs):

        produtores = Produtor.objects.all()

        return render(
            request,
            'produtor.html',
            {'produtores': produtores}
        )


# ==========================================
# PROPRIEDADE
# ==========================================

class PropriedadesView(View):

    def get(self, request, *args, **kwargs):

        propriedades = Propriedade.objects.all()

        return render(
            request,
            'propriedade.html',
            {'propriedades': propriedades}
        )


# ==========================================
# SAFRA
# ==========================================

class SafrasView(View):

    def get(self, request, *args, **kwargs):

        safras = Safra.objects.all()

        return render(
            request,
            'safra.html',
            {'safras': safras}
        )


# ==========================================
# TIPO CUSTO
# ==========================================

class TiposCustoView(View):

    def get(self, request, *args, **kwargs):

        tipos_custo = TipoCusto.objects.all()

        return render(
            request,
            'tipocusto.html',
            {'tipos_custo': tipos_custo}
        )


# ==========================================
# CUSTO PRODUÇÃO
# ==========================================

class CustosProducaoView(View):

    def get(self, request, *args, **kwargs):

        custos = CustoProducao.objects.all()

        return render(
            request,
            'custoproducao.html',
            {'custos': custos}
        )


# ==========================================
# INSUMO
# ==========================================

class InsumosView(View):

    def get(self, request, *args, **kwargs):

        insumos = Insumo.objects.all()

        return render(
            request,
            'insumo.html',
            {'insumos': insumos}
        )


# ==========================================
# DADO CLIMÁTICO
# ==========================================

class DadosClimaticosView(View):

    def get(self, request, *args, **kwargs):

        dados_climaticos = DadoClimatico.objects.all()

        return render(
            request,
            'dadoclimatico.html',
            {'dados_climaticos': dados_climaticos}
        )


# ==========================================
# PREÇO CAFÉ
# ==========================================

class PrecosCafeView(View):

    def get(self, request, *args, **kwargs):

        precos = PrecoCafe.objects.all()

        return render(
            request,
            'precocafe.html',
            {'precos': precos}
        )


# ==========================================
# PROJEÇÃO LUCRO
# ==========================================

class ProjecoesLucroView(View):

    def get(self, request, *args, **kwargs):

        projecoes = ProjecaoLucro.objects.all()

        return render(
            request,
            'projecaolucro.html',
            {'projecoes': projecoes}
        )


# ==========================================
# CENÁRIO
# ==========================================

class CenariosView(View):

    def get(self, request, *args, **kwargs):

        cenarios = Cenario.objects.all()

        return render(
            request,
            'cenario.html',
            {'cenarios': cenarios}
        )


# ==========================================
# RELATÓRIO
# ==========================================

class RelatoriosView(View):

    def get(self, request, *args, **kwargs):

        relatorios = Relatorio.objects.all()

        return render(
            request,
            'relatorio.html',
            {'relatorios': relatorios}
        )


# ==========================================
# USUÁRIO
# ==========================================

class UsuariosView(View):

    def get(self, request, *args, **kwargs):

        usuarios = Usuario.objects.all()

        return render(
            request,
            'usuario.html',
            {'usuarios': usuarios}
        )


# ==========================================
# HISTÓRICO ANÁLISE
# ==========================================

class HistoricosAnaliseView(View):

    def get(self, request, *args, **kwargs):

        historicos = HistoricoAnalise.objects.all()

        return render(
            request,
            'historicoanalise.html',
            {'historicos': historicos}
        )


# ==========================================
# PRODUTIVIDADE
# ==========================================

class ProdutividadesView(View):

    def get(self, request, *args, **kwargs):

        produtividades = Produtividade.objects.all()

        return render(
            request,
            'produtividade.html',
            {'produtividades': produtividades}
        )


# ==========================================
# INDICADOR ECONÔMICO
# ==========================================

class IndicadoresEconomicosView(View):

    def get(self, request, *args, **kwargs):

        indicadores = IndicadorEconomico.objects.all()

        return render(
            request,
            'indicadoreconomico.html',
            {'indicadores': indicadores}
        )