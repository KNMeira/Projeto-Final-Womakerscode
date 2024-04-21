@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'cpf')
    fields = [('nome', 'sobrenome'), 'email', ('cpf')]  

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('carro', 'placa', 'ano', 'cliente')
    list_filter = ('ano', 'cliente')
