---
title: "Update Weldment Cut List and Fire Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VB.htm"
---

# Update Weldment Cut List and Fire Post-Notify Event Example (VBA)

This example shows how to handle the post-notification
event that fires

when the weldment cut list is updated.

```vb
'------------------------------------------------------
' Preconditions:
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Create main module with Main module code.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Insert Class1 module with Class1 module code.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Specified file to open exists.
' kadov_tag{{<spaces>}}4. Run macro (F5).
'
' Postconditions:
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Right-click on the Cut list folder.
' kadov_tag{{<spaces>}}2. Select Update from the right-click menu.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. A message box displays.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4. Click OK.
' kadov_tag{{<spaces>}}5. Stop the macro.
'--------------------------------------------------------------------------
' Main module
'--------------------------------------------------------------------------
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim swPartEvents As Class1
Dim swPart As SldWorks.PartDoc
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Option Explicit
Sub main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swDocSpecification.InteractiveComponentSelection = True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swDocSpecification.DocumentType = swDocPART
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.OpenDoc7(swDocSpecification)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swPart = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Set up event
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swPartEvents = New Class1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swPartEvents.swPart = swPart
End Sub

'--------------------------------------------------------------------------
' Class1 module
'--------------------------------------------------------------------------
Public WithEvents swPart As SldWorks.PartDoc
Private Function swPart_WeldmentCutListUpdatePostNotify() As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}MsgBox "The cut list is updated."
End Function
```
