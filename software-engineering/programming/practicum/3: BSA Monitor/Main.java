import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Practicum 3: BSA calculator
 * Dit programma vertelt een gebruiker hun BSA aan de hand van ingevoerde cijfers.
 *
 * @author Aetheryx
 */
public class Main {
	// Declareer alle vakken met het bijbehorend aantal studiepunten
	private static final Map<String, Integer> /* <Vak, Studiepunten> */ VAKKEN = Map.of(
			"Fasten Your Seatbelts", 12,
			"Programming", 3,
			"Databases", 3,
			"Object Oriented Programming 1", 3,
			"User Interaction", 3,
			"Personal Skills", 2,
			"Project Skills", 2
	);

	// Het maximaal aantal haalbare studiepunten (met opzet dynamisch berekend)
	private static final int MAX_AANTAL_STUDIEPUNTEN = VAKKEN
			.values()
			.stream()
			.mapToInt(Integer::intValue)
			.sum();

	// De barriere voor een positief BSA
	private static final double BARRIERE_POSITIEF_BSA = (double) 5 / 6;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		HashMap<String, Double> behaaldeCijfers = new HashMap<String, Double>();
		int totaalBehaaldeStudiepunten = 0;

		System.out.println("Voer behaalde cijfers in:");

		// Itereer over de vakken, vraag en sla het cijfer op
		for (String vakNaam : VAKKEN.keySet()) {
			System.out.print(vakNaam + ": ");
			double behaaldCijfer = scanner.nextDouble();
			behaaldeCijfers.put(vakNaam, behaaldCijfer);
		}

		// lege regel
		System.out.println();

		// Bereken voor elk vak het aantal studiepunten, tel het op bij het totaal, print de informatie uit
		for (String vakNaam : VAKKEN.keySet()) {
			double behaaldCijfer = behaaldeCijfers.get(vakNaam);
			double behaaldeStudiepunten = behaaldCijfer >= 5.5
					? VAKKEN.get(vakNaam)
					: 0;

			totaalBehaaldeStudiepunten += behaaldeStudiepunten;

			System.out.printf(
					"Vak/project: %-30s Cijfer: %-6.1f Behaalde punten: %.0f\n",
					vakNaam,
					behaaldCijfer,
					behaaldeStudiepunten
			);
		}

		System.out.printf("\nTotaal behaalde studiepunten: %d/%d\n", totaalBehaaldeStudiepunten, MAX_AANTAL_STUDIEPUNTEN);

		// Het ratio van aantal behaalde studiepunten : maximaal haalbare studiepunten
		double studiePuntenRatio = (double) totaalBehaaldeStudiepunten / MAX_AANTAL_STUDIEPUNTEN;
		System.out.println(
				studiePuntenRatio >= BARRIERE_POSITIEF_BSA
						? "Je loopt op schema voor een positief BSA."
						: "PAS OP: je ligt op schema voor een negatief BSA!"
		);
	}
}
