from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_start = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.story.title} – {self.title}"

class Choice(models.Model):
    from_chapter = models.ForeignKey(
        Chapter,
        related_name='choices',
        on_delete=models.CASCADE
    )
    to_chapter = models.ForeignKey(
        Chapter,
        related_name='incoming_choices',
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=300)
    condition = models.CharField(max_length=300, blank=True)  # Beispiel: has_key == True
    effect = models.CharField(max_length=300, blank=True)     # Beispiel: karma = -1

    def __str__(self):
        return f"{self.from_chapter.title} → {self.to_chapter.title} : {self.text}"

class Variable(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    default_value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} = {self.default_value}"
