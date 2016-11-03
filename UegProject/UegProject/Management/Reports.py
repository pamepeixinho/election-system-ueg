# -*- coding: utf-8 -*-
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import numpy as np
import random

from matplotlib.gridspec import GridSpec


class Reports(object):
    pdf = None
    colors = ['lightskyblue', '#624ea7', '#FF1493', 'gold', '#FF4500', 'yellowgreen', 'lightcoral']

    width = 20
    height = 18

    @classmethod
    def initPdf(cls):
        cls.pdf = None
        cls.pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")

    @classmethod
    def report_total_votes(cls, candidates, null_votes, white_votes):
        # return candidates
        x_ind = np.arange(len(candidates) + 2)
        y_votes = [p.getTotalVotes() for p in candidates]
        names = [p.name for p in candidates]

        y_votes.append(null_votes)
        y_votes.append(white_votes)

        names.append("NULO")
        names.append("BRANCO")

        fig1 = plt.figure(figsize=(cls.width, cls.height))

        random.shuffle(cls.colors)
        plt.bar(x_ind, y_votes, align='center', alpha=1, color=cls.colors)
        plt.xticks(x_ind, names, rotation='vertical')
        plt.subplots_adjust(bottom=0.1)
        plt.title("Total Votos", fontsize=20, fontweight='bold')

        cls.pdf.savefig(fig1)

        plt.close()

    @classmethod
    def report_uev_votes(cls, candidates, uevs, total_null_votes, total_white_votes):
        fig2 = plt.figure(figsize=(cls.width, 4.5 * len(candidates)))
        grid = GridSpec(len(candidates), 2)

        if len(candidates) > 0:
            cls._get_candidate_pies(candidates, grid)
            cls._get_null_pie(uevs, total_null_votes, grid)
            cls._get_white_pie(uevs, total_white_votes, grid)
            fig2.suptitle('Votos x Uev', fontsize=20, fontweight='bold')
            cls.pdf.savefig(fig2)

        plt.close()

    # TODO fix grid layout
    @classmethod
    def _get_candidate_pies(cls, candidates, grid):
        for i, candidate in enumerate(candidates):
            total_votes = candidate.getTotalVotes()

            if total_votes == 0:
                pass

            regions = candidate.qntVotesPerUev.keys()

            percentages_regions = [value
                                   for key, value in candidate.qntVotesPerUev.iteritems()]

            cls.extract_pie_subplot('Candidato: ' + candidate.name, i, 0, percentages_regions, regions, grid)

    @classmethod
    def _get_null_pie(cls, uevs, total_votes, grid):
        if total_votes == 0:
            return
        regions = [uev.username for uev in uevs]
        percentages_regions = [uev.null_votes for uev in uevs]
        cls.extract_pie_subplot("Votos Nulos", 1, 1, percentages_regions, regions, grid)

    @classmethod
    def _get_white_pie(cls, uevs, total_votes, grid):
        if total_votes == 0:
            return
        regions = [uev.username for uev in uevs]
        percentages_regions = [uev.white_votes for uev in uevs]
        cls.extract_pie_subplot("Votos em branco", 2, 1, percentages_regions, regions, grid)

    values = []

    @staticmethod
    def my_autopct(pct):
        total = sum(Reports.values)
        val = int(pct * total / 100.0)
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    @classmethod
    def extract_pie_subplot(cls, title, i, j, percentages_regions, regions, grid):
        if len(regions) == 0:
            return -1
        explode = [0] * len(regions)
        explode[0] = 0.1
        random.shuffle(cls.colors)
        plt.subplot(grid[i, j], title=title)
        cls.values = percentages_regions
        patches, texts, _ = plt.pie(percentages_regions, colors=cls.colors, autopct=cls.my_autopct,
                                    explode=explode, shadow=True, startangle=140)
        plt.legend(patches, regions, loc='center left', bbox_to_anchor=(0.75, 0.75))
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.axis("equal")
        return 1

    @classmethod
    def report_no_show_voter(cls, voters):
        fig3 = plt.figure(figsize=(cls.width, cls.height+25))
        fig3.suptitle('Eleitores Ausentes', fontsize=20, fontweight='bold')
        t = 0.97
        # TODO FIX this method
        for voter in voters:
            if voter.votedFlag is False or voter.votedFlag is 0:
                fig3.text(.2, t, voter.name + " - " + str(voter.cpf), fontsize=12)
                t -= 0.005

        cls.pdf.savefig(fig3)
        plt.close()

    @classmethod
    def close_pdf(cls):
        cls.pdf.close()
        return "output.pdf"
