from django.db import models


TIPOS = [
    ('RECEITAS', 'RECEITAS'),
    ('DESPESAS', 'DESPESAS')]


class BaseUser(models.Model):
    email = models.EmailField("E-mail")

    def __str__(self):
        return self.email


class Categoria(models.Model):
    user = models.ForeignKey('BaseUser', on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=8, choices=TIPOS)
    categoria = models.CharField('Categoria', max_length = 50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.tipo} | {self.categoria}"


class Movimento(models.Model):
    user = models.ForeignKey('BaseUser', on_delete=models.CASCADE)
    data = models.DateField('Data')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    descricao = models.CharField('Descrição', max_length=100)
    valor = models.FloatField('Valor')

    class Meta:
        verbose_name = "Movimento"
        verbose_name_plural = "Movimentos"

    def __str__(self):
        return f"{self.user} | {self.data} | {self.categoria} | {self.descricao[:20]} | {self.valor}"
