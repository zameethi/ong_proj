from django.db import models

class Subcategoria(models.Model):
  descricao_subcategoria = models.CharField(max_length=30, unique=True, blank=True)

  def __str__(self):
      return self.descricao_subcategoria


class Categoria(models.Model):
  descricao_categoria = models.TextField(blank=False, unique=True, verbose_name='categoria')
  subcategoria = models.ManyToManyField('Subcategoria', blank=True)

  def __str__(self):
      return self.descricao_categoria


class TipoDocumento(models.Model):
    tipo_documento = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.tipo_documento


class TipoTransacao(models.Model):
    tipo_transacao = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.tipo_transacao


class Despesa(models.Model):
    data_despesa = models.DateField(verbose_name='data')
    valor_despesa = models.DecimalField(max_digits=8, decimal_places=2)
    descricao_despesa = models.TextField(max_length=255)
    documento = models.OneToOneField('TipoDocumento', on_delete=models.CASCADE)
    documento_complemento = models.CharField(max_length=50)
    transacao = models.OneToOneField('TipoTransacao', on_delete=models.CASCADE)
    transacao_complemento = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.descricao_despesa

