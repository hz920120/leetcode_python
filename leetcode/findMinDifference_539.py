from datetime import datetime


class Solution(object):
    def __init__(self):
        self.fmt = '%Y%m%d %H:%M'

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints.sort()


    def calDistance(self, time1, time2):
        t1 = datetime.strftime(time1, self.fmt)
        t2 = datetime.strftime(time2, self.fmt)

        return (t2 - t1).total_seconds() / 60.0


    def getDifference(self, time1, time2):
        time1.replace()



if __name__ == '__main__':
    s = Solution()
    out = s.calDistance('20000101 23:23', '00:00')
    print(out)