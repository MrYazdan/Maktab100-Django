import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post, Comment  # noqa
from product.models import Product  # noqa
from members.models import Membership  # noqa
from django.db.models import Q, Count, Max, Min, Avg, Sum  # noqa

# Limit - Offset
# tmp = Product.objects.filter()[5:15]

# Ordering
# tmp = Product.objects.archive().order_by('id') => ASC
# tmp = Product.objects.archive().order_by('-id') => DESC
# tmp = Product.objects.archive().order_by('?') => RAND

# IS NULL
# tmp = Membership.objects.filter(invite_reason=None)
# tmp = Membership.objects.filter(invite_reason__isnull=False)

# Range => BETWEEN
# tmp = Product.objects.archive().filter(id__range=(1, 10))
# tmp = Product.objects.archive().filter(updated_at__range=("2024-01-01", "2025-01-01"))

# Not between
# tmp = Product.objects.archive().filter(~Q(id__range=(1, 10)))

# Not isnull
# tmp = Membership.objects.filter(~Q(invite_reason=None))


# LIKE
# tmp = Product.objects.archive().filter(title__startswith="P")  # LIKE 'P%'
# tmp = Product.objects.archive().filter(title__istartswith="p")  # LIKE UPPER('P%')
# tmp = Product.objects.archive().filter(title__iendswith="p")  # LIKE UPPER('%P')
# tmp = Product.objects.archive().filter(title__icontains="oy")  # LIKE UPPER('%OY%')


# Filtering
# tmp = Product.objects.filter(title__icontains="o", id__gt=1)  # AND
# tmp = Product.objects.filter(id__lt=10) | Product.objects.filter(id__gt=20)  # OR
# tmp = Product.objects.filter(Q(id__lt=10) | Q(id__gt=20) & Q(id=21))  # OR

# values vs values_list vs only
# tmp = Product.objects.values('title')  # select title from ... => {'title': ...}
# tmp = Product.objects.values_list('title')  # select title from ... => (...,)
# tmp = Product.objects.values_list('title', flat=True)  # select title from ... => (...,)
# tmp = Product.objects.only('title')  # select title from ... => [Object.is]

# Length
# tmp = Product.objects.archive().count()
# tmp = Product.objects.aggregate(plt_10_count=Count("id", filter=Q(id__lt=10)))
# tmp = Product.objects.aggregate(Avg("id"))
# tmp = Product.objects.aggregate(Sum("id"))
# tmp = Product.objects.aggregate(Min("id"))
# tmp = Product.objects.aggregate(Max("id"))

# Annotate
# tmp = Product.objects.annotate(avg_id=Avg('id'))
# tmp = Post.objects.archive().annotate(count_comments=Count('comments'))

# from faker import Faker
# import random

# fake = Faker()

# for i in range(100):
#     Comment.objects.create(
#         post=Post.objects.get(id=random.randint(1, 10)),
#         subject=fake.name(),
#         reply_to=Comment.objects.get(id=random.randint(1, i + 2 - 1)) if random.randint(0, 1) else None
#     )

# for i in range(9):
#     Post.objects.create(title=fake.name(), content=fake.text())

# for post in tmp:
#     print("Post:", post.id, "Comments:", post.count_comments)

tmp = Comment.objects.filter(Q(reply_to=None)).annotate(count_replies=Count("replies")).filter(count_replies__gte=2)

for comment in tmp:
    print("Comment:", comment.id, "replies:", comment.count_replies)

print(str(tmp.query))
