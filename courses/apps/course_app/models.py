from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors['name'] = 'Course name to be more than 5 characters.'
        if len(postData['desc']) <= 15:
            errors['desc'] = 'The description to be more than 15 characters.'
        return errors

class Description(models.Model):
    content = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Description, related_name='course')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __str__(self):
        return 'Course: %s' % self.name

class Comment(models.Model):
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text[:10]



