from django.db import models
from django.contrib.auth.models import User

# Métodos e Choices


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


# Classes (modelos)

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, verbose_name='UF')

    def __str__(self):
        return "{}".format(self.uf)


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nome)


class Campus(models.Model):
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150, verbose_name="endereço")
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Servidor(models.Model):
    nome_completo = models.CharField(max_length=100)
    siape = models.CharField(max_length=10)
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="usuário")


class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Situacao(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    movimentado_em = models.DateTimeField(auto_now_add=True)
    movimentado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    detalhes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{} em {} por {}".format(self.status, self.movimentado_em, self.movimentado_por)


class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField(verbose_name="nível")
    descricao = models.CharField(max_length=150, verbose_name="descrição", null=True, blank=True)

    def __str__(self):
        return "{} nível {}".format(self.nome, self.nivel)


class Progressao(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, verbose_name="classe pretendida")
    data_inicial = models.DateField()
    data_final = models.DateField()
    observacao = models.CharField(max_length=255, verbose_name="observação")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} -> {} | {} a {}".format(self.usuario, self.classe, self.data_inicial, self.data_final)


class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Atividade(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=255, verbose_name="descrição")
    pontos = models.DecimalField(decimal_places=2, max_digits=5)
    detalhes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["numero", "campo"], name="unica_num_atividade_campo")
        ]


class Comprovante(models.Model):
    progressao = models.ForeignKey(Progressao, on_delete=models.PROTECT, verbose_name="progressão")
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    data = models.DateField()
    data_final = models.DateField(null=True, blank=True, help_text="Informar apenas se o comprovante for relativo a um período.")
    arquivo = models.FileField(upload_to='pdf/')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "[{}] {} - {}/{}".format(self.pk, self.usuario, self.progressao, self.atividade)


class Validacao(models.Model):
    comprovante = models.ForeignKey(Comprovante, on_delete=models.PROTECT)
    validado_em = models.DateTimeField(auto_now_add=True)
    validado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    justificativa = models.TextField(max_length=255)

    def __str__(self):
        return "[{}] Pontuação: {}/{} por {}".format(self.comprovante.pk, self.quantidade, self.comprovante.quantidade, self.validado_por)
