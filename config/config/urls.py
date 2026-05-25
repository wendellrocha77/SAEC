from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [

    # ==========================================
    # ADMIN
    # ==========================================

    path('admin/', admin.site.urls),


    # ==========================================
    # INDEX
    # ==========================================

    path('', IndexView.as_view(), name='index'),


    # ==========================================
    # PRODUTOR
    # ==========================================

    path(
        'produtor/',
        ProdutoresView.as_view(),
        name='produtor'
    ),


    # ==========================================
    # PROPRIEDADE
    # ==========================================

    path(
        'propriedade/',
        PropriedadesView.as_view(),
        name='propriedade'
    ),


    # ==========================================
    # SAFRA
    # ==========================================

    path(
        'safra/',
        SafrasView.as_view(),
        name='safra'
    ),


    # ==========================================
    # TIPO CUSTO
    # ==========================================

    path(
        'tipocusto/',
        TiposCustoView.as_view(),
        name='tipocusto'
    ),


    # ==========================================
    # CUSTO PRODUÇÃO
    # ==========================================

    path(
        'custoproducao/',
        CustosProducaoView.as_view(),
        name='custoproducao'
    ),


    # ==========================================
    # INSUMO
    # ==========================================

    path(
        'insumo/',
        InsumosView.as_view(),
        name='insumo'
    ),


    # ==========================================
    # DADO CLIMÁTICO
    # ==========================================

    path(
        'dadoclimatico/',
        DadosClimaticosView.as_view(),
        name='dadoclimatico'
    ),


    # ==========================================
    # PREÇO CAFÉ
    # ==========================================

    path(
        'precocafe/',
        PrecosCafeView.as_view(),
        name='precocafe'
    ),


    # ==========================================
    # PROJEÇÃO LUCRO
    # ==========================================

    path(
        'projecaolucro/',
        ProjecoesLucroView.as_view(),
        name='projecaolucro'
    ),


    # ==========================================
    # CENÁRIO
    # ==========================================

    path(
        'cenario/',
        CenariosView.as_view(),
        name='cenario'
    ),


    # ==========================================
    # RELATÓRIO
    # ==========================================

    path(
        'relatorio/',
        RelatoriosView.as_view(),
        name='relatorio'
    ),


    # ==========================================
    # USUÁRIO
    # ==========================================

    path(
        'usuario/',
        UsuariosView.as_view(),
        name='usuario'
    ),


    # ==========================================
    # HISTÓRICO ANÁLISE
    # ==========================================

    path(
        'historicoanalise/',
        HistoricosAnaliseView.as_view(),
        name='historicoanalise'
    ),


    # ==========================================
    # PRODUTIVIDADE
    # ==========================================

    path(
        'produtividade/',
        ProdutividadesView.as_view(),
        name='produtividade'
    ),


    # ==========================================
    # INDICADOR ECONÔMICO
    # ==========================================

    path(
        'indicadoreconomico/',
        IndicadoresEconomicosView.as_view(),
        name='indicadoreconomico'
    ),

]
