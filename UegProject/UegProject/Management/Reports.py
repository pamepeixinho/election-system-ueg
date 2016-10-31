import matplotlib.pyplot as plt
import numpy as np


class Reports(object):
    @staticmethod
    def report_total_votes(candidates):
        x_ind = np.arange(len(candidates))
        y_votes = [p.getTotalVotes() for p in candidates]
        names = [p.name for p in candidates]

        # plt.margins(0.1)
        plt.bar(x_ind, y_votes, align='center', alpha=0.4, color='r')
        plt.xticks(x_ind, names)
        plt.subplots_adjust(bottom=0.1)
        plt.title("Total Votes")
        plt.show()
        plt.savefig("/UevProject/CandidatesImages/plot.png")

        return 1
