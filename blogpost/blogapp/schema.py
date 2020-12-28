from graphene_django import DjangoObjectType,DjangoListField
import graphene
from .models import BlogPost,Comments
from datetime import datetime

class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        field = ('id','title','description','publish_date','author')
    
class CommentsType(DjangoObjectType):
    class Meta:
        model = Comments
        field = ('id','comment','created_on','author')

class Query(graphene.ObjectType):

    #5) Post all query with djangofield,without resolve
    posts = DjangoListField(BlogPostType)
    # Comments all query with djangofield,without resolve
    comments = DjangoListField(CommentsType)

    # blog get by id
    post_id = graphene.Field(BlogPostType, id=graphene.Int())
    # comment get by id
    comments_id = graphene.List(CommentsType, id=graphene.Int())

    #6) get blog by id with resolve
    def resolve_post_id(self, info, id):
        return BlogPost.objects.get(id=id)
        
    # get comment by id with resolve
    def resolve_comments_id(self, info, id):
        return Comments.objects.filter(author=id)

# 1) Create blogpost mutation 
class CreateMutation(graphene.Mutation):
    create_post = graphene.Field(BlogPostType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(required=True)
        publish_date =  graphene.DateTime(default_value=datetime.now())

    def mutate(self,info,title,description,author,publish_date):
        createPost = BlogPost(title=title,description=description,author=author,publish_date=publish_date)
        createPost.save()
        return CreateMutation(create_post=createPost)

# 2) Update post with post ID
class UpdateBlogMutation(graphene.Mutation):
    update_post = graphene.Field(BlogPostType)
    # I added all attributes to required True
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(required=True)

    def mutate(self,info,id,title,description,author):
        update_Post = BlogPost.objects.filter(id=id) #if we have two author name,i used first index object to update
        # for this assignment i'm not added updated date field
        update_Post[0].title = title
        update_Post[0].description = description
        update_Post[0].author = author
        update_Post[0].save()
        return UpdateBlogMutation(update_post=update_Post[0])

#3) Create New Comment for Blog post with only unique one author
class CreateCommentMutation(graphene.Mutation):
    
    create_comment = graphene.Field(CommentsType)
    
    class Arguments:
        comment = graphene.String()
        author = graphene.String()
        
    def mutate(self, info,author, comment):
        author = BlogPost.objects.filter(author=author)
        if len(author) == 1:
            comments_create = Comments( comment=comment, author=author[0])
            comments_create.save()
            return CreateCommentMutation(create_comment=comments_create)
        elif len(author) > 1:
            return CreateCommentMutation("can't create comment two author with the same")
        else:
            return CreateCommentMutation("Create author with name and then add comment")


#4) Delete comment with ID
class DeleteCommentMutation(graphene.Mutation):
    delete_comment = graphene.Field(CommentsType)
    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self,info,id):
        deleteComment = Comments.objects.get(id=id)
        deleteComment.delete()
        return DeleteCommentMutation(delete_comment=deleteComment)

        

class Mutation(graphene.ObjectType):
    createpost = CreateMutation.Field()
    update_post = UpdateBlogMutation.Field()
    delete_comment = DeleteCommentMutation.Field()
    create_comment = CreateCommentMutation.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)
