import datetime

from django.db import models


class ScientificDirector(models.Model):
    last_name = models.CharField(verbose_name="Last Name", max_length=60, default="", blank=False)
    first_name = models.CharField(verbose_name="First Name", max_length=60, default="", blank=False)
    patronymic = models.CharField(verbose_name="Patronymic", max_length=60, default="", blank=False)

    former_student = models.ForeignKey(
        verbose_name="Former Student",
        to="topics.Student",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


def get_current_year():
    return datetime.date.today().year


class BachelorTopic(models.Model):
    title = models.CharField(verbose_name="Title", max_length=120, default="", blank=False)
    year = models.IntegerField(
        verbose_name="Year",
        choices=[(x, str(x)) for x in range(1984, datetime.date.today().year+1)],
        default=get_current_year
    )

    director = models.ForeignKey(
        ScientificDirector,
        verbose_name="Director",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    last_name = models.CharField(verbose_name="Last Name", max_length=60, default="", blank=False)
    first_name = models.CharField(verbose_name="First Name", max_length=60, default="", blank=False)
    patronymic = models.CharField(verbose_name="Patronymic", max_length=60, default="", blank=False)

    topic = models.ForeignKey(
        BachelorTopic,
        verbose_name="Bachelor Topic",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"