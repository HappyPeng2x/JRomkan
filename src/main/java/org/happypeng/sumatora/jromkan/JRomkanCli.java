package org.happypeng.sumatora.jromkan;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class JRomkanCli 
{
    public static void main( String[] args )
    {
        try {
            Romkan romkan = new Romkan();
            
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            String input = "";
            String mode = "";
            String converted = "";
            int m = 0;

            System.out.println("Conversion type (1: hiragana 2: katakana 3: hepburn 4: kunrei):");

            while(mode.length() < 1){
                System.out.print("> ");
                mode = reader.readLine();
            }

            try {
                m = Integer.parseInt(mode);
            } catch (NumberFormatException e) {}

            if (!(m >= 1 && m <= 4)) {
                System.out.println("Unrecognized conversion type '" + mode + "'");

                return;
            }

            System.out.println("Input to be converted:");

            while(input.length() < 1){
                System.out.print("> ");
                input = reader.readLine();
            }

            if (m == 1) {
                converted = romkan.to_hiragana(input);
            } else if (m == 2) {
                converted = romkan.to_katakana(input);
            } else if (m == 3) {
                converted = romkan.to_hepburn(input);
            } else if (m == 4) {
                converted = romkan.to_kunrei(input);
            }

            System.out.println("Conversion result: '" + converted + "'");
        }
        catch(Exception e){
            System.out.println("An exception occured!");
            System.out.println(e.toString());
        }
    }
}
