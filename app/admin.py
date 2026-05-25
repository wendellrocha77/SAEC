from django.contrib import admin
from .models import *


# ====================================
# INLINES
# ====================================

class PropriedadeInline(admin.TabularInline):
    model = Propriedade
    extra = 5


class SafraInline(admin.TabularInline):
    model = Safra
    extra = 5


class CustoProducaoInline(admin.TabularInline):
    model = CustoProducao
    extra = 5


class DadoClimaticoInline(admin.TabularInline):
    model = DadoClimatico
    extra = 5


class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 5


class ProjecaoLucroInline(admin.TabularInline):
    model = ProjecaoLucro
    extra = 5


class ProdutividadeInline(admin.TabularInline):
    model = Produtividade
    extra = 5


class CenarioInline(admin.TabularInline):
    model = Cenario
    extra = 5


class HistoricoAnaliseInline(admin.TabularInline):
    model = HistoricoAnalise
    extra = 5


# ====================================
# ADMINS
# ====================================

class ProdutorAdmin(admin.ModelAdmin):
    inlines = [PropriedadeInline]


class PropriedadeAdmin(admin.ModelAdmin):
    inlines = [
        SafraInline,
        DadoClimaticoInline,
        RelatorioInline
    ]


class SafraAdmin(admin.ModelAdmin):
    inlines = [
        CustoProducaoInline,
        ProjecaoLucroInline,
        ProdutividadeInline
    ]


class TipoCustoAdmin(admin.ModelAdmin):
    inlines = [CustoProducaoInline]


class ProjecaoLucroAdmin(admin.ModelAdmin):
    inlines = [CenarioInline]


class UsuarioAdmin(admin.ModelAdmin):
    inlines = [HistoricoAnaliseInline]


class CustoProducaoAdmin(admin.ModelAdmin):
    pass


class DadoClimaticoAdmin(admin.ModelAdmin):
    pass


class RelatorioAdmin(admin.ModelAdmin):
    pass


class InsumoAdmin(admin.ModelAdmin):
    pass


class PrecoCafeAdmin(admin.ModelAdmin):
    pass


class ProdutividadeAdmin(admin.ModelAdmin):
    pass


class IndicadorEconomicoAdmin(admin.ModelAdmin):
    pass


class CenarioAdmin(admin.ModelAdmin):
    pass


class HistoricoAnaliseAdmin(admin.ModelAdmin):
    pass


# ====================================
# REGISTROS
# ====================================

admin.site.register(Produtor, ProdutorAdmin)
admin.site.register(Propriedade, PropriedadeAdmin)
admin.site.register(Safra, SafraAdmin)

admin.site.register(TipoCusto, TipoCustoAdmin)

admin.site.register(CustoProducao, CustoProducaoAdmin)

admin.site.register(Insumo, InsumoAdmin)

admin.site.register(DadoClimatico, DadoClimaticoAdmin)

admin.site.register(PrecoCafe, PrecoCafeAdmin)

admin.site.register(ProjecaoLucro, ProjecaoLucroAdmin)

admin.site.register(Cenario, CenarioAdmin)

admin.site.register(Relatorio, RelatorioAdmin)

admin.site.register(Usuario, UsuarioAdmin)

admin.site.register(HistoricoAnalise, HistoricoAnaliseAdmin)

admin.site.register(Produtividade, ProdutividadeAdmin)

admin.site.register(IndicadorEconomico, IndicadorEconomicoAdmin)