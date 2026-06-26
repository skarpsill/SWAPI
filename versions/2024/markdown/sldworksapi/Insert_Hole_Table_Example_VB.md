---
title: "Insert Hole Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hole_Table_Example_VB.htm"
---

# Insert Hole Table Example (VBA)

This example shows how to insert a hole table in a drawing.

```
'----------------------------------------------------------------------------
' Preconditions: Ensure that the specified part to open, drawing template,
' and hole table template exist.
'
' Postconditions:
' 1. Opens the part and creates a drawing of it.
' 2. Inserts a hole table of the part in the drawing.
' 3. Examine the hole table in the drawing.
'
' NOTE: Because the part is used elsewhere, do not save changes.
' ---------------------------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim spec As SldWorks.DocumentSpecification
Dim Drawing As SldWorks.DrawingDoc
Dim boolstatus As Boolean
```

```
Option Explicit
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set spec = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\cover_datum.sldprt")
    Set Part = swApp.OpenDoc7(spec)
    Set Drawing = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2019\templates\Drawing.drwdot", 2, 0.2794, 0.4318)
```

```
    Set Part = Drawing
```

```
    boolstatus = Part.Extension.SelectByID2("Sheet1", "SHEET", 0.39237, 0.5218942019544, 0, False, 0, Nothing, 0)
    boolstatus = Part.Create3rdAngleViews2("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\cover_datum.sldprt")
    Part.ClearSelection2 True
```

```
    boolstatus = Part.ActivateView("Drawing View1")
```

```
    'Select a vertex in the drawing view to be the origin of all datums in the table
    'All XLOC and YLOC table column values will be relative to this datum origin
    boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.117324728174898, 0.108554228680764, -500.0075, True, 1, Nothing, 0)
    'Select a face that contains the holes that will be annotated in the table
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.090728339186173, 0.119052803281577, -500.0075, True, 2, Nothing, 0)
```

```
    Dim myView As SldWorks.View
    Set myView = Part.SelectionManager.GetSelectedObjectsDrawingView2(1, -1)
    Dim myHoleTable As SldWorks.HoleTableAnnotation
    'Insert a hole table
    'anchored with its top left corner at x-coordinate = 0.07m and y-coordinate = 0.175m,
    'with starting datum tag "A",
    'using hole table template: standard hole table--letters.sldholtbt
    Set myHoleTable = myView.InsertHoleTable3(False, 0.153019881817662, -3.77259107537343E-02, 1, "A", "C:\Program Files\SolidWorks Corp\SOLIDWORKS\lang\english\standard hole table--letters.sldholtbt", 1, 1, Nothing)
```

```
    Part.ClearSelection2 True
```

```
    boolstatus = Part.ActivateSheet("Sheet1")
```

```
End Sub
```
