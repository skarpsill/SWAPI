---
title: "Add Watermark to Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Watermark_to_Part_Example_VBNET.htm"
---

# Add Watermark to Part Example (VB.NET)

This example shows how to add and modify a watermark.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Insert a note for a watermark.
'    a. Expand the Annotations folder in the FeatureManager
'       design tree.
'    b. Right-click Notes Area and click Activate.
'    c. Click Insert > Annotations > Note.
'    d. Place the note on the model, type the note text, and
'       click OK in the Note PropertyManager page.
'    e. Right-click the note and click Watermark.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Places the watermark behind the geometry and
'    sets its transparency level to 50%.
' 2. Examine the graphics area and the Immediate window.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swNote As Note
        Dim swSelectionMgr As SelectionMgr

        swModel = swApp.ActiveDoc
        swSelectionMgr = swModel.SelectionManager
        swNote = swSelectionMgr.GetSelectedObject6(1, 0)
	Debug.Print("Is note a watermark? " & swNote.WatermarkNote)
	swNote.WatermarkBehindGeometry = True
	Debug.Print("Is note behind geometry? " & swNote.WatermarkBehindGeometry)
	swNote.WatermarkTransparencyLevel = 0.5
	Debug.Print("Note transparency level = " & swNote.WatermarkTransparencyLevel * 100 & "%")

        swModel.ClearSelection2(True)
        swModel.EditRebuild3()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
