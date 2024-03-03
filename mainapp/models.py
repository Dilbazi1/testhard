from django.db import models

from django.contrib.auth import get_user_model
from _datetime import datetime
from django.db.models import CharField, Count, Prefetch, Sum

User = get_user_model()


class Product(models.Model):
    author = models.CharField(max_length=60, verbose_name="author")
    name = models.CharField(max_length=60, verbose_name="name")
    created_at = models.DateField(auto_now_add=True, verbose_name="created_at")
    price = models.DecimalField(max_digits=14, decimal_places=6, verbose_name="price")
    started = models.BooleanField(verbose_name="As markdown", default=False)

    def add_student_into_groups(self, student):
        max_group_count = 6
        min_group_count = 4

        users = UserCourse.objects.all()
        if not self.started:
            s = len(users) // min_group_count
            p = len(users) % min_group_count
            users = list(users)
            last = users[p:]
            first = users[:p]
            chunks = [last[i:i + min_group_count] for i in range(0, len(last), min_group_count)]
            for i in range(s):
                try:
                    my_group = Group.objects.create(name=f'group{i}', )
                    my_group.members.set(chunks[i], through_defaults={"product": self.product.id})
                except:
                    print('unique')

            for i in range(len(first)):
                g = Group.objects.values("name", entries=Count("members")).order_by('entries')

                my_groups = Group.objects.filter(name=g[0]['name'])
                for my_group in my_groups:
                    print(first[i], my_group.name)
                    my_group.members.add(first[i], through_defaults={"product": self.product.id})
                    break
                continue


        else:
            student = 14
            g = Group.objects.values("name", entries=Count("members")).order_by('entries')
            for i in range(len(g)):
                if g[i]['entries'] < max_group_count:

                    my_groups = Group.objects.filter(name=g[i]['name'])
                    for my_group in my_groups:
                        my_group.members.add(student, through_defaults={"product": self.product.id})

                    break

                break
            i = Group.objects.values("name").annotate(entries=Count("members")).aggregate(Sum("entries"))
            groups = Group.objects.all()

            sum = i['entries__sum']
            if sum == max_group_count * len(list(groups)):
                Group.objects.create(name=f'group{len(g)}', product=self.product.id)


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    name = models.CharField(max_length=256, verbose_name="Name")
    link = models.URLField(max_length=200)


class UserCourse(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(UserCourse, )
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
