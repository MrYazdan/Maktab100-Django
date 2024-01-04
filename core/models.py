from django.db import models


class TimeStampBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class LogicalQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True)

    def hard_delete(self):
        return super().delete()


class LogicalManager(models.Manager):
    # def logical_queryset(self):
    #     return LogicalQuerySet(self.model)

    def get_queryset(self):
        return LogicalQuerySet(self.model).filter(is_deleted=False, is_active=True)

    def archive(self):
        return LogicalQuerySet(self.model)

    def deleted(self):
        return LogicalQuerySet(self.model).filter(is_deleted=True)


class LogicalBaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    # objects = models.Manager()
    # shima = LogicalManager()
    objects = LogicalManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    def undelete(self):
        self.is_deleted = False
        self.save()


class StatusMixin:
    @property
    def status(self) -> bool:
        return self.is_active and not self.is_deleted  # noqa



