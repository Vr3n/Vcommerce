from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

# Create your models here.


class Category(MPTTModel):
    """
    Inventory category table implemented with MPTT.
    """

    name = models.CharField(_("Category Name"), max_length=255,
                            help_text=_("format: required, max-255"))
    slug = models.SlugField(
        _("Category slug"),
        max_length=255,
        help_text=_("format: required, max-255"),
    )

    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey("self",
                            on_delete=models.PROTECT,
                            related_name="children",
                            null=True,
                            blank=True,
                            verbose_name=_("Parent of category"),
                            help_text=_("format: not required"),
                            )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self) -> str:
        return self.name
