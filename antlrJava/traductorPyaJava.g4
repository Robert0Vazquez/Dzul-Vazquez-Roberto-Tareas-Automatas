grammar traductorPyaJava;

// Tokens
DEF : 'def';                // Definición de funciones en Python
RETURN : 'return';          // Palabra clave return
LPAREN : '(';               // Paréntesis izquierdo
RPAREN : ')';               // Paréntesis derecho
COMMA : ',';                // Coma
COLON : ':';                // Dos puntos (usados en definiciones de funciones)
ASSIGN : '=';               // Operador de asignación
PLUS : '+';                 // Suma
MINUS : '-';                // Resta
MULTIPLY : '*';             // Multiplicación
DIVIDE : '/';               // División
ID : [a-zA-Z_][a-zA-Z0-9_]*; // Identificadores (variables, nombres de funciones)
Number : [0-9]+;            // Números
WS : [ \t\n\r]+ -> skip;    // Espacios en blanco

// Reglas de análisis sintáctico (parse rules)
program
    : functionDefinition+   // El programa puede tener una o más definiciones de funciones
    ;

functionDefinition
    : DEF ID LPAREN parameters RPAREN COLON block
    ;

parameters
    : ID (COMMA ID)*        // Lista de parámetros, separados por comas
    ;

block
    : statement+            // Un bloque está compuesto por una o más sentencias
    ;

statement
    : expressionStatement   // Sentencias pueden ser expresiones
    | returnStatement       // O declaraciones de retorno
    | assignmentStatement   // O asignaciones de variables
    ;

assignmentStatement
    : ID ASSIGN expression  // Asignación de una variable con cualquier expresión
    ;

expressionStatement
    : expression
    ;

returnStatement
    : RETURN expression
    ;

expression
    : functionCall                       // Una expresión puede ser una llamada a función
    | term ((PLUS | MINUS) term)*        // O una operación de suma/resta
    ;

term
    : factor ((MULTIPLY | DIVIDE) factor)* // Expresiones con multiplicación/división
    ;

factor
    : ID                                // Un factor puede ser un identificador
    | Number                            // O un número
    | LPAREN expression RPAREN           // O una expresión entre paréntesis
    ;

// Nueva regla para llamadas a funciones
functionCall
    : ID LPAREN arguments RPAREN         // Una llamada a función con argumentos
    ;

// Nueva regla para la lista de argumentos en una función
arguments
    : expression (COMMA expression)*     // Lista de argumentos separados por comas
    ;
