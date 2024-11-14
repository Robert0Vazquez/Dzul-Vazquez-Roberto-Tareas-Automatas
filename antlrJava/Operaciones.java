public class Operaciones {

    public static int operaciones(int aa, int bb, int c) {
        int operacion = aa-bb*c;
        return operacion;
    }

    public static void main(String[] args) {

        // Llamada a la función operaciones y mostrar el resultado

        System.out.println(operaciones(1, 2, 1));

    }

}
