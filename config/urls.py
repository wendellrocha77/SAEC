
from django.contrib import admin
from django.urls import path
from app.views import *

print("URLS CARREGADAS")

urlpatterns = [

    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
    'relatorio-tecnico/',
    RelatorioTecnicoView.as_view(),
    name='relatorio_tecnico'
    ),

    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('produtor/', ProdutorView.as_view(), name='produtor'),

    path('propriedade/', PropriedadeView.as_view(), name='propriedade'),

    path('safra/', SafraView.as_view(), name='safra'),

    path('tipocusto/', TipoCustoView.as_view(), name='tipocusto'),

    path('custoproducao/', CustoProducaoView.as_view(), name='custoproducao'),

    path('insumo/', InsumoView.as_view(), name='insumo'),

    path('dadoclimatico/', DadoClimaticoView.as_view(), name='dadoclimatico'),

    path('precocafe/', PrecoCafeView.as_view(), name='precocafe'),

    path('projecaolucro/', ProjecaoLucroView.as_view(), name='projecaolucro'),

    path('cenario/', CenarioView.as_view(), name='cenario'),

    path('relatorio/', RelatorioView.as_view(), name='relatorio'),

    path('usuario/', UsuarioView.as_view(), name='usuario'),

    path('historicoanalise/', HistoricoAnaliseView.as_view(), name='historicoanalise'),

    path('produtividade/', ProdutividadeView.as_view(), name='produtividade'),

    path('indicadoreconomico/', IndicadorEconomicoView.as_view(), name='indicadoreconomico'),

]