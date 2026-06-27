---
title: "Manage Drawing Document Line Styles Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Manage_Drawing_Document_Line_Styles_Example_VB.htm"
---

# Manage Drawing Document Line Styles Example (VBA)

This example shows how to manage the line styles of a drawing document.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document template exists.
' 2. Ensure that c:\temp exists.
' 3. Open an Immediate Window.
'
' Postconditions:
' 1. Opens a new drawing.
' 2. Adds line styles.
' 3. Saves lines styles.
' 4. Deletes a line style.
' 5. Loads saved line styles, replacing existing line styles.
' 6. Inspect the Immediate window.
'
' NOTE: Line styles are saved to c:\temp\styles.sldlin.
'---------------------------------------------------------------

Option Explicit
```

```vb
 Dim swApp As SldWorks.SldWorks
Dim Part As DrawingDoc
 Dim boolstatus As Boolean
 Dim longstatus As Long

Sub main()
    Dim def As String
     Dim name As String

    Set swApp = Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\drawing.drwdot", 2, 0.2794, 0.4318)
     swApp.ActivateDoc2 "Draw1 - Sheet1", False, longstatus

    printData "Line Style Data at Start", ""

    def = "B,1.2,-0.2,2,-0.1,2"
     name = "NewOne"
     boolstatus = Part.AddLineStyle(name, def)
     printData "Line Style Data After Add", ""

    Dim names As Variant
     Dim styleNames(2) As String

    styleNames(0) = "NewOne"
     styleNames(1) = "CHAIN"
     styleNames(2) = "PHANTOM"

    names = styleNames

    ' Save line styles
     boolstatus = Part.SaveLineStyles("c:\temp\styles", names, True)
     printData "Line Style Data saved to file ", "c:\temp\styles"

    ' Delete a line style
     boolstatus = Part.DeleteLineStyle("NewOne", "STITCH")
     printData "Line Style Data After Delete", ""

    ' Load saved line styles, replacing existing line styles
     boolstatus = Part.LoadLineStyles("c:\temp\styles", names, True)
     printData "Line Style Data Imported from file", ""
End Sub
Sub printData(title As String, file As String)
    Dim names As Variant
     Dim types As Variant
     Dim i As Integer
     Dim stat As Boolean

    Debug.Print Chr$(10) + "-------------------------"
     Debug.Print title
     Debug.Print "-------------------------"

    If file = "" Then
        stat = Part.GetLineStyles(names, types)
     Else
        stat = swApp.GetLineStyles(file, names, types)
     End If

    If stat Then
        For i = 0 To UBound(types)
        Debug.Print Str$(i) + " ", names(i) + " " + types(i)
         Next i
     Else
         MsgBox "Error in printData"
     End If

End Sub
```
