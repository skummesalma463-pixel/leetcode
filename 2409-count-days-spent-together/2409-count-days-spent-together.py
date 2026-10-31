class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        def to_days(date_str):
            m,d=map(int,date_str.split("-"))
            return sum(days[:m-1])+d
        start=max(to_days(arriveAlice),to_days(arriveBob))
        end=min(to_days(leaveAlice),to_days(leaveBob))
        return max(0,end-start+1)