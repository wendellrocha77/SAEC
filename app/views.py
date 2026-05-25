from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


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

        dados_climaticos = DadoClimatico.objects.all()

        return render(
            request,
            'dadoclimatico.html',
            {'dados_climaticos': dados_climaticos}
        )


# ==========================================
# PREÇO CAFÉ
# ==========================================

class PrecoCafeView(LoginRequiredMixin, View):

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