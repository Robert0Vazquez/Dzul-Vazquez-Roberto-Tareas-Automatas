from traductorPyaJavaParser import *
from traductorPyaJavaListener import traductorPyaJavaListener

class InPyaJava(traductorPyaJavaListener):
    def __init__(self):
        self.java_code = []  # Aquí se almacenará el código traducido a Java
        self.class_name = ""  # Nombre de la clase
        self.func_name = ""  # Nombre de la función
        self.parameters = []  # Parámetros de la función
        self.argument_values = []  # Valores de los argumentos en print()

    # Método para obtener el código traducido
    def get_java_code(self):
        # Crear la estructura completa de la clase Java
        code = []
        code.append(f"public class {self.class_name} {{\n")  # Definir clase con nombre dinámico

        # Incluir la función traducida
        code.extend(self.java_code)

        # Incluir el método main con una llamada a la función y un ejemplo
        param_example = ', '.join(self.argument_values)  # Usar los valores capturados de los argumentos
        code.append(f"\n    public static void main(String[] args) {{")
        code.append(f"\n        // Llamada a la función {self.func_name} y mostrar el resultado")
        code.append(f"\n        System.out.println({self.func_name}({param_example}));")
        code.append(f"\n    }}")

        code.append(f"\n}}\n")  # Cierre de la clase
        return "\n".join(code)

    # Enter a parse tree produced by traductorPyaJavaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx: traductorPyaJavaParser.FunctionDefinitionContext):
        self.func_name = ctx.ID().getText()  # Obtener el nombre de la función
        self.class_name = self.func_name.capitalize()  # Usar el nombre de la función para la clase (capitalizado)
        
        params = [param.getText() for param in ctx.parameters().ID()]  # Obtener los parámetros
        self.parameters = params  # Guardar parámetros para usarlos después

        # Generar la declaración de la función en Java
        java_func = f"    public static int {self.func_name}({', '.join(['int ' + p for p in params])}) {{"
        self.java_code.append(java_func)

    def exitFunctionDefinition(self, ctx: traductorPyaJavaParser.FunctionDefinitionContext):
        self.java_code.append("    }")  # Cierra la función en Java

    # Enter a parse tree produced by traductorPyaJavaParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx: traductorPyaJavaParser.AssignmentStatementContext):
        var_name = ctx.ID().getText()  # Obtener el nombre de la variable
        expression = ctx.expression().getText()  # Obtener la expresión de asignación
        self.java_code.append(f"        int {var_name} = {expression};")

    # Enter a parse tree produced by traductorPyaJavaParser#returnStatement.
    def enterReturnStatement(self, ctx: traductorPyaJavaParser.ReturnStatementContext):
        return_expr = ctx.expression().getText()  # Obtener el valor de retorno
        self.java_code.append(f"        return {return_expr};")

    # Enter a parse tree produced by traductorPyaJavaParser#functionCall.
    def enterFunctionCall(self, ctx: traductorPyaJavaParser.FunctionCallContext):
        # Capturar los argumentos de la llamada a la función dentro de print
        if ctx.ID().getText() == self.func_name:
            args = [arg.getText() for arg in ctx.arguments().expression()]
            self.argument_values = args  # Guardar los valores de los argumentos

