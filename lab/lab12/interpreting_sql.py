from collections import namedtuple
from itertools import product


class Select:
    """select [columns] from [tables] where [condition] order by [order]."""

    def __init__(self, columns, tables, condition, order):
        self.columns = columns
        self.tables = tables
        self.condition = condition
        self.order = order
        self.make_row = create_make_row(self.columns)

    def execute(self, env):
        """Join, filter, sort, and map rows from tables to columns."""
        from_rows = join(self.tables, env)
        filtered_rows = filter(self.filter, from_rows)
        ordered_rows = self.sort(filtered_rows)
        return map(self.make_row, ordered_rows)

    def filter(self, row):
        if self.condition:
            return eval(self.condition, row)
        else:
            return True

    def sort(self, rows):
        if self.order:
            return sorted(rows, key=lambda r: eval(self.order, r))
        else:
            return rows


def create_make_row(description):
    """Return a function from an input environment (dict) to an output row.
    description -- a comma-separated list of [expression] as [ column name]
    """
    columns = description.split(", ")
    expressions, names = [], []
    for column in columns:
        if "as" in column:
            expression, name = column.split(" as ")
        else:
            expression, name = column, column
        expressions.append(expression)
        names.append(name)
    row = namedtuple("Row", names)
    return lambda env: row(*[eval(e, env) for e in expressions])


def join(tables, env):
    names = tables.split(", ")
    joined_rows = product(*[env[name] for name in names])
    return map(lambda rows: make_env(rows, names), joined_rows)


def make_env(rows, names):
    """Create an environment of names bound to values."""
    env = dict(zip(names, rows))
    for row in rows:
        for name in row._fields:
            env[name] = getattr(row, name)
    return env
