# Summary
This is a tool that helps dissect the information in CGM vector graphics files.

# Usage
This can be used programmatically for more advanced uses, or for basic printing 
of the elements of a CGM file there is a command line tool provided:
```
$ parse_cgm <file>
```

Or to print only the metadata/application data (i.e. non-graphics) parts of 
a cgm file:
```
$ parse_cgm -m <file>
```

# CGM standard
The CGM standard can be downloaded for free from from [iso.org](iso.org). Search 
for `ISO/IEC 8632` on the publicly available standards page: 
[https://standards.iso.org/ittf/PubliclyAvailableStandards/index.html](https://standards.iso.org/ittf/PubliclyAvailableStandards/index.html).

# CGM standard utility
There is a utility script that was used to extract information about the CGM 
standard.  This shouldn't be needed anymore but is here so I don't lose it and 
then need to re-scrape information from the CGM standard again.

```
./utils/make_cgm_types.py docs/c032380e.pdf cgm/types/parsed_types.py
```

This script requires installing `tabula-py`.  The makefile target 
`scrape-standard` automatically creates and uses a virtualenv to install tabula 
and run the script.

However the data scraped from the `docs/c032380e.pdf` PDF seems to be missing 
the `EDGE_WIDTH` element in one of the tables so the following element was 
patched in after running the script:
```diff
diff --git a/cgm/types/parsed_types.py b/cgm/types/parsed_types.py
index bff3e20..1482b42 100644
--- a/cgm/types/parsed_types.py
+++ b/cgm/types/parsed_types.py
@@ -1712,6 +1712,14 @@
     "len": "BIX",
     "range": "IXR"
   },
+  # 28 was manually added because the PDF is missing it?
+  28: {
+    "element": "EDGE_WIDTH",
+    "id": 28,
+    "type": "SS",
+    "len": "BSS",
+    "range": "SSR"
+  },
   29: {
     "element": "EDGE_COLOUR",
     "id": 29,
```
