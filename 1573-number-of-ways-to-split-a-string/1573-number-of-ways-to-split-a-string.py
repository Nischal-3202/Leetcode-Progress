class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones=s.count('1')
        if total_ones % 3 != 0:
            return 0
        elif total_ones == 0:
            return (((len(s)-1)*(len(s)-2))/2) % (10**9+7)
        else:
            ones_partition=total_ones//3
            ones_seen=0
            first_cut_choices=0
            second_cut_choices=0
            for i in range(len(s)-1):
                if s[i]=='1':
                    ones_seen +=1
                if ones_seen == ones_partition:
                    first_cut_choices += 1
                if (ones_seen == 2*ones_partition) :
                    second_cut_choices += 1
            
            return (first_cut_choices*second_cut_choices) % (10**9+7)