---
title: "Hide or Show First Column in Hole Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Column_in_Hole_Table_Example_VBNET.htm"
---

# Hide or Show First Column in Hole Table Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swHoleTableAnnotation As HoleTableAnnotation
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swTableAnnotation As TableAnnotation
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAnnotation As Annotation
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swHoleTable As HoleTable

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swSelMgr.GetSelectedObjectCount = 0 Or Not (swSelMgr.GetSelectedObjectType(1) = swSelectType_e.swSelHOLETABLEFEATS)) Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Please select a hole table feature in the FeatureManager design tree.")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swHoleTable = swSelMgr.GetSelectedObject6(1, -1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swHoleTableAnnotation = swHoleTable.GetTableAnnotations(0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swTableAnnotation = swHoleTableAnnotation
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAnnotation = swTableAnnotation.GetAnnotation

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If first column hidden, then show it
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swTableAnnotation.ColumnHidden(0)) Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" First column hidden before API call: " & swTableAnnotation.ColumnHidden(0))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTableAnnotation.ColumnHidden(0) = False
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" First column hidden after API call: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" & swTableAnnotation.ColumnHidden(0))
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' If first column shown, then hide it
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" First column hidden before API call: " & swTableAnnotation.ColumnHidden(0))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTableAnnotation.ColumnHidden(0) = True
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" First column hidden after API call: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" & swTableAnnotation.ColumnHidden(0))
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
