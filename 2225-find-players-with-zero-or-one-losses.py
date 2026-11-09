
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loser_dict = {}
        all_player = set()

        for winner, loser in matches:
            all_player.add(winner)
            all_player.add(loser)

            loser_dict[loser] = loser_dict.get(loser, 0) + 1

        no_loss = []
        exactly_one = []

        for player in all_player:
            if player not in loser_dict:
                no_loss.append(player)
            elif loser_dict[player] == 1:
                exactly_one.append(player)

        return [sorted(no_loss), sorted(exactly_one)]