from sketchbookapi.models import Post
from sketchbookapi.models import MediumPost
from sketchbookapi.models import Medium
from sketchbookapi.models import Artist
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from sketchbookapi.serializers import PostSerializer
 
 
class PostView(ViewSet):
    
    def list(self, request):
        """Get a list of all post"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
 
#     def create(self, request):
#         """Create a new post"""
#         #! grabbing post object where seller =request.auth.user
#         artist = Artist.objects.get(user=request.auth.user)
#         #! grabbing medium object that is also needed 
#         medium_post = MediumPost.objects.get(pk=request.data['mediumPostId'])
        
#         try:
#             product = Product.objects.create(
#                 name=request.data['name'],
#                 # grabbing post information from above
#                 price=request.data['price'],
#                 description=request.data['description'],
#                 quantity=request.data['quantity'],
#                 location=request.data['location'],
#                 # adding medium information from above
#                 medium_post=medium_post
#             )
#             serializer = ProductSerializer(product)
#             # need to make a serializer to create json out of dictionary object
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#  # !!! when would the except run? I tried filling this out client-side ommiting data and it still creates and object
#         except ValidationError as ex:
#             return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
         
