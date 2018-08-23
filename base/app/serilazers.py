from app.extensions import ma
from app.models.post import Post, Category


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
