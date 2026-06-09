from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from app.models import PrecoCafe

class LoginView(View):

    def get(self, request):

        return render(
            request,
            'login.html'
        )

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

        return render(
            request,
            'login.html',
            {'erro': 'Usuário ou senha inválidos'}
        )
    

class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect('/login/')
    


class RelatorioTecnicoView(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'produtores': Produtor.objects.all(),
            'propriedades': Propriedade.objects.all(),
            'safras': Safra.objects.all(),
        }

        return render(
            request,
            'relatorio_tecnico_form.html',
            context
        )

    def post(self, request):

        produtor_id = request.POST.get('produtor')
        propriedade_id = request.POST.get('propriedade')
        safra_id = request.POST.get('safra')

        custo_admin = Decimal(
            request.POST.get('custo_admin') or '0'
        )

        custo_financeiro = Decimal(
            request.POST.get('custo_financeiro') or '0'
        )

        outros_custos = Decimal(
            request.POST.get('outros_custos') or '0'
        )

        preco_esperado = Decimal(
            request.POST.get('preco_esperado') or '0'
        )

        produtor = Produtor.objects.get(
            id=produtor_id
        )

        propriedade = Propriedade.objects.get(
            id=propriedade_id
        )

        safra = Safra.objects.get(
            id=safra_id
        )

        custos = CustoProducao.objects.filter(
            safra=safra
        )

        custo_total = sum(
            (custo.valor for custo in custos),
            Decimal('0')
        )

        custo_total += (
            custo_admin +
            custo_financeiro +
            outros_custos
        )

        receita = (
            Decimal(str(safra.produtividade))
            * preco_esperado
        )

        lucro = receita - custo_total

        if lucro > 50000:
            classificacao = "Excelente"

        elif lucro > 20000:
            classificacao = "Boa"

        elif lucro > 0:
            classificacao = "Regular"

        else:
            classificacao = "Prejuízo"


        # Diagnóstico automático

        if classificacao == "Excelente":

            diagnostico = """
            A propriedade apresenta excelente desempenho econômico,
            com elevada margem de lucro e boa perspectiva financeira.
            """

            recomendacao = """
            Recomenda-se manter o atual modelo de produção e avaliar
            investimentos em expansão da área produtiva.
            """

        elif classificacao == "Boa":

            diagnostico = """
            A propriedade apresenta desempenho satisfatório,
            com retorno financeiro positivo.
            """

            recomendacao = """
            Recomenda-se otimizar custos e acompanhar o mercado
            para aumentar a rentabilidade.
            """

        elif classificacao == "Regular":

            diagnostico = """
            A margem de lucro encontra-se reduzida,
            indicando necessidade de melhorias operacionais.
            """

            recomendacao = """
            Recomenda-se revisar os custos de produção e buscar
            ganhos de produtividade.
            """

        else:

            diagnostico = """
            A análise indica prejuízo econômico na safra avaliada.
            """

            recomendacao = """
            Recomenda-se reavaliar o planejamento financeiro e
            reduzir custos operacionais.
            """


        # Cenários

        cenario_pessimista = receita * Decimal('0.85')

        cenario_realista = receita

        cenario_otimista = receita * Decimal('1.15')


        context = {

            'produtores': Produtor.objects.all(),
            'propriedades': Propriedade.objects.all(),
            'safras': Safra.objects.all(),

            'produtor': produtor,
            'propriedade': propriedade,
            'safra': safra,

            'receita': receita,
            'custo_total': custo_total,
            'lucro': lucro,
            'classificacao': classificacao,

            'diagnostico': diagnostico,
            'recomendacao': recomendacao,

            'cenario_pessimista': cenario_pessimista,
            'cenario_realista': cenario_realista,
            'cenario_otimista': cenario_otimista,
        }

        return render(
            request,
            'relatorio_tecnico_form.html',
            context
        )
# ==========================================
# INDEX
# ==========================================

class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# ==========================================
# PRODUTOR
# ==========================================

class ProdutorView(LoginRequiredMixin, View):

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

class PropriedadeView(LoginRequiredMixin, View):

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

class SafraView(LoginRequiredMixin, View):

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

class TipoCustoView(LoginRequiredMixin, View):

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

class CustoProducaoView(LoginRequiredMixin, View):

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

class InsumoView(LoginRequiredMixin, View):

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

class DadoClimaticoView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        dados = DadoClimatico.objects.order_by('data')

        dados_json = [
            {
                "data": d.data.strftime("%d/%m/%Y"),
                "temperatura": float(d.temperatura),
                "chuva": float(d.chuva),
            }
            for d in dados
        ]

        return render(
            request,
            'dadoclimatico.html',
            {
                'dados': dados,
                'dados_json': dados_json
            }
        )


# ==========================================
# PREÇO CAFÉ
# ==========================================

class PrecoCafeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        precos = PrecoCafe.objects.order_by('data')

        # 🔴 conversão correta para JSON (resolve o erro)
        precos_json = [
            {
                "data": p.data.strftime("%d/%m/%Y"),
                "valor_saca": float(p.valor_saca),
                "mercado": p.mercado
            }
            for p in precos
        ]

        return render(
            request,
            'precocafe.html',
            {
                'precos': precos,          # tabela Django normal
                'precos_json': precos_json # gráfico JSON seguro
            }
        )

# ==========================================
# PROJEÇÃO LUCRO
# ==========================================

class ProjecaoLucroView(LoginRequiredMixin, View):

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

class CenarioView(LoginRequiredMixin, View):

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

class RelatorioView(LoginRequiredMixin, View):

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

class UsuarioView(LoginRequiredMixin, View):

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

class HistoricoAnaliseView(LoginRequiredMixin, View):

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

class ProdutividadeView(LoginRequiredMixin, View):

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

class IndicadorEconomicoView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        indicadores = IndicadorEconomico.objects.all()

        return render(
            request,
            'indicadoreconomico.html',
            {'indicadores': indicadores}
        )