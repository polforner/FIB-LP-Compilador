from antlr4 import *
from funxLexer import funxLexer
from funxParser import funxParser
from EvalVisitor import EvalVisitor
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html', tfs=visitor.tfs, inputs_and_outputs=inputs_and_outputs)


@app.route('/evaluate', methods=['POST'])
def evaluate():
    expression = request.form['funx_expression']
    input_stream = InputStream(expression)
    lexer = funxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = funxParser(token_stream)
    tree = parser.root()
    try:
        result = visitor.visit(tree)
    except Exception as e:
        result = e
    del inputs_and_outputs[0]
    inputs_and_outputs.append((input_stream, result))
    return render_template('base.html', result=result, tfs=visitor.tfs, inputs_and_outputs=inputs_and_outputs)


visitor = EvalVisitor([{}], {})

inputs_and_outputs = [('', ''), ('', ''), ('', ''), ('', ''), ('', '')]

if __name__ == '__main__':
    app.run()
