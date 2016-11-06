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
        try:
            cls.pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
        except Exception, e:
            return "Erro ao Carregar Apuração, recarregue esse página"
        return "OK"

    @classmethod
    def report_total_votes(cls, candidates):
        c_array = candidates
        fig1 = plt.figure(figsize=(cls.width, 30))
        grid = GridSpec(3, 2)

        prefeito = [c for c in candidates if c.role == "Prefeito"]
        prefeito = cls.array_without_duplicate_candidate(prefeito)

        if len(prefeito) > 0:
            cls._plot_by_cargo(prefeito, grid, 0, 0, "Prefeito")

        vereador = [c for c in candidates if c.role == "Vereador"]
        vereador = cls.array_without_duplicate_candidate(vereador)
        if len(vereador) > 0:
            cls._plot_by_cargo(vereador, grid, 1, 0, "Vereador")

        governador = [c for c in candidates if c.role == "Governador"]
        governador = cls.array_without_duplicate_candidate(governador)
        if len(governador) > 0:
            cls._plot_by_cargo(governador, grid, 2, 0, "Governador")

        presidente = [c for c in candidates if c.role == "Presidente"]
        presidente = cls.array_without_duplicate_candidate(presidente)
        if len(presidente) > 0:
            cls._plot_by_cargo(presidente, grid, 0, 1, "Presidente")

        deputado = [c for c in candidates if c.role == "Deputado"]
        deputado = cls.array_without_duplicate_candidate(deputado)
        if len(deputado) > 0:
            cls._plot_by_cargo(deputado, grid, 1, 1, "Deputado")

        fig1.suptitle('Votos Totalizados por Cargo', fontsize=20, fontweight='bold')

        try:
            cls.pdf.savefig(fig1)
        except Exception, e:
            return "Erro ao Carregar Apuração, recarregue esse página"

        plt.close()
        return "OK"

    @classmethod
    def array_without_duplicate_candidate(cls, candidates):
        c_unique = []

        for c in candidates:
            if cls._find_in_candidate_array(c_unique, c.number) is not True:
                c_unique.append(c)
        return c_unique

    @classmethod
    def _find_in_candidate_array(cls, candidates, number):
        for c in candidates:
            if c.number == number:
                return True
        return False


    @classmethod
    def _plot_by_cargo(cls, candidates, grid, i, j, cargo):
        x_ind = np.arange(len(candidates))
        y_votes = [p.getTotalVotes() for p in candidates]
        names = [p.name for p in candidates]

        plt.subplot(grid[i, j], title="Cargo: {0}".format(cargo))
        random.shuffle(cls.colors)
        plt.bar(x_ind, y_votes, align='center', alpha=1, color=cls.colors)
        plt.xticks(x_ind, names, rotation='vertical')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    @classmethod
    def report_candidates_votes(cls, candidates, uevs):
        candidates = Reports._remove_candidate_without_votes(candidates)
        c_size = int((len(candidates) / 2) + 0.5)
        fig2 = plt.figure(figsize=(cls.width, 4.5 * c_size))
        grid = GridSpec(c_size, 2)

        flag = False

        if len(candidates) > 0:
            flag = True
            cls._get_candidate_pies(candidates, grid, c_size)

        fig2.suptitle('Votos x Uev', fontsize=20, fontweight='bold')

        if flag:
            try:
                cls.pdf.savefig(fig2)
            except Exception, e:
                return "Erro ao Carregar Apuração, recarregue esse página"

        plt.close()
        return "OK"

    @classmethod
    def report_no_show_voter(cls, voters):
        fig3 = plt.figure(figsize=(18, 70))
        fig3.suptitle('Eleitores Ausentes', fontsize=20, fontweight='bold', y=0.98)
        ax = fig3.add_subplot(111)
        ax.axis('off')

        column_name = ["Nome", "CPF", "Cidade"]
        data = [[voter.name, voter.cpf, voter.region.city] for voter in voters if
                voter.votedFlag is False or voter.votedFlag is 0]

        the_table = plt.table(cellText=data,
                              colWidths=[.3, .3, .3],
                              colLabels=column_name,
                              loc='center')

        table_props = the_table.properties()
        table_cells = table_props['child_artists']
        for cell in table_cells:
            cell.set_width(0.2)
            cell.set_height(0.004)
            cell._loc = 'left'

        try:
            cls.pdf.savefig(fig3, dpi=(200))
        except Exception, e:
            return "Erro ao Carregar Apuração, recarregue esse página"

        plt.close()
        return "OK"

    @staticmethod
    def _remove_candidate_without_votes(candidates):
        return [candidate for candidate in candidates if candidate.getTotalVotes() > 0]

    @classmethod
    def _get_candidate_pies(cls, candidates, grid, c_size):
        k = 0
        for i in np.arange(c_size):
            for j in np.arange(2):
                if k >= len(candidates):
                    return
                candidate = candidates[k]
                regions = [key for key, value in candidate.qntVotesPerUev.iteritems() if value > 0]
                percentages_regions = [value for key, value in candidate.qntVotesPerUev.iteritems() if value > 0]
                cls._extract_pie_subplot(candidate.role.upper() + ':' + candidate.name, i, j, percentages_regions,
                                         regions, grid)
                k += 1

    values = []

    @classmethod
    def _extract_pie_subplot(cls, title, i, j, percentages_regions, regions, grid):
        if len(regions) == 0:
            return -1
        explode = [0] * len(regions)
        explode[0] = 0.1
        plt.subplot(grid[i, j], title=title)
        cls.values = percentages_regions
        patches, texts, _ = plt.pie(percentages_regions, colors=cls.colors, autopct=cls._my_autopct,
                                    explode=explode, shadow=True, startangle=140)
        plt.legend(patches, regions, loc='center left', bbox_to_anchor=(0.75, 0.75))
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.axis("equal")

    @staticmethod
    def _my_autopct(pct):
        total = sum(Reports.values)
        val = int(pct * total / 100.0)
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    @classmethod
    def close_pdf(cls):
        try:
            cls.pdf.close()
        except Exception, e:
            return "Erro ao Carregar Apuração, recarregue esse página"
        return "output.pdf"
