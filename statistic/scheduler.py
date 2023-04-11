import schedule
import datetime
from statistic.signals import usd_statistic_query, rup_statistic_query, location_statistic_query, ads_statistic_query, \
    google_sheets


def on_startup():
    def statistic_scheduler():
        ads_statistic_query()
        usd_statistic_query()
        rup_statistic_query()
        location_statistic_query()
        google_sheets()
        print(f'Задача выполнена. Время выполнения: {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}')
    schedule.every().day.at("23:55").do(statistic_scheduler)
    while True:
        schedule.run_pending()


on_startup()
