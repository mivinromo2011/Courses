class Solution 
{
    public:
        void nextPermutation(vector<int>& nums)
        {
            int flag=0,n=nums.size();
            for(int i=1;i<n;i++)
                if(nums[i]>nums[i-1])
                {
                    flag=1;
                    break;
                }
            if(flag==0)
            {
                sort(nums.begin(),nums.end());
            }
            else
            {
                int m,p,s,j;
                m=nums[n-1];
                j=n-1;
                for(int i=n-2;i>=0;i--)
                {
                    if(nums[i]<m)
                    {
                        p=i;
                        break;
                    }
                    if(nums[i]>m)
                    { 
                        j=i;
                        m=nums[i];
                    }
                }
                for(int i=p+1;i<n;i++)
                {
                    if(nums[i]<m&&nums[i]>nums[p])
                    {
                        j=i;
                        m=nums[i];
                    }
                }
                swap(nums[p],nums[j]);
                vector<int>x;
                for(int i=p+1;i<n;i++)
                    x.push_back(nums[i]);
                sort(x.begin(),x.end());
                for(int i=p+1;i<n;i++)
                    nums[i]=x[i-p-1];
            }
        }
};