from landsites import Land


class Mode1Navigator:
    """
    Mode1Navigator facilitates navigation and decision-making for adventurers in mode 1.

    Approach Details:

    Data Structures and Data Types Used:
    - This class primarily utilizes a list to store instances of the Land class, representing different sites, and integers to represent the total number of adventurers and other numeric values associated with sites.

    Small Example:
    navigator = Mode1Navigator(sites=[Land("Forest", guardians=20, gold=100), Land("Mountain", guardians=15, gold=200)], adventurers=50)
    selected_sites = navigator.select_sites()
    print(selected_sites)

    Explanation of Complexity:
    - The _partition method partitions the array based on the ratio of gold to guardians, aiming to achieve balanced partitions.
    - Best Case: When the pivot consistently divides the array into roughly equal parts, the time complexity of quicksort is O(n log n). Subsequently, the loop in select_sites iterates over the sorted sites once, resulting in a linear time complexity of O(n). Therefore, the overall best-case time complexity is O(n log n).
    - Worst Case: If the pivot consistently results in highly unbalanced partitions, quicksort degrades to O(n^2). However, the subsequent linear loop in select_sites still dominates the time complexity, making it O(n^2) overall due to the sorting algorithm.
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Initializes the Mode2Navigator with a list of land sites and the total number of adventurers.
    
        Best Case: O(1) - Initializing with a list of land sites and a fixed number of adventurers.
        Worst Case: O(1) - Initializing with a list of land sites and a fixed number of adventurers.
        """
        self.sites = sites
        self.total_adventurers = adventurers

    def _partition(self, arr: list[Land], low: int, high: int) -> int:
        """
        Partitions the array around a pivot element such that elements greater than or equal to the pivot
        are on the left of the pivot and elements less than the pivot are on the right.

        Best Case: O(n) - The pivot is always the median or near the median, leading to balanced partitions.
        Worst Case: O(n) - The pivot is always the smallest or largest element, leading to unbalanced partitions.

        Args:
            arr (list[Land]): The list of Land objects to be partitioned.
            low (int): The starting index of the sublist to be partitioned.
            high (int): The ending index of the sublist to be partitioned.

        Returns:
            int: The index position of the pivot element after partitioning.
        """
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j].gold / arr[j].guardians >= pivot.gold / pivot.guardians if arr[j].guardians > 0 else 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(self, arr: list[Land], low: int, high: int) -> None:
        """
        Sorts the sites based on the number of guardians using the quicksort algorithm.

        The best-case scenario for quicksort occurs when the pivot chosen at each step divides the array into two roughly equal parts. 
        In this case, the algorithm's runtime complexity is O(nlogn).

        The worst-case scenario happens when the pivot is either the smallest or largest element in the array at each step. 
        This results in one partition having n-1 elements and the other partition having 0 elements. 
        In such a scenario, the runtime complexity is O(n^2).
        """
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort(arr, low, pi - 1)
            self._quicksort(arr, pi + 1, high)

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Selects sites to send adventurers based on the number of guardians and the total number of adventurers.

        Best Case: 
        The best-case scenario occurs when the array of sites is already sorted or nearly sorted, leading to balanced partitions during quicksort. 
        In this case, the time complexity of quicksort is O(n log n). 
        Subsequently, the loop iterates over the sorted sites once, resulting in a linear time complexity of O(n). 
        Therefore, the overall best-case time complexity is O(n log n).

        Worst Case:
        The worst-case scenario arises when the array is sorted in reverse order, causing quicksort to create highly unbalanced partitions. 
        This results in a time complexity of O(n^2) for the sorting algorithm. 
        However, the subsequent linear loop in select_sites still dominates the time complexity, making it O(n^2) overall due to the sorting algorithm.
        """
        self._quicksort(self.sites, 0, len(self.sites) - 1)
        result = []
        remaining_adventurers = self.total_adventurers

        for site in self.sites:
            if remaining_adventurers == 0:
                break
            send_adventurers = min(remaining_adventurers, site.guardians)
            result.append((site, send_adventurers))
            remaining_adventurers -= send_adventurers

        return result

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Calculates the total rewards for a list of adventure numbers by distributing adventurers to sites based on guardians.

        Best Case:
            The best-case scenario occurs when the number of adventurers exactly matches the number of guardians in each iteration, ensuring that the loop breaks early. 
            The time complexity is O(n) for iterating over the adventure numbers, and for each adventure number, it is O(m), where m is the number of sites. 
            Therefore, the overall best-case time complexity is O(n * m).

    Worst Case:
            The worst-case scenario occurs when the number of adventurers does not match the guardians perfectly, requiring full iteration through all sites for each adventure number. 
            This results in a time complexity of O(n) for iterating over the adventure numbers, and for each adventure number, it is O(m), where m is the number of sites. 
            Therefore, the overall worst-case time complexity is O(n * m).
    """
        rewards = []

        for adventurers in adventure_numbers:
            total_reward = 0
            for site in self.sites:
                send_adventurers = min(adventurers, site.guardians)
                reward = min(site.gold, send_adventurers * (site.gold / site.guardians)) if site.guardians > 0 else 0
                total_reward += reward
                adventurers -= send_adventurers
                if adventurers == 0:
                    break
            rewards.append(total_reward)

        return rewards


    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Updates the reward and guardians for a given site.

        Best Case:
            The best-case scenario occurs when the site is updated in constant time without any additional operations. 
            The time complexity is O(1).

        Worst Case:
            The worst-case scenario is identical to the best case because updating the attributes of an object is always done in constant time. 
            The time complexity is O(1).
    """
        land.reward = new_reward
        land.guardians = new_guardians
