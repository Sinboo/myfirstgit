from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')




# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     title = serializers.CharField(required=False,
#                                   max_length=100)
#     code = serializers.CharField(widget=widgets.Textarea,
#                                  max_length=100000)
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(default='python')
#     style = serializers.ChoiceField(default='friendly')

#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance.
#         """
#         if instance:
#             # Update existing instance
#             instance.title = attrs['title']
#             instance.code = attrs['code']
#             instance.linenos = attrs['linenos']
#             instance.language = attrs['language']
#             instance.style = attrs['style']
#             return instance

#         # Create new instance
#         return Snippet(**attrs)




# class SnippetSerializer(serializers.ModelSerializer):
# 	#owner = serializers.ReadOnlyField(source='owner.username')
# 	owner = serializers.Field(source='owner.username')
# 	#owner = serializers.CharField(read_only=True, source='owner.username')

# 	class Meta:
# 		model = Snippet
# 		fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner',)

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets',)






