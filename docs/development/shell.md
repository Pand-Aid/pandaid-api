# Using the manage.py shell

1. get a Docker shell, as specified in the README. 

Mac:

```
$ docker exec -ti pandaid-api_web_1 /bin/bash
```

Windows:

```bash
$ winpty docker exec -it pandaid-api_web_1 //bin/sh
```

2. use manage.py to get into the Django shell.

```bash
> python manage.py shell
```

3. Import the database models
```python
In [1]: from pandaid_base.models import *
```

4. try adding, editing, saving models e.g. 

```python 
bottle = Item(title="Baby bottle")
bottle.save()
formula_kit = Need(title="Baby formula kit")
formula_kit.save()
fk_needs_bottle = ItemNeed(item=bottle, need=formula_kit, quantity=3) 
# have to explicitly create instances of the through model = see https://stackoverflow.com/questions/31862599/how-to-save-a-manytomany-field-with-a-through-relationship
```

5. look at the results 
```python 
Item.objects.all()
# <QuerySet: [<Item: Baby bottle>]>
formula_kit.items
# <QuerySet: [<ItemNeed: 3 of Baby bottle for Baby formula kit>]>
```


6. try to dumpdata 

https://docs.djangoproject.com/en/3.0/ref/django-admin/#what-s-a-fixture