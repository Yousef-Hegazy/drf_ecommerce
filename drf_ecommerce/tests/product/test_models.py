import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        post = category_factory(name="test_cat")
        # Assert
        assert post.__str__() == "test_cat"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        post = brand_factory(name="test_brand")
        # Assert
        assert post.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        post = product_factory(name="test_prod")
        # Assert
        assert post.__str__() == "test_prod"
