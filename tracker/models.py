from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(blank=False, max_length=50, null=False)
  description=models.TextField(blank=True)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name
  
  class Meta:
    db_table='project'
  

class Ticket(models.Model):
  STATUS_CHOICES=[
    ('OPEN', 'open'),
    ('CLOSED', 'closed'),
    ('IN PROGRESS', 'in progress'),
    ('RESOLVED', 'resolved')
  ]
  PRIORITY_CHOICES=[
      ('LOW', 'low'),
      ('MEDIUM','medium'),
      ('HIGH', 'high'),
      ('CRITICAL', 'critical'),
      ('BLOCKER', 'blocker')  
    ]

  title=models.CharField(blank=False, max_length=10, null=False)
  description= models.TextField()
  project=models.ForeignKey(Project, on_delete=models.CASCADE)
  status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
  priority=models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='HIGH')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title, self.status
  
  class Meta:
    db_table='ticket'