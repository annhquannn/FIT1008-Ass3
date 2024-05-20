from landsites import Land


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.total_adventurers = adventurers

    def _partition(self, arr: list[Land], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j].gold / arr[j].guardians >= pivot.gold / pivot.guardians if arr[j].guardians > 0 else 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(self, arr: list[Land], low: int, high: int) -> None:
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort(arr, low, pi - 1)
            self._quicksort(arr, pi + 1, high)

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
        """
        land.reward = new_reward
        land.guardians = new_guardians
