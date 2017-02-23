'''
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
'''
import requests
from colorama import init, Fore
from docopt import docopt
from prettytable import PrettyTable
import re




init()
class TrainCollection:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()
    def __init__(self,AvailableTrains,options):
        """查询到的火车班次集合

                :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                         火车班次是一个字典
                :param options: 查询的选项, 如高铁, 动车, etc...
                """
        self.AvailableTrains = AvailableTrains
        self.options = options
    def _get_duration(self,raw_train):
        duration=raw_train.get("lishi").replace(':',"小时")+"分"
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration
    def trains(self):
        for raw_train in self.AvailableTrains:
            train_no=raw_train["station_train_code"]
            inital=train_no[0].lower()
            if not self.options or inital in self.options:
                train=[
                    train_no,
                    '\n'.join([Fore.GREEN + raw_train['from_station_name'] + Fore.RESET,
                               Fore.RED + raw_train['to_station_name'] + Fore.RESET]),
                    '\n'.join([Fore.GREEN + raw_train['start_time'] + Fore.RESET,
                               Fore.RED + raw_train['arrive_time'] + Fore.RESET]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        trains=self.trains()
        for train in trains:
            pt.add_row(train)
        print(pt)

def getStations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
    response = requests.get(url, verify=False)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    return dict(stations)

def cli():
    '''command-line interface'''
    arguments=docopt(__doc__)
    stations=getStations()
    FromStation=stations.get(arguments['<from>'])
    ToStation=stations.get(arguments['<to>'])
    date=arguments['<date>']
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, FromStation, ToStation
    )
    options = ''.join([
                          key for key, value in arguments.items() if value is True
                          ])
    r = requests.get(url, verify=False)
    table= r.json()['data']
    available_trains =[x["queryLeftNewDTO"] for x in table]
    TrainCollection(available_trains, options).pretty_print()


cli()