import ast
import operator as op


class ProblemSolver:
    operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                 ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
                 ast.USub: op.neg}

    def solve_problem(self, expression):
        """
        :param expression: string math problem
        :return: value as float, int, or fraction
        """

        return self.evaluate(ast.parse(expression, mode='eval').body)

    def evaluate(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            try:
                return self.operators[type(node.op)](self.evaluate(node.left), self.evaluate(node.right))
            except ZeroDivisionError:
                return "N/A"
        elif isinstance(node, ast.UnaryOp):
            return self.operators[type(node.op)](self.evaluate(node.operand))
        else:
            raise TypeError(node)
