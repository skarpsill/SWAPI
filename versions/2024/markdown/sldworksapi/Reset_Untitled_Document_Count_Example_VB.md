---
title: "Reset Untitled Document Count Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reset_Untitled_Document_Count_Example_VB.htm"
---

# Reset Untitled Document Count Example (VBA)

kadov_tag{{</spaces>}}For new untitled documents, SOLIDWORKS
increments the untitled document count and generates a document name by
appending the count to the document type. By default, Part1 is for the first untitled document in a SOLIDWORKS session,
Part2 for the next untitled document in that same SOLIDWORKS session, etc.).kadov_tag{{</spaces>}}The untitled
document count is automatically reset between SOLIDWORKS sessions.

You can use Ikadov_tag{{</spaces>}}SldWorks::ResetUntitledCount to
reset the untitled document
count within a single SOLIDWORKS session.

The following code example demonstrates how to use ISldWorks::ResetUntitledCount
to reset the untitled document count.kadov_tag{{</spaces>}}The
code resets the untitled document count at the beginning of the SOLIDWORKS
session, creates two
untitled documents, maximizes one document, and minimizes the second document.

**NOTE:**Programs designed to run multiple times in the same SOLIDWORKS session
should either assign titles to new documents or reset the untitled document
count at the beginning of the SOLIDWORKS session.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
ensures that SOLIDWORKS creates predictable names for untitled documents,
resulting in predictable outcomes for each invocation of the program.

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified document template
' exists.
'
' Postconditions:
' 1. Creates two new untitled part documents, Part9 and Part10;
'    maximizes Part9 and minimizes Part10.
' 2. Minimize Part9 and maximize Part10.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim Part2 As SldWorks.ModelDoc2
Dim ModelView As SldWorks.ModelView
Dim ModelView2 As SldWorks.ModelView
Dim boolstatus As Boolean
Dim longstatus As Long
Dim longwarnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Reset the counts for untitled
    ' documents (parts, assemblies, and drawings)
    ' to 8
    swApp.ResetUntitledCount 8, 8, 8
```

```
    ' When a new untitled document is created,
    ' SOLIDWORKS increments the untitled document
    ' count to 9
    ' The next untitled document gets a name with
    ' count = 9 ("Part9")
    Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc2 "Part9", False, longstatus
    Set Part = swApp.ActiveDoc
    Set ModelView = Part.ActiveView
```

```
    ' Maximize Part9
    ModelView.FrameState = swWindowState_e.swWindowMaximized
```

```
    ' When a new untitled document is created, SOLIDWORKS
    ' increments the untitled document count to 10
    ' The next untitled document gets a name with
    ' count = 10 ("Part10")
    Set Part2 = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc2 "Part10", False, longstatus
    Set Part2 = swApp.ActiveDoc
    Set ModelView2 = Part2.ActiveView
```

```
    ' Minimize Part10
    ModelView2.FrameState = swWindowState_e.swWindowMinimized
```

```
End Sub
```
