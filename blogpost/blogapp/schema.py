from graphene_django import DjangoObjectType,DjangoListField
import graphene
from .models import BlogPost,Comments

class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        field = ('id','title','description','publish_date')
    
class CommentsType(DjangoObjectType):
    class Meta:
        model = Comments
        field = ('id','comment','created_on','author')

class Query(graphene.ObjectType):

    # Post all query with djangofield
    all_posts = DjangoListField(BlogPostType)
    # Comments all query with djangofield
    all_comments = DjangoListField(CommentsType)


    # blog get by id
    blog_by_id = graphene.Field(BlogPostType, id=graphene.Int())
    # comment get by id
    comments_by_id = graphene.Field(CommentsType, id=graphene.Int())

    # get blog by id with resolve
    def resolve_blog_by_id(self, info, id):
        return BlogPost.objects.get(pk=id)
        
    # get comment by id with resolve
    def resolve_comments_by_id(self, info, id):
        return Comments.objects.get(pk=id)
    
schema = graphene.Schema(query=Query)