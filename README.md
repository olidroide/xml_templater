[![Tests](https://github.com/olidroide/xml_templater/actions/workflows/main.yml/badge.svg)](https://github.com/olidroide/xml_templater/actions/workflows/main.yml)

# xml_templater
POC parse xml into a txt template

### Input example
```xml
<?xml version="1.0" encoding="UTF-8"?>
<POLICY>
   <ID>1234</ID>
   <TITLE>TITLE EXAMPLE</TITLE>
   <CONTROL_LIST>
      <CONTROL>
         <ID>1111</ID>
         <STATEMENT>STATEMENT EXAMPLE</STATEMENT>
         <DESCRIPTION>EXAMPLE DESCRIPTION</DESCRIPTION>
      </CONTROL>
      <CONTROL>
         <ID>2222</ID>
         <STATEMENT>STATEMENT EXAMPLE 2</STATEMENT>
         <SUBCONTROL>
            <CONTROL>
                <ID>3333</ID>
                <STATEMENT>NESTED CONTROL SUB STATEMENT EXAMPLE 3</STATEMENT>
            </CONTROL>
         </SUBCONTROL>
      </CONTROL>
   </CONTROL_LIST>
</POLICY>
```

### Template example
```text
This is a *|policy.1234.title|*
A valid value for statement is *|policy.1234.control_list.control.1111.statement|*
Another statement is *|policy.1234.control_list.control.2222.statement|*
```

### Output example
```text
This is a TITLE EXAMPLE
A valid value for statement is STATEMENT EXAMPLE
Another statement is STATEMENT EXAMPLE 2
```

## How to use
```
python main.py -i input.xml -t template.txt
```