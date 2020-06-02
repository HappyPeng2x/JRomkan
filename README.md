# JRomkan

JRomkan is a Java library to convert Romaji to Hiragana, Katakana and vice-versa.

It is compatible with JDK 7 or newer and Android API 14 or newer.

It is a port of [python-romkan](https://github.com/soimort/python-romkan) from Mort Yao, itself the Pythonic port of [Ruby/Romkan](http://0xcc.net/ruby-romkan/index.html.en), originally authored by Satoru Takabayashi and [originally ported](http://lilyx.net/python-romkan/) by Masato Hagiwara. 

Its main destination will be to be used in [Sumatora Dictionary](https://github.com/HappyPeng2x/SumatoraDictionary), an offline free software Japanese dictionary for Android.


## Usage

JRomkan is available on JCenter.

### Maven

    <dependency>
	  <groupId>org.happypeng.sumatora.jromkan</groupId>
	  <artifactId>JRomkan</artifactId>
	  <version>1.0</version>
	  <type>pom</type>
    </dependency>

### Gradle

    implementation 'org.happypeng.sumatora.jromkan:JRomkan:1.0'

### Code

    import import org.happypeng.sumatora.jromkan.Romkan;

    void convert_strings(String my_romaji_input, 
            String my_kana_input) {
        Romkan romkan = new Romkan();

        String katakana = romkan.to_katakana(my_romaji_input);
        String hiragana = romkan.to_hiragana(my_romaji_input);

        String hepburn = romkan.to_hepburn(my_kana_input);
        String kunrei = romkan.to_kunrei(my_kana_input);

        // to_hepburn() also converts romaji from kunrei to hepburn
        // to_kunrei() also converts romaji from hepburn to kunrei
    }

## CLI

JRomkan also includes a very simple command line interface.

    $ java -jar build/romkan.jar
    Conversion type (1: hiragana 2: katakana 3: hepburn 4: kunrei):
    > 4
    Input to be converted:
    > ハロー、ワールド！
    Conversion result: 'haro-、war-rudo！'

## License

JRomkan is licensed under the GPL, either [version 3 of the License](https://www.gnu.org/licenses/gpl-3.0-standalone.html), or (at your option) any later version.

## Build

The JRomkan build system is standard maven. It can be built with the following commands:

    mvn package

Data can be generated from python-romkan using the following command:

    python3 jromkan-generate.py -c RomkanData -p org.happypeng.sumatora.jromkan -o src/main/java/org/happypeng/sumatora/jromkan/RomkanData.java