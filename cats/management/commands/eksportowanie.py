from django.core.management import BaseCommand
from django.db.models import Max
from cats.models import Hunting, Cat
import csv

class Command(BaseCommand):
    def add_arguments(self, parser): 
        parser.add_argument("-k", "--kot", 
            help="Wybor kota", 
            default=1, 
            type=str)

    def handle(self, *args, **options):
        cat = (
            Cat.objects.filter(cat_name=options['kot'])
            .aggregate(num=Max("id"))
            .get("num")
        )
        hunting = (
            Hunting.objects.filter(cat_id=cat).count()
        )
        cat1 = (
            Cat.objects.filter(cat_name=options['kot'])
            .values_list('cat_name')
        )
        f = open('plik.csv', 'w')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Imię kota', 'Liczba polowań'])
        for name in cat1:
            csv_writer.writerow([name, hunting])
   
    