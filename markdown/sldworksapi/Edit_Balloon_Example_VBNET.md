---
title: "Edit Balloon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Balloon_Example_VBNET.htm"
---

# Edit Balloon Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim swNote As Note

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         ' Get the selected balloon
         swNote = swSelMgr.GetSelectedObject6(1, -1)

         ' Edit the selected balloon
         swNote = swModelDocExt.EditBalloonProperties2(swBalloonStyle_e.swBS_SplitCirc, swBalloonFit_e.swBF_5Chars, swBalloonTextContent_e.swBalloonTextCustom, "Upper", swBalloonTextContent_e.swBalloonTextCustom,  "Lower", 0, True, 1, "X", 0.0355)

         Debug.Print("Balloon name:  " & swNote.GetName)

     End Sub

     Public swApp As SldWorks

 End  Class
```
