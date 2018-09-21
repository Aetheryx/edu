/**
 * Practicum 1: Songtekst
 * Dit programma drukt de songtekst van een nummer af.
 *
 * @author Aetheryx
 */
public class Main {
    public static String repeat(String str, int count) {
        String repeated = new String(new char[count]).replace("\0", str);
        return repeated;
    }

    public static void main(String[] args) {
        final String VERSE_1 = repeat(
            "I'm a goner\n" +
            "Somebody catch my breath\n",
            2
        ) + repeat(
            "I wanna be known by you\n",
            2
        ) + "\n";

        final String VERSE_2 = repeat(
            "I’ve got two faces\n" +
            "Blurry’s the one I’m not\n",
            2
        ) + repeat(
            "I need your help to\n" +
            "Take him out\n",
            2
        ) + "\n";

        final String CHORUS = "Though I'm weak\n" +
            "And beaten down\n" +
            "I'll slip away\n" +
            "Into the sound\n" +
            "The ghost of you\n" +
            "Is close to me\n" +
            "I'm inside out\n" +
            "You're underneath\n\n";

        System.out.println(
            "Twenty One Pilots - Goner\n" +
            "\n" +
            repeat(VERSE_1, 2) +
            CHORUS +
            VERSE_2 +
            repeat(CHORUS, 2) +
            repeat("Don’t let me be gone\n", 4) +
            "\n" +
            repeat("Don't let me be!\n", 2) +
            "\n" +
            "Oh, yeah!\n" +
            "\n" +
            VERSE_1
        );
    }
}
