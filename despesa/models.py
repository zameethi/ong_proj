from django.db import models
from smart_selects.db_fields import ChainedManyToManyField

class Subcategoria(models.Model):
    descricao_subcategoria = models.CharField(max_length=30, unique=True, blank=True)

    class Meta:
        db_table = 'subcategoria'

    def __str__(self):
      return self.descricao_subcategoria


class Categoria(models.Model):
    descricao_categoria = models.CharField(max_length=254, blank=False, unique=True, verbose_name='categoria', default=None)
    subcategorias = models.ManyToManyField('Subcategoria', blank=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
      return self.descricao_categoria


class TipoDocumento(models.Model):
    tipo_documento = models.CharField(blank=False, max_length=50, unique=True)

    class Meta:
        db_table = 'tipoDocumento'

    def __str__(self):
        return self.tipo_documento


class TipoTransacao(models.Model):
    tipo_transacao = models.CharField(blank=False, max_length=50)

    class Meta:
        db_table = 'tipoTransacao'

    def __str__(self):
        return self.tipo_transacao


class Despesa(models.Model):
    data_despesa = models.DateField(verbose_name='data')
    valor_despesa = models.FloatField(max_length=10)
    descricao_despesa = models.TextField(max_length=255)
    documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, blank=True)
    documento_complemento = models.CharField(max_length=50, blank=True)
    transacao = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, blank=True)
    transacao_complemento = models.CharField(max_length=50, blank=True)
    conciliado = models.BooleanField(default='0')
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
    subcategorias = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        db_table = 'despesa'

    def __str__(self):
        return self.descricao_despesa

