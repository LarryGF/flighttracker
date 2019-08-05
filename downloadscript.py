import requests
import click
import json

def get_info(airport, date, time):
    url = f'https://www.flightstats.com/v2/api-next/flight-tracker/dep/{airport}/{date}/{time}'

    try:
        r = requests.get(url)
        return r.json()

    except ConnectionError:
        print('2- site not reachable')
        exit(2)

    except:
        print('0 - fail')
        exit(0)


@click.command()
@click.option('--airport_name', default='HAV', help='airport name mean airport code for example HAV for havana international airport')
@click.option('--date', default='2019/08/6', help='date in format year/month/day')
@click.option('--time', default= 1, help="""
"time"
1. 6AM-12PM
2. 12PM - 6PM
3. 6pm - 12AM
4. 12AM-6AM
5. All
""")

@click.option('--output_option', default= 1, help="""
output option:
1 - standard output
2 - file json
3 - standard output then file json
""")
def extract(airport_name, date, time, output_option):

    ans = []

    if time < 5:
        data = get_info(airport_name, date, (time % 4) * 6)

    else:
        data = [get_info(airport_name, date, (i % 4) * 6) for i in range(1,5)]

    data = json.dumps(data, ensure_ascii=False, indent=2)
    if output_option == 1:
        print(data)

    if output_option == 2:
        open('data.json','w').write(data)
        exit(3)


    if output_option == 3:
        print(data)
        open('data.json','w').write(data)

    exit(1)

if __name__=='__main__':
    extract()