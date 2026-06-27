---
title: "Get Break Line Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Break_Line_Data_Example_VBNET.htm"
---

# Get Break Line Data Example (VB.NET)

This example shows how to get information on all break lines in a view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create or open a drawing with one or more views that contain
 '    one or more break lines.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions: Inspect the Immediate Window.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Draw As DrawingDoc
     Dim swActiveView As View
     Dim Size As Long
     Dim Breaks As Long
     Dim info As Object
     Dim boolstatus As Boolean

     Sub main()

         Draw = swApp.ActiveDoc
         Dim count As Long
         count = Draw.GetViewCount
         Debug.Print("There are " & count & " views in this drawing including the sheet view.")
         Dim i As Long
         Dim j As Long
         swActiveView = Draw.GetFirstView ' get the sheet
         swActiveView = swActiveView.GetNextView ' get the first view
         For i = 0 To count - 2
             Debug.Print("View " & i + 1)
             Breaks = swActiveView.GetBreakLineCount2(Size)
             Debug.Print("   Number of breaks is " & Breaks)
             Debug.Print("   Size of break line data array is " & Size)

             If Not Breaks = 0 Then
                 info = swActiveView.GetBreakLineInfo2

                 ' General break line information
                 Debug.Print("   General break line info")
                 Debug.Print("     Style as defined in swBreakLineStyle_e: " & info(0))
                 Debug.Print("     Color (0 or -1 for default color): " & info(1))
                 Debug.Print("     Line type as defined in swLineTypes_e: " & info(2))
                 Debug.Print("     Line style as defined in swLineStyles_e: " & info(3))
                 Debug.Print("     Line weight as defined in swLineWeights_e: " & info(4))
                 Debug.Print("     Layer id: " & info(5))
                 Debug.Print("     Layer override as defined in swLayerOverride_e: " & info(6))
                 Debug.Print("     Number of line segments: " & info(7))
                 Debug.Print("     Number of arcs: " & info(8))
                 Debug.Print("     Number of jagged lines: " & info(9))

                 ' Straight, zigzag, arc, or jagged break line data
                 Debug.Print("")
                 Debug.Print("     Straight, zigzag, arc, or jagged break line data:")
                 For j = 10 To Size - 1
                     Debug.Print("      " & info(j))
                 Next j

             End If
             swActiveView = swActiveView.GetNextView
         Next i

     End Sub

     Public swApp As SldWorks

 End Class
```
