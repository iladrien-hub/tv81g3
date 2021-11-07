import random

from django.core.management.base import BaseCommand, CommandError

from topics.models import ScientificDirector, BachelorTopic, Student


class Command(BaseCommand):
    help = 'Generates dummy data'

    @staticmethod
    def get_person(data):
        return random.choice(data["surnames"]), random.choice(data["names"]), random.choice(data["patronymics"]),

    def handle(self, *args, **options):
        bot_data = "./bot_data"
        self.stdout.write(self.style.SUCCESS("Loading Data..."))

        female = {}
        male = {}

        with open(f"{bot_data}/f_names.txt", encoding="utf-8") as f:
            female["names"] = f.read().strip().split("\n")

        with open(f"{bot_data}/f_surnames.txt", encoding="utf-8") as f:
            female["surnames"] = f.read().strip().split("\n")

        with open(f"{bot_data}/f_patronymics.txt", encoding="utf-8") as f:
            female["patronymics"] = f.read().strip().split("\n")

        with open(f"{bot_data}/m_names.txt", encoding="utf-8") as f:
            male["names"] = f.read().strip().split("\n")

        with open(f"{bot_data}/m_surnames.txt", encoding="utf-8") as f:
            male["surnames"] = f.read().strip().split("\n")

        with open(f"{bot_data}/m_patronymics.txt", encoding="utf-8") as f:
            male["patronymics"] = f.read().strip().split("\n")

        with open(f"{bot_data}/themes.txt", encoding="utf-8") as f:
            themes = f.read().strip().split("\n")

        names = (female, male)

        directors = []
        topics_generated = []

        self.stdout.write(self.style.SUCCESS("Generating directors..."))
        for _ in range(10):
            sur, nam, pat = Command.get_person(random.choice(names))
            self.stdout.write(self.style.SUCCESS(f"  - {sur} {nam} {pat}"))
            d = ScientificDirector(
                last_name=sur,
                first_name=nam,
                patronymic=pat,
            )
            d.save()
            directors.append(d)

        self.stdout.write(self.style.SUCCESS("Generating themes..."))
        for title in themes:
            year = random.randint(2000, 2021)
            director = random.choice(directors)
            self.stdout.write(self.style.SUCCESS(f"  - {title} {director} {year}"))
            topic = BachelorTopic(
                title=title,
                year=year,
                director=director
            )
            topic.save()
            topics_generated.append(topic)

            for _ in range(random.randint(1, 4)):
                sur, nam, pat = Command.get_person(random.choice(names))
                self.stdout.write(self.style.SUCCESS(f"   - {sur} {nam} {pat}"))
                student = Student(
                    last_name=sur,
                    first_name=nam,
                    patronymic=pat,
                    topic=topic
                )

                student.save()
