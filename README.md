## ---Graphql-assignment---##

A simple blog post and comments with associated author, and curd operation on graphical API.

I used the graphene library to implement Graphql API query and mutation.


# Impelment same project in your local:


1)Clone repo


2)create virtual environment


3)install required library to implement by using "pip install -r requirements.txt"


4)python manage.py makemigrations


5)python manahe.py migrate


6)open browser and paste "http://127.0.0.1:8000/graphql/"


query all listed statements in graphql dashboard:


###### 1) Create new blog post


 mutation CreateMutation{
  createPost(title:"New create blog post",description:"added new post with description",author:"Madu Devara"){
     createPost{
       id
       title
       description
       author
       publishDate
     }
   }
 }


o/p:

'''
{
  "data": {
    "createpost": {
      "createPost": {
        "id": "11",
        "title": "New create blog post",
        "description": "added new post with description",
        "author": "Madu Devara",
        "publishDate": "2020-12-28T09:20:59.254127+00:00"
      }
    }
  }
}
'''

###### 2) Update blog post


 mutation updatemutation{
   updatePost(id:1,title:"Firs Blog Updated",author:"Ramu",description:"Update mutation all Description"){
     updatePosts{
       title
       description
       author
       id
     }
   }
 }


o/p:


{
  "data": {
    "updatePost": {
      "updatePost": {
        "title": "First Blog Post",
        "description": "First blog post description data",
        "author": "Ramu",
        "id": "1"
      }
    }
  }
}


###### 3) create new  comment with author name 


 mutation CreateCommentMutation{
   createComment(author:"Ramu",comment:"new commnet created with post author"){
     createComment{
       comment
       author{
         id
       }
     }
     }
   }


o/p:


{
  "data": {
    "createComment": {
      "createComment": {
        "comment": "new commnet created with post author",
        "author": {
          "id": "1"
        }
      }
    }
  }
}


###### 4)Delete comment with unique ID 


 mutation DeleteComment{
   deleteComment(id:15){
     deleteComment{
       comment
       id
     }
   }
   }


o/p:


{
  "data": {
    "deleteComment": {
      "deleteComment": null
    }
  }
}


###### 5)query to get all posts


 query{
   posts {
     title
     publishDate
     author
     id
   }
 }


o/p:


{
  "data": {
    "posts": [
      {
        "title": "First Blog Post",
        "publishDate": "2020-12-26T18:49:14.858082+00:00",
        "author": "Ramu",
        "id": "1"
      },
      {
        "title": "Second Blog Post",
        "publishDate": "2020-12-26T18:49:14.858082+00:00",
        "author": "Jaya",
        "id": "3"
      },
      {
        "title": "Fourth Blog Post",
        "publishDate": "2020-12-27T14:27:58.128098+00:00",
        "author": "Madhu Devara",
        "id": "9"
      },
      {
        "title": "Duplicate Post",
        "publishDate": "2020-12-28T08:42:52.660509+00:00",
        "author": "Madhu Devara",
        "id": "10"
      },
      {
        "title": "New create blog post",
        "publishDate": "2020-12-28T09:20:59.254127+00:00",
        "author": "Madu Devara",
        "id": "11"
      }
    ]
  }
}


###### 6)query to get all comments with post id


 query{
   postId(id:1) {
     id
     title
     author
   }
   commentsId(id:1){
     comment
     author {
       id
       author
     }
   }
 }

o/p:


{
  "data": {
    "postId": {
      "id": "1",
      "title": "First Blog Post",
      "author": "Ramu"
    },
    "commentsId": [
      {
        "comment": "First Comment",
        "author": {
          "id": "1",
          "author": "Ramu"
        }
      },
      {
        "comment": "Third Comment",
        "author": {
          "id": "1",
          "author": "Ramu"
        }
      }
    ]
  }
}
