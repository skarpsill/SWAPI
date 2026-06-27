---
title: "Get Object ID of GTol Annotation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Object_ID_of_GTol_Annotation_Example_VBNET.htm"
---

# Get Object ID of GTol Annotation Example (VB.NET)

This example shows how to get the object ID of a GTol annotation.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Selects the GTol annotation.
' 3. Gets the type of annotation selected.
' 4. Gets the selected GTol annotation's object ID.
' 5. Examine the Immediate window.
'--------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swDrawing As DrawingDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swGTol As Gtol
        Dim swGTolAnnotation As Annotation
        Dim status As Boolean
        Dim errors As Integer, warnings As Integer
        Dim id As Integer

        'Open the drawing
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\gtolwitnessline.slddrw", 3, 0, "", errors, warnings)
        swDrawing = swModel

        'Select GTol
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("DetailItem40@Drawing View3", "GTOL", 0.44609485235144, 0.381203477032446, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swGTol = swSelectionMgr.GetSelectedObject6(1, -1)

        'Print type of annotation and its object ID
        swGTolAnnotation = swGTol.GetAnnotation
        Debug.Print("Annotation type: " & swGTolAnnotation.GetType)
        id = swModelDocExt.GetObjectId(swGTolAnnotation)
        Debug.Print("ID = " & id)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
