class Solution:
 def maximumSubarraySum(self,nums:list[int],k:int)->int:
  n=len(nums)
  max_sum=0
  current_sum=0
  count_map={}
  for i in range(n):
   num=nums[i]
   current_sum+=num
   count_map[num]=count_map.get(num,0)+1
   if i>=k:
    left_num=nums[i-k]
    current_sum-=left_num
    count_map[left_num]-=1
    if count_map[left_num]==0:
     del count_map[left_num]
   if i>=k-1:
    if len(count_map)==k:
     max_sum=max(max_sum,current_sum)
  return max_sum