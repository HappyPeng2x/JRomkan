# JRomkan

JRomkan is a Java port of [python-romkan](https://github.com/soimort/python-romkan) from Mort Yao, itself the Pythonic port of [Ruby/Romkan](http://0xcc.net/ruby-romkan/index.html.en), originally authored by Satoru Takabayashi and [originally ported](http://lilyx.net/python-romkan/) by Masato Hagiwara. 

Its main destination will be to be used in [Sumatora Dictionary](https://github.com/HappyPeng2x/SumatoraDictionary), an offline free software Japanese dictionary for Android.

## Build

The JRomkan build system is based on [CMake](https://cmake.org/), and generates Java code from python-romkan.

The dependencies are as follows:
- CMake
- Python 3.x
- python-romkan
- JDK 7.x or newer

JRomkan can be built with the following commands:

    cmake .
    make

romkan.jar will be generated in the build directory.

## Usage

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