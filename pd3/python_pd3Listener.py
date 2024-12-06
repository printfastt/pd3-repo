# Generated from python_pd3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .python_pd3Parser import python_pd3Parser
else:
    from python_pd3Parser import python_pd3Parser

# This class defines a complete listener for a parse tree produced by python_pd3Parser.
class python_pd3Listener(ParseTreeListener):

    # Enter a parse tree produced by python_pd3Parser#program.
    def enterProgram(self, ctx:python_pd3Parser.ProgramContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#program.
    def exitProgram(self, ctx:python_pd3Parser.ProgramContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#statement.
    def enterStatement(self, ctx:python_pd3Parser.StatementContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#statement.
    def exitStatement(self, ctx:python_pd3Parser.StatementContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#assignment.
    def enterAssignment(self, ctx:python_pd3Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#assignment.
    def exitAssignment(self, ctx:python_pd3Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#if_block.
    def enterIf_block(self, ctx:python_pd3Parser.If_blockContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#if_block.
    def exitIf_block(self, ctx:python_pd3Parser.If_blockContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#elif_clause.
    def enterElif_clause(self, ctx:python_pd3Parser.Elif_clauseContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#elif_clause.
    def exitElif_clause(self, ctx:python_pd3Parser.Elif_clauseContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#else_clause.
    def enterElse_clause(self, ctx:python_pd3Parser.Else_clauseContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#else_clause.
    def exitElse_clause(self, ctx:python_pd3Parser.Else_clauseContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#while_loop.
    def enterWhile_loop(self, ctx:python_pd3Parser.While_loopContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#while_loop.
    def exitWhile_loop(self, ctx:python_pd3Parser.While_loopContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#for_loop.
    def enterFor_loop(self, ctx:python_pd3Parser.For_loopContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#for_loop.
    def exitFor_loop(self, ctx:python_pd3Parser.For_loopContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#block.
    def enterBlock(self, ctx:python_pd3Parser.BlockContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#block.
    def exitBlock(self, ctx:python_pd3Parser.BlockContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#expression.
    def enterExpression(self, ctx:python_pd3Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#expression.
    def exitExpression(self, ctx:python_pd3Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#condition.
    def enterCondition(self, ctx:python_pd3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#condition.
    def exitCondition(self, ctx:python_pd3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#list.
    def enterList(self, ctx:python_pd3Parser.ListContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#list.
    def exitList(self, ctx:python_pd3Parser.ListContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#iterable.
    def enterIterable(self, ctx:python_pd3Parser.IterableContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#iterable.
    def exitIterable(self, ctx:python_pd3Parser.IterableContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#comparison.
    def enterComparison(self, ctx:python_pd3Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#comparison.
    def exitComparison(self, ctx:python_pd3Parser.ComparisonContext):
        pass



del python_pd3Parser