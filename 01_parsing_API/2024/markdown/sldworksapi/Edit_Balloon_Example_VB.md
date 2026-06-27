---
title: "Edit Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Balloon_Example_VB.htm"
---

# Edit Balloon Example (VBA)

This example shows how to edit a balloon in a drawing document.

```vb
' --------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 ' 2. Click Insert > Annotations > Balloon.
 ' 3. Click a model edge in either drawing view and add the balloon.
 ' 4. Close the Balloon PropertyManager page.
 ' 5. Select the balloon in the drawing.
 '
 ' Postconditions: The properties of the selected balloon are modified.
 '
 ' NOTE: Because this drawing document is used elsewhere, do not save any
 ' changes when closing it.
 ' --------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swNote As SldWorks.Note
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager

    ' Get the selected balloon
     Set swNote = swSelMgr.GetSelectedObject6(1, -1)

    ' Edit the selected balloon
     Set swNote = swModelDocExt.EditBalloonProperties2(swBS_SplitCirc, swBF_5Chars, swBalloonTextCustom, "Upper", swBalloonTextCustom, "Lower", 0, True, 1, "X", 0.0355)

    Debug.Print "Balloon name:  " & swNote.GetName
End Sub
```
