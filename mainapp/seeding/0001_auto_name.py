from seeding.seeding import BaseSeeding

from mainapp.models import CoursesTeacher


class Seeding(BaseSeeding):

    def seeding(self):
        """ Seeding data in project """
     
        CoursesTeacher.objects.create(
            name_first="Альфред",
            name_second="Нуцубидзе",
            day_birth="1990-07-10",
            course=[1, 3],
        )
                 

    def rollback(self):
        """ Remove seeded data from project  """
        pass
