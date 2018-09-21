import java.util.Scanner;

/**
 * Practicum 2: Verkoopprijs
 * Dit programma kan een gebruiker helpen bij het berekenen van verkoop prijzen. 
 *
 * @author Aetheryx
 */
public class Main {
    static final double BTW_LAAG = 1.06;
    static final double BTW_HOOG = 1.21;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Inkoopprijs: ");
        double inkoopPrijs = scanner.nextDouble();

        System.out.print("Winstmarge (in %): ");
        double winstMarge = scanner.nextDouble();

        double verkoopExclusiefBTW = inkoopPrijs * ((winstMarge / 100) + 1);
        double verkoopBTWLaag = verkoopExclusiefBTW * BTW_LAAG;
        double verkoopBTWHoog = verkoopExclusiefBTW * BTW_HOOG;

        System.out.println("\nVerkoopprijs exclusief BTW: " + verkoopExclusiefBTW);
        System.out.println("Verkoopprijs inclusief 6% BTW: " + verkoopBTWLaag);
        System.out.println("Verkoopprijs inclusief 21% BTW: " + verkoopBTWHoog);
    }
}
