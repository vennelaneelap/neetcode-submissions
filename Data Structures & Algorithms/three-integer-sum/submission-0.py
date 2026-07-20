from typing import List  # Import List for the function's input and output types.


class Solution:  # Create the class required by LeetCode.

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Define the function that returns unique triplets.

        nums.sort()
        # Sort the array so the two-pointer method works.

        outputs = set()
        # Use a set so duplicate triplets are stored only once.

        for i in range(len(nums) - 2):
            # Select nums[i] as the first number of the triplet.

            left = i + 1
            # Place the left pointer immediately after i.

            right = len(nums) - 1
            # Place the right pointer at the final index.

            while left < right:
                # Continue until the pointers meet.

                curr_sum = nums[i] + nums[left] + nums[right]
                # Calculate the sum of the three current numbers.

                if curr_sum == 0:
                    # Check whether the three numbers add up to zero.

                    outputs.add((nums[i], nums[left], nums[right]))
                    # Add a tuple because sets cannot store lists.
                    # The set automatically prevents duplicate triplets.

                    left += 1
                    # Move the left pointer forward to search for another triplet.

                    right -= 1
                    # Move the right pointer backward to search for another triplet.

                elif curr_sum < 0:
                    # If the sum is too small, we need a larger number.

                    left += 1
                    # Move left forward because the array is sorted.

                else:
                    # If the sum is too large, we need a smaller number.

                    right -= 1
                    # Move right backward because the array is sorted.

        answer = []
        # Create the final list required by LeetCode.

        for triplet in outputs:
            # Visit every unique tuple in the set.

            answer.append(list(triplet))
            # Convert the tuple back into a list.

        return answer
        # Return the unique triplets.