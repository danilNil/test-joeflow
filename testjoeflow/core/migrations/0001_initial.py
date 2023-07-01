# Generated by Django 4.2.1 on 2023-07-01 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joeflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailingWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='GatewayWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='LoopWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
                ('counter', models.PositiveIntegerField(default=0)),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('shipping_address', models.TextField()),
                ('tracking_code', models.TextField()),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='SimpleWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='SplitJoinWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
                ('parallel_task_value', models.PositiveIntegerField(default=0)),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='TestWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='WaitWorkflowState',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
                ('parallel_task_value', models.PositiveIntegerField(default=0)),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='WelcomeWorkflow',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('joeflow.workflow',),
        ),
    ]
