from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], cooldown_period: int) -> int:
        # Count the frequency of each task
        task_frequencies = {}  
        for task in tasks:
            if task in task_frequencies:
                task_frequencies[task] += 1
            else:
                task_frequencies[task] = 1

        # Sort frequencies in descending order
        sorted_frequencies = sorted(task_frequencies.values(), reverse=True)
        max_frequency = sorted_frequencies[0]

        # Count how many tasks share the maximum frequency
        max_freq_task_count = 0
        for freq in sorted_frequencies:
            if freq == max_frequency:
                max_freq_task_count += 1
            else:
                break  # Stop early since the list is sorted

        # Calculate the minimum intervals required by the formula
        chunks = max_frequency - 1
        chunk_length = cooldown_period + 1
        scheduled_intervals = chunks * chunk_length + max_freq_task_count
        
        # Total intervals cannot be less than the actual number of tasks
        return max(scheduled_intervals, len(tasks))