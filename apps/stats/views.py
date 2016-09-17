from collections import Counter
from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.response import Response

from aeupdates.utils.mongo_tools import get_mongo_db
from bson.json_util import dumps

from bson import ObjectId

def encoder(coursor):
    resp = {}
    for k, v in coursor.items():
        if isinstance(v, ObjectId):
            v = str(v)
        resp.update({k: v})
    return resp

USER_PRODUCT = 'gifgun'

def is_user_id(el):
    return el['user_id'].isdigit()


### TODO: Do not open connection to DB every time
class StatsViewSet(viewsets.ViewSet):

    def list_all_data_with_filters(self, filters_list=None):
        db = get_mongo_db()
        cursor = db.all_stats.find({'product': USER_PRODUCT})
        result = []
        for c in cursor:
            accepted = True
            if filters_list:
                for _filter in filters_list:
                    if not _filter(c):
                        accepted = False
                        break
            if accepted:
                result.append({str(c.get('_id')): encoder(c)})
        return result

    def _data_logins_by_user(self, data):
        aggregated_by_user = Counter()
        for record in data:
            # Only one element here
            for _, v in record.items():
                aggregated_by_user.update([v['user_id']])
        return aggregated_by_user

    def _data_logins_by_day(self, data, backtrack_days=180):
        aggregated_by_day = Counter()
        for record in data:
            for _, v in record.items():
                oldest_day = datetime.today() - timedelta(days=backtrack_days)
                _date = datetime.fromtimestamp(v['timestamp'] // 1000)
                if _date > oldest_day:
                    aggregated_by_day.update(['{year}-{month:02d}-{day:02d}'.format(year=_date.year,
                                                                                    month=_date.month,
                                                                                    day=_date.day)])
        # We sort keys by lexicographical order!
        # That's why only European format is acceptable ( Year-Month-Day )
        sorted_keys = sorted(list(aggregated_by_day))
        return [{key: aggregated_by_day[key]} for key in sorted_keys]

    def list(self, request):
        all = self.list_all_data_with_filters(filters_list=[is_user_id])
        aggregated_by_user = self._data_logins_by_user(all)
        aggregated_by_day = self._data_logins_by_day(all)
        return Response({'aggregated_by_user': aggregated_by_user,
                         'aggregated_by_day': aggregated_by_day,
                         })
