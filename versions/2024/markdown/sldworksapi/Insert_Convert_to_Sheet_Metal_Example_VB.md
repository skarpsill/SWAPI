---
title: "Convert Extrusion to Sheet Metal Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Convert_to_Sheet_Metal_Example_VB.htm"
---

# Convert Extrusion to Sheet Metal Example (VBA)

This example shows how to convert a solid body to sheet metal.

```vb
 '--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\sweepcutextrude.sldprt.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Converts Boss-Extrude1 to sheet metal containing two rip edges.
 ' 2. Examine the FeatureManager design tree, which now contains:
 '    * Sheet-Metal1
 '    * Convert-Solid1
 '    * Flat-Pattern1
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '-------------------------------------------------------------------------
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
Sub main()
Set swApp = Application.SldWorks
```

```vb
Set Part = swApp.ActiveDoc
boolstatus = Part.Extension.SelectByID2("", "FACE", 4.130570195002E-04, 0.02357994168921, 0.02568415695742, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("", "EDGE", -0.00190522473838, 0.02387533864419, 0.04979931166838, True, 1, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.02911271681069, 0.02376277320678, 0.02892436699148, True, 1, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("", "EDGE", -0.004838857104858, 0.02387396382323, -1.997542986487E-04, True, 1, Nothing, 0)

' Convert extrusion to sheet metal of thickness=13mm, bend radius=0.5mm, rip gap=2mm,
 ' relief type = rectangular, relief ratio = 0.5, rip edge overlap type = open butt,
 ' and rip edge overlap ratio = 0.5, do not keep bodies
boolstatus = Part.FeatureManager.InsertConvertToSheetMetal2(0.013, False, False, 0.0005, 0.002, 0, 0.5, 1, 0.5, false)
Part.ClearSelection2 True
```

```vb
End Sub
```
