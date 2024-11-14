from antlr4 import *
from traductorPyaJavaLexer import traductorPyaJavaLexer
from traductorPyaJavaParser import traductorPyaJavaParser
from InPyaJava import InPyaJava

def main():
    in_morse_line = input('File name> ')
    # Leer archivo de entrada
    with open(in_morse_line) as file:
        lexer = traductorPyaJavaLexer(InputStream(file.read()))
        t_stream = CommonTokenStream(lexer)

        parser = traductorPyaJavaParser(t_stream)
        tree = parser.program()

        # Usar el Listener para convertir el código
        listener = InPyaJava()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        
         # Obtener el nombre de la función para usarlo como nombre de archivo
        nombre_funcion = listener.func_name.capitalize()  # Capitalizar el nombre de la función para el archivo

        # Guardar el código traducido a un archivo .java
        with open(f"{nombre_funcion}.java", "w") as f:
            f.write(listener.get_java_code())

if __name__ == '__main__':
    main()
