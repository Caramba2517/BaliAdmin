import schedule
from statistic.signals import usd_statistic_query, rup_statistic_query, location_statistic_query, ads_statistic_query


def on_startup():
    def statistic_scheduler():
        ads_statistic_query()
        usd_statistic_query()
        rup_statistic_query()
        location_statistic_query()

    schedule.every().day.at('23:59').do(statistic_scheduler)
    while True:
        schedule.run_pending()
