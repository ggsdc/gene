from abc import ABC
import numpy as np


class Individual(ABC):
    def __init__(
        self,
        genes: list = None,
        idx: int = None,
        parents: tuple = None,
        gene_length=0,
        encoding: str = "real",
    ):
        self._genes = genes
        self._idx = idx
        self.fitness = None
        self._hash = self.__hash__()
        self._gene_length = gene_length
        self._parents = parents
        self._encoding = encoding

    """
    Properties
    """

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, value: list = None):
        self._genes = np.array(value)

    @genes.deleter
    def genes(self):
        del self._genes

    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self, value):
        self._idx = value

    @idx.deleter
    def idx(self):
        del self._idx

    @property
    def gene_length(self):
        return self._gene_length

    @gene_length.setter
    def gene_length(self, value):
        self._gene_length = value

    @gene_length.deleter
    def gene_length(self):
        del self._gene_length

    @property
    def parents(self):
        return self._parents

    @parents.setter
    def parents(self, value):
        self._parents = value

    @parents.deleter
    def parents(self):
        del self._parents

    @property
    def encoding(self):
        return self._encoding

    @encoding.setter
    def encoding(self, value):
        self._encoding = value

    @encoding.deleter
    def encoding(self):
        del self._encoding

    """
    Methods of the individuals
    """

    def mutate(self, prob):
        pass

    def dominates(self):
        pass

    def create_random_genes(self):
        """
        Creates random genes for the individual
        """
        if self.encoding == "real":
            self.genes = np.random.uniform(
                low=0, high=1, size=self.gene_length
            ).tolist()
        elif self.encoding == "binary":
            self.genes = np.random.randint(
                low=0, high=2, size=self.gene_length
            ).tolist()

    """
    Class methods
    """

    @classmethod
    def create_individual(
        cls, idx: int = 0, gene_length: int = 0, encoding: str = "real"
    ):
        ind = cls(idx=idx, gene_length=gene_length, encoding=encoding)
        ind.create_random_genes()
        return ind

    """
    Internal methods
    """

    def __hash__(self):
        return hash(tuple(self._genes))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._hash == other._hash

    def same_genotype(self, other):
        if isinstance(other, self.__class__):
            return self._hash == other._hash

    def same_phenotype(self, other):
        if isinstance(other, self.__class__):
            return self.fitness == other.fitness

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness < other.fitness

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness <= other.fitness

    def __repr__(self):
        return f"Individual: {self.idx}"
