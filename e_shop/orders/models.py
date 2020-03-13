from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User


class Cart(models.Model):
    NEW = "new"
    IN_PROCESS = "in_process"
    RENOUNCEMENT = "renouncement"
    COMPLETE = "complete"
    WITH_QUESTION = "?"

    STATUSES = (
        (NEW, "Новый заказ"),
        (IN_PROCESS, "Заказ в процессе обработки"),
        (RENOUNCEMENT, "Заказ отклонен"),
        (COMPLETE, "Заказ выполнен "),
        (WITH_QUESTION, "Не получен ответ пользователя")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost = models.FloatField(
        validators=[MinValueValidator(0.0)], verbose_name='Полная цена')
    status = models.CharField(
        max_length=30, verbose_name='Статус', choices=STATUSES, default=NEW)

    def __str__(self):
        return str(self.id) + self.status