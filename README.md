# Deduplication script

### Intro
This program was developed in Feb 2020 for SEO purposes at my previous Marketing job.

The analysis of competitors' linkbuilding strategy meant going through tons of SEMrush csv reports, containing partly-replicated URLs and their Domain Authority (ex: 81 - google.com/currency, 74 - google.com/maps, and 50 - google.com/dollar/sign were represented as unique domains with varying Domain Authority).

I needed a tool which would make the selection of highest-ranking url and deletion of duplicates fast and easy. This is how the deduplication script appeared.

    ![Deduplication script with GUI screenshot](https://i.ibb.co/sKYNqmR/Screenshot-from-2020-06-13-11-15-53.png)

### How to use the script?:
- put the CSV file that you would like to deduplicate inside the script folder
- indicate the name of the csv file containing multiple URLs with different paths in the column #1
- indicate the name of the new csv file without duplicates, click 'RUN'
- the script will create a new file and populate it with the first occurence of each domain name 
