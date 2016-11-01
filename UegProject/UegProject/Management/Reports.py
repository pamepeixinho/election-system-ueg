# coding=utf-8
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib.gridspec import GridSpec


class Reports(object):
    pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
    colors = ['lightskyblue', '#624ea7', '#FF1493', 'gold', '#FF4500', 'yellowgreen', 'lightcoral']

    @classmethod
    def report_total_votes(cls, candidates, null_votes, white_votes):
        # return candidates
        x_ind = np.arange(len(candidates) + 2)
        y_votes = [p.getTotalVotes() for p in candidates]
        names = [p.name for p in candidates]

        y_votes.append(null_votes)
        y_votes.append(white_votes)

        names.append("Nulo")
        names.append("Branco")

        fig1 = plt.figure(figsize=(7, 5))

        random.shuffle(cls.colors)
        plt.bar(x_ind, y_votes, align='center', alpha=0.7, color=cls.colors)
        plt.xticks(x_ind, names)
        plt.subplots_adjust(bottom=0.1)
        plt.title("Total Votes")

        cls.pdf.savefig(fig1)

        plt.close()

    @classmethod
    def report_uev_votes(cls, candidates):
        fig2 = plt.figure(figsize=(8, 8))

        the_grid = GridSpec(len(candidates), 1)

        for i, candidate in enumerate(candidates):
            total_votes = candidate.getTotalVotes()

            regions = candidate.qntVotesPerRegion.keys()

            percentages_regions = [(value * 1.0 / total_votes) * 100
                                   for key, value in candidate.qntVotesPerRegion.iteritems()]

            explode = [0] * len(regions)
            explode[0] = 0.1

            random.shuffle(cls.colors)

            plt.subplot(the_grid[i, 0], title=candidate.name)

            patches, texts, _ = plt.pie(percentages_regions, colors=cls.colors, autopct='%1.1f%%',
                                        explode=explode, shadow=True, startangle=140)

            plt.legend(patches, regions, loc='best', bbox_to_anchor=(0.6, 0.5))

            plt.axis("equal")

        cls.pdf.savefig(fig2, title="Candidatos x Região (Uev)")

        plt.close()

    @classmethod
    def report_no_show_voter(cls, voters):
       return  1

    @classmethod
    def close_pdf(cls):
        cls.pdf.close()
