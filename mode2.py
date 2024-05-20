from landsites import Land

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        Initializes the object and stores the number of adventurer teams in the game.

        Best Case: O(1) - Initializing with a fixed number of teams.
        Worst Case: O(1) - Initializing with a fixed number of teams.
        """
        self.n_teams = n_teams
        self.sites = []

    def add_sites(self, sites: list[Land]) -> None:
        """
        Stores and adds land sites to the object. If there are existing land sites
        already in the object, this method will append new land sites to the existing ones.

        Best Case: O(S) - Adding S new sites when the list is initially empty.
        Worst Case: O(S) - Adding S new sites to the existing list.
        """
        self.sites.extend(sites)


    def select_best_action(self, remaining_adventurers: int, sites: List[Land]) -> Tuple[Union[Land, None], int, float]:
        best_score = 2.5 * remaining_adventurers
        best_action = (None, 0, best_score)  # (site, adventurers, score)

        for site in sites:
            if site.guardians == 0:
                continue
            for send_adventurers in range(1, remaining_adventurers + 1):
                if send_adventurers <= site.guardians:
                    r = min(site.gold, send_adventurers * (site.gold / site.guardians))
                    score = 2.5 * (remaining_adventurers - send_adventurers) + r
                    if score > best_score:
                        best_score = score
                        best_action = (site, send_adventurers, score)
        
        return best_action

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Simulates a day of the game where each team selects a land site or skips their turn.
        
        Input: adventurer_size is the size of the adventurers for every team.
        Output: Returns a list of tuples, where each tuple represents the choices made by
                the first, second, third, ..., n_teams team leaders in order.
                Each tuple contains the land site chosen (or None) and the number of adventurers sent (or 0).

        Best Case: O(T * N) - T teams each making a selection from N sites with minimal adventurer options.
        Worst Case: O(T * N * A) - T teams each making a selection from N sites, considering up to A adventurers.
        """
        actions = []
        remaining_adventurers_list = [adventurer_size] * self.n_teams

        for i in range(self.n_teams):
            best_site, best_adventurers, _ = self.select_best_action(remaining_adventurers_list[i], self.sites)
            actions.append((best_site, best_adventurers))

            if best_site is not None:
                remaining_adventurers_list[i] -= best_adventurers

        return actions