from django.db import models

class JobPosting(models.Model):
    """
    Represents a job posting.
    """
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        help_text="Title (e.g. position) for the job posting.",
    )
    description = models.TextField(
        max_length=2048,
        blank=True,
        help_text = "Long-format description for this job posting.",
    )
    posted = models.DateTimeField(auto_now_add=True, blank=True)
    location = models.ForeignKey('Office', blank=True, null=True)

    def __repr__(self):
        return self.title


class Office(models.Model):
    """
    Represents a location for a job posting.
    """
    name = models.CharField(
        max_length="100",
        db_index=True,
        help_text="Location name"
    )

    def __repr__(self):
        return self.name

