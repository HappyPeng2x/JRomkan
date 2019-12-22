#!/usr/bin/env python3
""" Data code generator for JRomkan based on Python-Romkan.

This program generates the database for use with the Android application 
Sumatora Dictionary.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import getopt

from romkan import common


def write_map(a_map, a_name, a_file):
    a_file.write("""  private static HashMap<String, String> """)
    a_file.write(a_name)
    a_file.write("""() {
    final HashMap<String, String> map = new HashMap<>();

""")

    for key in a_map:
        a_file.write('    map.put("' + key + '", "' + a_map[key] + '");\n')

    a_file.write("""
    return map;
  }

""")


HELP_STRING = "usage: jromkan-generate.py " \
    + "-c <class> -e <encoding> -p <package>"


def main(argv):
    output_class = ""
    encoding = ""
    package = ""

    try:
        opts, args = getopt.getopt(argv, "c:e:p:",
                                   ["class=", "encoding=", "package="])
    except getopt.GetoptError:
        print(HELP_STRING)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(HELP_STRING)
            sys.exit()
        elif opt in ("-c", "--class"):
            output_class = arg
        elif opt in ("-e", "--encoding"):
            encoding = arg
        elif opt in ("-p", "--package"):
            package = arg

    if output_class == "" or encoding == "":
        print(HELP_STRING)
        sys.exit(2)

    out = open(output_class + '.java.gen', 'w', encoding=encoding)

    if package != "":
        out.write("package " + package + ";\n\n")

    out.write("// This file was generated by jromkan-generate.py\n")
    out.write("import java.util.HashMap;\n\n");
    out.write("public class " + output_class + """ {
  private HashMap<String, String> ROMKAN;
  private HashMap<String, String> ROMKAN_H;
  private HashMap<String, String> KANROM;
  private HashMap<String, String> KANROM_H;
  private HashMap<String, String> TO_HEPBURN;
  private HashMap<String, String> TO_KUNREI;

  public HashMap<String, String> get_romkan() { return ROMKAN; }
  public HashMap<String, String> get_romkan_h() { return ROMKAN_H; }
  public HashMap<String, String> get_kanrom() { return KANROM; }
  public HashMap<String, String> get_kanrom_h() { return KANROM_H; }
  public HashMap<String, String> get_to_hepburn() { return TO_HEPBURN; }
  public HashMap<String, String> get_to_kunrei() { return TO_KUNREI; }

  public """ + output_class + """ () {
    ROMKAN = romkan();
    ROMKAN_H = romkan_h();
    KANROM = kanrom();
    KANROM_H = kanrom_h();
    TO_HEPBURN = to_hepburn();
    TO_KUNREI = to_kunrei();
  }

""")

    write_map(common.ROMKAN, 'romkan', out)
    write_map(common.KANROM, 'kanrom', out)
    write_map(common.ROMKAN_H, 'romkan_h', out)
    write_map(common.KANROM_H, 'kanrom_h', out)
    write_map(common.TO_HEPBURN, 'to_hepburn', out)
    write_map(common.TO_KUNREI, 'to_kunrei', out)

    # KANKAN_H = dict()
    # KAN_HKAN = dict()

    # for key in common.KANROM:
    #     try:
    #         KANKAN_H[key] = common.ROMKAN_H[common.KANROM[key]]
    #         KAN_HKAN[common.ROMKAN_H[common.KANROM[key]]] = key
    #     except KeyError:
    #         pass

    # write_map(KANKAN_H, 'kankan_h', out)
    # write_map(KAN_HKAN, 'kan_hkan', out)

    out.write("}")

    out.close()


if __name__ == "__main__":
    main(sys.argv[1:])