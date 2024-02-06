import factory

from drf_ecommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"test_category_{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"test_brand_{n}")


class ProductFactory(factory.django.DjangoModelFactory):
    name = "test_prod"
    description = "test_desc"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
