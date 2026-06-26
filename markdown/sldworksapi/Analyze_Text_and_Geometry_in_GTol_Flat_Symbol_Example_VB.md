---
title: "Analyze Text and Geometry in GTol Symbol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_VB.htm"
---

# Analyze Text and Geometry in GTol Symbol Example (VBA)

This example shows how to analyze the text and geometry in a GTol symbol.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified part document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part document.
 ' 2. Gets whether <"GTOL-SPROF"> is bound.
 ' 3. Gets the number of lines, arcs, circles, text strings,
 '    and triangles in <"GTOL-SPROF">.
 ' 4. Gets the number of point coordinates in the
 '    lines in <"GTOL-SPROF">.
 ' 5. Gets the x,y,z coordinates for the first and second points
 '    of each line in <"GTOL-SPROF">.
 ' 6. Gets the arc information for <"GTOL-SPROF">.
 ' 7. Examine the Immediate window.
 '---------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swEnvironment As SldWorks.Environment
 Dim fileName As String
 Dim errors As Long
 Dim warnings As Long
 Dim nbrSymbols As Variant
 Dim lineSymbols As Variant
 Dim arcInfo As Variant
 Dim nbrLineCoordinates As Long
 Dim i As Long
Sub main()
     Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\minimum_clearance\top_plate.sldprt"
     Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
     Set swEnvironment = swApp.GetEnvironment

    Debug.Print "GTOL library - Surface Profile symbol name:"
```

```
    'Get whether <"GTOL-SPROF"> is bound
    Dim bound As Boolean
    swEnvironment.GetIsBound "<GTOL-SPROF>", bound
    Debug.Print (" Bound? " & bound)
    Debug.Print ("")
```

```vb
    'Get the number of lines, arcs, circles, text strings,
     'and triangles in <"GTOL-SPROF">
     nbrSymbols = swEnvironment.GetSymEdgeCounts("<GTOL-SPROF>")
     Debug.Print (" Line count:     " & nbrSymbols(0))
     Debug.Print (" Arc count:      " & nbrSymbols(1))
     Debug.Print (" Circle count:   " & nbrSymbols(2))
     Debug.Print (" Text count:     " & nbrSymbols(3))
     Debug.Print (" Triangle count: " & nbrSymbols(4))
     Debug.Print ""
     Debug.Print ("Number of lines: " & nbrSymbols(0))

    'Get the x,y,z coordinates for the first
     'and second points of each line
     lineSymbols = swEnvironment.GetSymLines("<GTOL-SPROF>")
     nbrLineCoordinates = UBound(lineSymbols)
     Debug.Print ("  Number of point coordinates: " & nbrLineCoordinates + 1)
     Debug.Print ("     Point coordinates:")
     Debug.Print ("       (Line 1's x,y,z coordinates for first and second points,")
     Debug.Print ("        Line 2's x,y,z coordinates for first and second points,")
     Debug.Print ("        ...)")
     For i = 0 To nbrLineCoordinates
         Debug.Print ("        " & lineSymbols(i))
     Next i
     Debug.Print ""
     Debug.Print ("Number of arcs: " & nbrSymbols(1))

    'Get the x,y,z coordinates of the center, start, and
     'end points of each arc, whether the arc is filled, and
     'whether a chord joining the start and end points of
     'the arc is drawn
     Debug.Print "  x,y,z coordinates of the center, start, and end points of each arc,"
     Debug.Print "  whether the arc is filled (1 = true, 0 = false),"
     Debug.Print "  and whether a chord is displayed for each arc (1 = true, 0 = false):"
     arcInfo = swEnvironment.GetSymArcs2("<GTOL-SPROF>")
     For i = 0 To UBound(arcInfo)
         Debug.Print ("        " & arcInfo(i))
     Next i

End Sub
```
