import schedule

from statistic.signals import usd_statistic_query, rup_statistic_query, location_statistic_query, ads_statistic_query, \
    google_sheets


def on_startup():
    def statistic_scheduler():
        print("выполнение началось")
        ads_statistic_query()
        usd_statistic_query()
        rup_statistic_query()
        location_statistic_query()
        google_sheets()

    schedule.every().day().at('23:55').do(statistic_scheduler)
    while True:
        schedule.run_pending()


on_startup()
