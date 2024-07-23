from dagster import MonthlyPartitionsDefinition
from ..constants import START_DATE, END_DATE

monthly_partitions = MonthlyPartitionsDefinition(
    start_date=START_DATE,
    end_date=END_DATE,
)
