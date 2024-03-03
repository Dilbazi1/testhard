from django.core.management import BaseCommand
from mainapp.models import Group, UserCourse, Product
from django.db import models

from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models.functions import Lower
from django.db.models import CharField, Count, Prefetch, Sum
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # # x = datetime.now()
        # # print(x.day)
        # products = Product.objects.first()
        # groups = Group.objects.all()
        # max_group_count = 3
        # # for group in groups:
        # #     print('eeeeeeeeeeeeeee', group.members.clear())
        # min_group_count = 2
        # if not Product.created_at:
        #     users = UserCourse.objects.all()
        #
        #     # members = UserCourse.objects.all()
        #     # print(list(users), users, '555555555555555555555555')
        #     # print(type(users))
        #     # print(groups)
        #     # for user in range(len(users)):
        #     #     print(user)
        #     s = len(users) // min_group_count
        #     p = len(users) % min_group_count
        #     print(list(users))
        #     users = list(users)
        #     last = users[p:]
        #     first = users[:p]
        #     print(first, '|||||', last)
        #
        #     # print(type(products.name))
        #     # print(type(Product.name))
        #     # my_groups=[]
        #     # i=1
        #     # chunk_size = 2
        #     # # chunks = [users[i:i + chunk_size] for i in range(0, len(users), chunk_size)]
        #     # for i in range(s+1):
        #
        #     # my_group=Group.objects.create(name=f'group{i}')
        #     # print('-----------------',my_group.name)
        #     #     # # print(len(chunks),'=================================================')
        #     #     # # if len(chunks)<min_group_count:
        #     #     #     # my_group.members.set([chunks[i], chunks[i+1]],through_defaults={"product": products.id})
        #     #     # # else:
        #     #     #     my_group.members.set(chunks[i], through_defaults={"product": products.id})
        #     #     print('here',my_group.members,my_group.name)
        #     # # return my_groups
        #     #
        #     #     print('zdes',list(users))
        #     users = list(users)
        #     # k=len(users)-1
        #
        #     chunks = [last[i:i + min_group_count] for i in range(0, len(last), min_group_count)]
        #
        #     for i in range(s):
        #         try:
        #
        #             my_group = Group.objects.create(name=f'group{i}', )
        #
        #             my_group.members.set(chunks[i], through_defaults={"product": products.id})
        #
        #
        #         except:
        #             print('unique')
        #         print(len(first), '--------------------------------')
        #         my_groups = Group.objects.filter(id__lt=len(first) + 1)
        #         print('55555555', my_groups)
        #
        #         for my_group in my_groups:
        #             print(my_group.members, '--')
        #             #
        #             #
        #             #     my_group.members.set(chunks[i], through_defaults={"product": products.id})
        #
        #             for i in range(len(first)):
        #                 my_group.members.add(first[i], through_defaults={"product": products.id})
        #                 print('000000000000000', first[i])
        #         # print(Group.objects.order_by(Lower("members").desc()))
        #     i = Group.objects.values("members", entries=Count("members"))
        #     print(i)
        #     i = Group.objects.values("name").annotate(entries=Count("members")).aggregate(Sum("entries"))
        #     print(i, 'fffffffffff')
        #     q = Group.objects.annotate(Count("members"))
        #     print(q[0].name)
        #     print(Group.objects.values('members'))
        #     print('------------')
        #     print(UserCourse.objects.values(), 'rftrgt')
        #     print(Group.objects.prefetch_related('members'))
        #     print(Group.objects.only('name'), 'name')
        #     # queryset = UserCourse.objects.only('date')
        #
        #     # restaurants = Group.objects.prefetch_related(
        #     #
        #     # Prefetch('members', queryset=queryset))
        #     # print(restaurants)
        #     print(UserCourse.objects.count(), 'rftrgt')
        #     print(Group.objects.count(), 'rftrgt')
        #
        #     print(Group.objects.filter(name__contains="gr").count())
        #     print(Group.objects.filter(name__contains="gr").count())
        #     print(Group.objects.filter(name="group0").count())
        #     blogs = Group.objects.alias(entries=Count("members")).order_by()
        #     print(blogs)
        # student = 4
        #
        # if Product.created_at < timezone.now():
        #     # order_groups=Group.objects.alias(entries=Count("members")).order_by('entries')
        #     # print(order_groups)
        #     #
        #     # for group in order_groups:
        #     #     print(group.name,'---')
        #
        #     # print(g[0]['entries'])
        #
        #     # print(order_groups)
        #     # for group in order_groups:
        #     #     print(group.name)
        #     g = Group.objects.values("name", entries=Count("members")).order_by('entries')
        #     print(g)
        #
        #     for i in range(len(g)):
        #         print(i, g[i]['entries'])
        #
        #         if g[i]['entries'] < max_group_count:
        #             print(i, 'zdes')
        #
        #             my_groups = Group.objects.filter(name=g[i]['name'])
        #             for my_group in my_groups:
        #                 my_group.members.add(student, through_defaults={"product": products.id})
        #
        #             print(g[i]['name'], 'zdes')
        #             break
        #
        #         continue
        #     i = Group.objects.values("name").annotate(entries=Count("members")).aggregate(Sum("entries"))
        #     print(i['entries__sum'])
        #     sum = i['entries__sum']
        #     if sum % max_group_count == 0:
        #         print(sum, max_group_count, 'creating')
        #         Group.objects.create(name=f'group{len(g)}', )
        max_group_count = 6
        min_group_count = 4
        student = 24
        users = UserCourse.objects.all()
        product = Product.objects.first()
        students = list()

        users = UserCourse.objects.all()
        if not product.started:
            # groups = Group.objects.all()
            # for group in groups:
            #      group.members.clear()
            s = len(users) // min_group_count
            p = len(users) % min_group_count
            users = list(users)
            last = users[p:]
            first = users[:p]
            chunks = [last[i:i + min_group_count] for i in range(0, len(last), min_group_count)]
            for i in range(s):
                try:
                    my_group = Group.objects.create(name=f'group{i}')
                    my_group.members.set(chunks[i], through_defaults={"product": product.id})
                except:
                    print('unique')

                my_groups = Group.objects.filter(id__lt=len(first) + 1)
            for i in range(len(first)):
                g = Group.objects.values("name", entries=Count("members")).order_by('entries')

                print('g=', g, 'g[0]name', g[0]['name'])
                my_groups = Group.objects.filter(name=g[0]['name'])
                for my_group in my_groups:
                    print(first[i], my_group.name)
                    my_group.members.add(first[i], through_defaults={"product": product.id})
                    break
                continue

            # for my_group in my_groups:
            #     for i in range(len(first)):
            #         my_group.members.add(first[i], through_defaults={"product": product.id})
            # groups = Group.objects.all()
            # for group in groups:
            #              group.members.clear()







        else:
            # student =12
            g = Group.objects.values("name", entries=Count("members")).order_by('entries')
            for i in range(len(g)):
                if g[i]['entries'] < max_group_count:
                    print(g[i]['entries'], g[i]['name'], max_group_count)
                    my_groups = Group.objects.filter(name=g[i]['name'])
                    for my_group in my_groups:
                        my_group.members.add(student, through_defaults={"product": product.id})

                    print(g[i]['name'])
                    break

                break
            i = Group.objects.values("name").annotate(entries=Count("members")).aggregate(Sum("entries"))
            groups = Group.objects.all()
            print(i['entries__sum'])
            sum = i['entries__sum']

            if sum == max_group_count * len(list(groups)):
                students.append(student)
                print(students)

                if len(students) == min_group_count:
                    group = Group.objects.create(name=f'group{len(g)}', )
                    for i in range(min_group_count):
                        group.members.set(students[i], through_defaults={"product": product.id})
