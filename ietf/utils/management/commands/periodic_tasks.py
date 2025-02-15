# Copyright The IETF Trust 2024, All Rights Reserved
import json
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from django.core.management.base import BaseCommand

CRONTAB_DEFS = {
    # same as "@weekly" in a crontab
    "weekly": {
        "minute": "0",
        "hour": "0",
        "day_of_month": "*",
        "month_of_year": "*",
        "day_of_week": "0",
    },
    "daily": {
        "minute": "5",
        "hour": "0",
        "day_of_month": "*",
        "month_of_year": "*",
        "day_of_week": "*",
    },
    "hourly": {
        "minute": "5",
        "hour": "*",
        "day_of_month": "*",
        "month_of_year": "*",
        "day_of_week": "*",
    },
    "every_15m": {
        "minute": "*/15",
        "hour": "*",
        "day_of_month": "*",
        "month_of_year": "*",
        "day_of_week": "*",
    },
}


class Command(BaseCommand):
    """Manage periodic tasks"""
    crontabs = None

    def add_arguments(self, parser):
        parser.add_argument("--create-default", action="store_true")
        parser.add_argument("--enable", type=int, action="append")
        parser.add_argument("--disable", type=int, action="append")

    def handle(self, *args, **options):
        self.crontabs = self.get_or_create_crontabs()
        if options["create_default"]:
            self.create_default_tasks()
        if options["enable"]:
            self.enable_tasks(options["enable"])
        if options["disable"]:
            self.disable_tasks(options["disable"])
        self.show_tasks()

    def get_or_create_crontabs(self):
        crontabs = {}
        for label, definition in CRONTAB_DEFS.items():
            crontabs[label], _ = CrontabSchedule.objects.get_or_create(**definition)
        return crontabs

    def create_default_tasks(self):
        PeriodicTask.objects.get_or_create(
            name="Send scheduled mail",
            task="ietf.message.tasks.send_scheduled_mail_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["every_15m"],
                description="Send mail scheduled to go out at certain times"
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Partial sync with RFC Editor index",
            task="ietf.sync.tasks.rfc_editor_index_update_task",
            kwargs=json.dumps(dict(full_index=False)),
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["every_15m"],
                description=(
                    "Reparse the last _year_ of RFC index entries until "
                    "https://github.com/ietf-tools/datatracker/issues/3734 is addressed. "
                    "This takes about 20s on production as of 2022-08-11."
                )
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Full sync with RFC Editor index",
            task="ietf.sync.tasks.rfc_editor_index_update_task",
            kwargs=json.dumps(dict(full_index=True)),
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["daily"],
                description=(
                    "Run an extended version of the rfc editor update to catch changes with backdated timestamps"
                ),
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Fetch meeting attendance",
            task="ietf.stats.tasks.fetch_meeting_attendance_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["daily"],
                description="Fetch meeting attendance data from ietf.org/registration/attendees",
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Send review reminders",
            task="ietf.review.tasks.send_review_reminders_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["daily"],
                description="Send reminders originating from the review app",
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Expire I-Ds",
            task="ietf.doc.tasks.expire_ids_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["daily"],
                description="Create expiration notices for expired I-Ds",
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Sync with IANA changes",
            task="ietf.sync.tasks.iana_changes_update_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["hourly"],
                description="Fetch change list from IANA and apply to documents",
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Sync with IANA protocols page",
            task="ietf.sync.tasks.iana_changes_update_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["hourly"],
                description="Fetch protocols page from IANA and update document event logs",
            ),
        )

        PeriodicTask.objects.get_or_create(
            name="Update I-D index files",
            task="ietf.idindex.tasks.idindex_update_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["hourly"],
                description="Update I-D index files",
            ),
        )
        
        PeriodicTask.objects.get_or_create(
            name="Send expiration notifications",
            task="ietf.doc.tasks.notify_expirations_task",
            defaults=dict(
                enabled=False,
                crontab=self.crontabs["weekly"],
                description="Send notifications about I-Ds that will expire in the next 14 days",
            )
        )

    def show_tasks(self):
        for label, crontab in self.crontabs.items():
            tasks = PeriodicTask.objects.filter(crontab=crontab).order_by(
                "task", "name"
            )
            self.stdout.write(f"\n{label} ({crontab.human_readable})\n")
            if tasks:
                for task in tasks:
                    desc = f"  {task.id:-3d}: {task.task} - {task.name}"
                    if task.enabled:
                        self.stdout.write(desc)
                    else:
                        self.stdout.write(self.style.NOTICE(f"{desc} - disabled"))
            else:
                self.stdout.write("  Nothing scheduled")

    def enable_tasks(self, pks):
        PeriodicTask.objects.filter(
            crontab__in=self.crontabs.values(), pk__in=pks
        ).update(enabled=True)

    def disable_tasks(self, pks):
        PeriodicTask.objects.filter(
            crontab__in=self.crontabs.values(), pk__in=pks
        ).update(enabled=False)
