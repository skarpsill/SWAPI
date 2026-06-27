---
title: "Hide or Show First Column in Hole Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Column_in_Hole_Table_Example_VB.htm"
---

# Hide or Show First Column in Hole Table Example (VBA)

This example shows how to hide the first column in a hole table.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\simplehole.slddrw.
' 2. Select the hole table feature in the FeatureManager
'    design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Hides the first column.
' 2. Examine the hole table and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swHoleTableAnnotation As SldWorks.HoleTableAnnotation
    Dim swTableAnnotation As SldWorks.TableAnnotation
    Dim swAnnotation As SldWorks.Annotation
    Dim swHoleTable As SldWorks.HoleTable
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    If (swSelMgr.GetSelectedObjectCount = 0 Or Not (swSelMgr.GetSelectedObjectType(1) = swSelHOLETABLEFEATS)) Then
        MsgBox "Please select a hole table feature in the FeatureManager design tree."
        Exit Sub
    End If
```

```
    Set swHoleTable = swSelMgr.GetSelectedObject6(1, -1)
    Set swHoleTableAnnotation = swHoleTable.GetTableAnnotations(0)
    Set swTableAnnotation = swHoleTableAnnotation
    Set swAnnotation = swTableAnnotation.GetAnnotation
```

```
    ' If first column is hidden, then show it
    If (swTableAnnotation.ColumnHidden(0)) Then
        Debug.Print " First column hidden before API call: " & swTableAnnotation.ColumnHidden(0)
        swTableAnnotation.ColumnHidden(0) = False
        Debug.Print " First column hidden after API call:  " & swTableAnnotation.ColumnHidden(0)
    Else
        ' If first column is shown, then hide it
        Debug.Print " First column hidden before API call: " & swTableAnnotation.ColumnHidden(0)
        swTableAnnotation.ColumnHidden(0) = True
        Debug.Print " First column hidden after API call:  " & swTableAnnotation.ColumnHidden(0)
    End If
```

```
End Sub
```
