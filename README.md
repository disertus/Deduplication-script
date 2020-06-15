# Deduplication script

### Intro
This is my very first program, that was developed in Feb 2020 for SEO purposes at my previous Marketing job.

The analysis of competitors' linkbuilding strategy meant going through tons of SEMrush csv reports, containing partly-duplicated URLs and their Domain Authority (ex: 81 - google.com/currency, 74 - google.com/maps, and 50 - google.com/dollar/sign were represented as unique domains with varying Domain Authority).

I needed an easy-to-use tool which could be used by others, and would make the selection of highest-ranking urls by domain and deletion of thousands of long-tail duplicates fast and easy (avoiding manual work). This is how the deduplication script appeared.

Input:

   ![Deduplication script with GUI screenshot](https://i.ibb.co/fXGFdRk/Screenshot-from-2020-06-13-11-50-28.png)
   
Result:

![Deduplication result](https://i.ibb.co/6NhLBv6/Screenshot-from-2020-06-13-11-44-02.png)

### How to use the script?:
- put the CSV file that you would like to deduplicate inside the script folder
- indicate the name of the csv file containing partly duplicated URLs in the column #1
- indicate the name of the new csv file without duplicates, click 'RUN'
- the script will create a new file and populate it with the first occurence of each domain name 
