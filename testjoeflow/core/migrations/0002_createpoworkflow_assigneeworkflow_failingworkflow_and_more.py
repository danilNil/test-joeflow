# Generated by Django 4.2.1 on 2023-07-01 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joeflow', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePOWorkflow',
            fields=[
                ('workflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joeflow.workflow')),
            ],
            bases=('joeflow.workflow',),
        ),
        migrations.CreateModel(
            name='AssigneeWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.simpleworkflowstate',),
        ),
        migrations.CreateModel(
            name='FailingWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.failingworkflowstate',),
        ),
        migrations.CreateModel(
            name='GatewayWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.gatewayworkflowstate',),
        ),
        migrations.CreateModel(
            name='LoopWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.loopworkflowstate',),
        ),
        migrations.CreateModel(
            name='ShippingWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.shipment',),
        ),
        migrations.CreateModel(
            name='SimpleWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.simpleworkflowstate',),
        ),
        migrations.CreateModel(
            name='SplitJoinWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.splitjoinworkflowstate',),
        ),
        migrations.CreateModel(
            name='TestWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.testworkflowstate',),
        ),
        migrations.CreateModel(
            name='WaitWorkflow',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.waitworkflowstate',),
        ),
        migrations.CreateModel(
            name='CreatePO',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.createpoworkflow',),
        ),
    ]